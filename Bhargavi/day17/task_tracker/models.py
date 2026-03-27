from pydantic import BaseModel, Field
from typing import Optional

# Base model for the Task that will be used for both creating and responding with task data.
class Task(BaseModel):
    # Title of the task, which must be between 1 and 255 characters long.
    title: str = Field(..., min_length=1, max_length=255)  # '...' indicates that this field is required
    # Description of the task, which must be between 1 and 500 characters long.
    description: str = Field(..., min_length=1, max_length=500)  # '...' indicates that this field is required
    # Boolean flag indicating whether the task is completed or not. Defaults to False.
    completed: bool = False

    class Config:
        orm_mode = True

# TaskInResponse model extends the base Task model and adds the `id` field.
class TaskInResponse(Task):
    # Adding the `id` field, which is returned as part of the task response.
    id: int

# TaskCreate is used when creating a new task. It inherits from the `Task` model.

class TaskCreate(Task):
    pass

# TaskUpdate is used when updating an existing task. All fields are optional, meaning they can be updated individually.
class TaskUpdate(BaseModel):
    # Title is optional and can be updated. No validation on length as it might not be provided.
    title: Optional[str] = None
    # Description is optional and can be updated. No validation on length as it might not be provided.
    description: Optional[str] = None
    completed: Optional[bool] = None

# This model is used to validate the request body when a user attempts to log in.
class LoginRequest(BaseModel):
    # Username is required for login.
    username: str
    # Password is required for login.
    password: str
