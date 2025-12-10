# Import required libraries
from pydantic import BaseModel, Field   # BaseModel for data validation, Field for metadata
from typing import Optional       # Optional for nullable fields


# ---------------- TASK MODEL ----------------
class TaskSchema(BaseModel):
    task_id: Optional[int] = None   # Task ID (auto-assigned when created)
    title: str = Field(..., description="Enter proper title")   # Task title (required)
    description: str = Field(..., description="Enter proper description for the task")  # Task description (required)
    completed: bool = Field(False, description="Mark it as true or false")  # Task status (default: False)
    
    class Config:
        orm_mode=True


# ---------------- LOGIN REQUEST MODEL ----------------
class LoginRequest(BaseModel):
    username: str   # Username provided by user
    password: str   # Password provided by user


# ---------------- TOKEN MODEL ----------------
class Token(BaseModel):
    access_token: str   # JWT access token
    token_type: str     # Token type (usually "bearer")


# ---------------- USER MODEL ----------------
class UserSchema(BaseModel):
    user_id:Optional[int]=None
    username: str   # Username of the user
    password: str   # Password of the user
    
    class Config:
        orm_mode = True

