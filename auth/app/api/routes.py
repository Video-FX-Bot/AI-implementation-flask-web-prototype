from fastapi import APIRouter, HTTPException, status
from app.schemas.user_schema import UserCreate, UserUpdate, UserOut
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["users"])
user_service = UserService(UserRepository())

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user_create: UserCreate):
    try:
        user = await user_service.register_user(user_create)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: str):
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/{user_id}", response_model=dict)
async def update_user(user_id: str, user_update: UserUpdate):
    success = await user_service.update_user(user_id, user_update)
    if not success:
        raise HTTPException(status_code=404, detail="User not found or no changes made")
    return {"message": "User updated successfully"}
