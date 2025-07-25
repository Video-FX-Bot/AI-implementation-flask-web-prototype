from app.database.session import users_collection
from app.schemas.user_schema import UserOut
from bson import ObjectId
from typing import Optional
import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRepository:

    @staticmethod
    async def get_by_email(email: str) -> Optional[UserOut]:
        data = await users_collection.find_one({"email": email})
        if data:
            data["_id"] = str(data["_id"])
            return UserOut(**data)
        return None

    @staticmethod
    async def get_by_id(user_id: str) -> Optional[UserOut]:
        data = await users_collection.find_one({"_id": ObjectId(user_id)})
        if data:
            data["_id"] = str(data["_id"])
            return UserOut(**data)
        return None

    @staticmethod
    async def create(user_data: dict) -> UserOut:
        user_data["passwordHash"] = pwd_context.hash(user_data.pop("password"))
        user_data["createdAt"] = datetime.datetime.utcnow()
        user_data["updatedAt"] = datetime.datetime.utcnow()
        user_data.setdefault("isEmailVerified", False)
        user_data.setdefault("roles", ["user"])
        user_data.setdefault("subscription", None)
        user_data.setdefault("loginAttempts", 0)
        user_data.setdefault("isDisabled", False)

        result = await users_collection.insert_one(user_data)
        user_data["_id"] = str(result.inserted_id)
        return UserOut(**user_data)

    @staticmethod
    async def update(user_id: str, update_data: dict) -> bool:
        update_data["updatedAt"] = datetime.datetime.utcnow()
        result = await users_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )
        return result.modified_count == 1
