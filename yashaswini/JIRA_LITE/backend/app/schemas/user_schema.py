from pydantic import BaseModel, Field
from typing import List


class UserBase(BaseModel):
    emp_id: str = Field(..., max_length=5)
    roles: List[str]
    status: str = Field(default="active", pattern="^(active|inactive)$")


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


class UserResponse(BaseModel):
    emp_id: str
    roles: List[str]
    status: str

    class Config:
        from_attributes = True
