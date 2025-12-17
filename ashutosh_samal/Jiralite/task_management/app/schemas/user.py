from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    roles: List[str]
    status: str


class UserCreate(UserBase):
    e_id: int
    password: str


class UserUpdate(UserBase):
    password: str


class UserPatch(BaseModel):
    status: str


class UserOut(UserBase):
    e_id: int

    class Config:
        from_attributes = True
