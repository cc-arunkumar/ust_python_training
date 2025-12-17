from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    TO_DO = "TO_DO"
    IN_PROGRESS = "IN_PROGRESS"
    REVIEW = "REVIEW"
    COMPLETED = "COMPLETED"

class TaskCreate(BaseModel):
    task_id: str = Field(..., max_length=10)
    title: str
    description: str
    priority: str
    assigned_to: str
    assigned_by: str
    created_by: str

    expected_closure: Optional[datetime] = None

class TaskUpdate(BaseModel):
    status: Optional[TaskStatus] = None
    remarks: Optional[str] = None
    reviewer: Optional[str] = None
    actual_closure: Optional[datetime] = None
