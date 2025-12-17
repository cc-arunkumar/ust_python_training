from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    dept_name: Optional[str] = None
    assigned_to: Optional[int] = None
    reviewer: Optional[int] = None
    priority: Optional[str] = None
    status: Optional[Literal["TO_DO", "IN_PROGRESS", "REVIEW", "DONE"]] = "TO_DO"
    expected_closure: Optional[datetime] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    dept_name: Optional[str] = None
    assigned_to: Optional[int] = None
    reviewer: Optional[int] = None
    priority: Optional[str] = None
    expected_closure: Optional[datetime] = None


class TaskStatusPatch(BaseModel):
    status: Literal["TO_DO", "IN_PROGRESS", "REVIEW", "DONE"]
    review: Optional[str] = None


class TaskResponse(TaskCreate):
    task_id: int

    class Config:
        from_attributes = True