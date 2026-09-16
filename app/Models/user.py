from typing import Optional
from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    phone_number: str
    address: str
    milkman_id: Optional[int] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    milkman_id: Optional[int] = None


class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


User = UserResponse
