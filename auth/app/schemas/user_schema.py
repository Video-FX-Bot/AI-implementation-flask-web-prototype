from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class Subscription(BaseModel):
    plan: str
    status: str
    startDate: datetime
    endDate: datetime
    paymentMethod: Optional[str] = None
    paymentProviderCustomerId: Optional[str] = None


class UserBase(BaseModel):
    username:str
    email: EmailStr

class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    isEmailVerified: Optional[bool] = None
    subscription: Optional[Subscription] = None
    roles: Optional[List[str]] = None


class UserOut(UserBase):
    id: str = Field(..., alias="_id")
    isEmailVerified: bool
    subscription: Optional[Subscription]
    roles: List[str]
    createdAt: datetime
    updatedAt: datetime

    class Config:
        allow_population_by_field_name = True


