from typing import Optional
from pydantic import BaseModel
# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # Import Base from database.py

# SQLAlchemy models

# Pydantic models for validation and response
class TaskInResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True  # Allow Pydantic models to work with SQLAlchemy models

class TaskCreate(BaseModel):
    title: str
    description: str
    completed:Optional[bool]=False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class LoginRequest(BaseModel):
    username: str
    password: str

class UserInResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
