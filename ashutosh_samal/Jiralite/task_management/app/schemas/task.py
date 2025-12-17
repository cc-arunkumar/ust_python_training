from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: int
    priority: Optional[str] = "MEDIUM"
    expected_closure: Optional[datetime] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    assigned_to: Optional[int] = None
    priority: Optional[str] = None
    expected_closure: Optional[datetime] = None
    remarks: Optional[str] = None


class TaskStatusUpdate(BaseModel):
    status: str
    remarks: Optional[str] = None


class TaskResponse(BaseModel):
    t_id: int
    title: str
    description: Optional[str]
    assigned_to: int
    created_by: int
    assigned_by: int
    reviewer: Optional[int]
    priority: str
    status: str
    remarks: Optional[str]
    assigned_at: datetime
    updated_at: Optional[datetime]
    expected_closure: Optional[datetime]
    actual_closure: Optional[datetime]

    class Config:
        from_attributes = True
