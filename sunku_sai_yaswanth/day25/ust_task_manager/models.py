from typing import Optional
from pydantic import BaseModel
# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # Import Base from database.py

# Pydantic models for validation and response

# TaskInResponse: Pydantic model used for returning task data in response
class TaskInResponse(BaseModel):
    id: int  # Task ID (int)
    title: str  # Task title (string)
    description: str  # Task description (string)
    completed: bool  # Whether the task is completed or not (boolean)

    class Config:
        orm_mode = True  # Allow Pydantic models to work with SQLAlchemy models

# TaskCreate: Pydantic model used for creating a new task (request body)
class TaskCreate(BaseModel):
    title: str  # Task title (string)
    description: str  # Task description (string)
    completed: Optional[bool] = False  # Whether the task is completed (optional, default is False)

# TaskUpdate: Pydantic model used for updating an existing task (request body)
class TaskUpdate(BaseModel):
    title: Optional[str] = None  # Optional task title (string)
    description: Optional[str] = None  # Optional task description (string)
    completed: Optional[bool] = None  # Optional task completion status (boolean)

# LoginRequest: Pydantic model for validating the login request body
class LoginRequest(BaseModel):
    username: str  # Username for login (string)
    password: str  # Password for login (string)

# UserInResponse: Pydantic model used for returning user data in response
class UserInResponse(BaseModel):
    id: int  # User ID (int)
    username: str  # Username (string)

    class Config:
        orm_mode = True  # Allow Pydantic models to work with SQLAlchemy models
