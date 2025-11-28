from typing import Optional
from pydantic import BaseModel, Field
from auth import get_current_user


class TaskModel(BaseModel):
    """Full Task model for storing tasks"""
    id: int
    title: str
    description: str
    completed: bool


class TaskModelCreate(BaseModel):
    """Model for creating a new task"""
    title: str = Field(..., description="Field is required")
    description: str = Field(..., description="Field is required")


class TaskModelUpdate(BaseModel):
    """Model for updating an existing task"""
    title: str = Field(..., description="Field is required")
    description: str = Field(..., description="Field is required")
    completed: bool = Field(..., description="Field is required")