from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate, UserOut
from typing import Optional

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def register_user(self, user_create: UserCreate) -> UserOut:
        existing = await self.repo.get_by_email(user_create.email)
        if existing:
            raise ValueError("Email already registered")

        user_dict = user_create.dict()
        return await self.repo.create(user_dict)

    async def update_user(self, user_id: str, user_update: UserUpdate) -> bool:
        update_data = user_update.dict(exclude_unset=True)
        return await self.repo.update(user_id, update_data)

    async def get_user(self, user_id: str) -> Optional[UserOut]:
        return await self.repo.get_by_id(user_id)