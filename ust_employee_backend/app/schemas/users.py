from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    emp_id: int
    roles: List[str]   # ["ADMIN", "MANAGER"]
    status: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    roles: List[str] | None = None
    status: str | None = None
    password: str | None = None

class UserLogin(BaseModel):
    emp_id: int
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class UserStatusUpdate(BaseModel):
    status: str