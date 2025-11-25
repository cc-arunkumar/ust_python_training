from pydantic import BaseModel, Field  # Import Pydantic for data validation
from typing import Optional  # For optional type hinting

# Task model for task-related data
class Task(BaseModel):
    # Title field with a minimum and maximum length constraint
    title: str = Field(..., min_length=1, max_length=255)
    
    # Description field with a minimum and maximum length constraint
    description: str = Field(..., min_length=1, max_length=500)
    
    # Completed flag to track task completion (default: False)
    completed: bool = False

    # Pydantic configuration class (used for serialization and deserialization)
    class Config:
        # Changed from `orm_mode` to `from_attributes` to support attribute-based models
        from_attributes = True


# TaskInResponse model extends Task and includes an ID field for API responses
class TaskInResponse(Task):
    id: int


# TaskCreate model is used for creating tasks (no extra fields, inherits from Task)
class TaskCreate(Task):
    pass


# TaskUpdate model allows optional updates to task fields (fields are not required)
class TaskUpdate(BaseModel):
    title: Optional[str] = None  # Optional title field
    description: Optional[str] = None  # Optional description field
    completed: Optional[bool] = None  # Optional completed field


# LoginRequest model for user authentication with username and password fields
class LoginRequest(BaseModel):
    username: str  # Username field
    password: str  # Password field
