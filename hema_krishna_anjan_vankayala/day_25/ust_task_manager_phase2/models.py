from pydantic import BaseModel, Field
from typing import Optional

# Schema for tasks (used for validation and API responses)
class TaskSchema(BaseModel):
    id: Optional[int] = Field(default=1)  # Task ID (auto-generated in DB)
    title: str = Field(..., min_length=1, description="Task title")  # Title of the task
    description: str = Field(..., description="description")  # Task description
    completed: Optional[bool] = Field(default=False, description="Completion")  # Completion status
    
    class Config:
        orm_mode = True  # Enables compatibility with ORM objects


# Schema for users (used for validation and API responses)
class UserSchema(BaseModel):
    user_id: Optional[int] 
    user_name: str = Field(...)  # Username
    user_password: str = Field(...)  # User password 
    
    class Config:
        orm_mode = True 


# Schema for JWT tokens
class Token(BaseModel):
    access_token: str  # JWT access token string
    token_type: str    # Token type (usually "Bearer")


# Schema for authenticated user
class UserID(BaseModel):  # Changed from username to user ID
    user_id: str 
