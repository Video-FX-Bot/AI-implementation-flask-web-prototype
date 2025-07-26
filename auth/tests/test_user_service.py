import pytest
import asyncio
from datetime import datetime
from app.database.session import users_collection  # Your real MongoDB collection
from app.schemas.user_schema import UserCreate, UserOut
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.schemas.user_schema import UserUpdate

@pytest.mark.asyncio
async def test_mongo_crud():
    repo = UserRepository()
    service = UserService(repo)

    # 1. Create user
    user_create = UserCreate(
        username="testuser",
        email="testuser3@example.com",
        password="password123",
        isEmailVerified=False,
        subscription={
            "plan": "free",
            "status": "inactive",
            "startDate": datetime.utcnow(),
            "endDate": datetime.utcnow(),
            "paymentMethod": None,
            "paymentProviderCustomerId": None,
        },
        roles=["user"],
    )
    created_user = await service.register_user(user_create)
    assert created_user.email == "testuser3@example.com"
    user_id = created_user.id  # or created_user._id depending on schema

    # 2. Read user
    fetched_user = await service.get_user(user_id)
    assert fetched_user.email == "testuser3@example.com"

    # 3. Update user
    update_data = UserUpdate(isEmailVerified=True)
    updated = await service.update_user(user_id, update_data)
    assert updated is True

    # 4. Confirm update
    updated_user = await service.get_user(user_id)
    assert updated_user.isEmailVerified is True

    # 5. Delete user (if you have a delete method)
    # await repo.delete(user_id)   # Implement if you want cleanup

    # Optionally clean up test data:
    await users_collection.delete_one({"_id": user_id})
