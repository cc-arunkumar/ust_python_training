from pydantic import BaseModel
from typing import List

class UserLogin(BaseModel):
    username: str
    password: str


class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    """Used for creating a task (no 'completed' in request)"""
    pass


class TaskUpdate(TaskBase):
    """Used for updating a task (full update, includes 'completed')"""
    completed: bool


class Task(TaskBase):
    """Response model for a task"""
    id: int
    completed: bool = False
