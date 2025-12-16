from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

PRIORITIES = {"low", "medium", "high", "critical"}
STATUSES = {"open", "in_progress", "review", "done", "closed"}

class TaskBase(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    description: Optional[str] = None
    assigned_to: int
    priority: str = Field(pattern="^(low|medium|high|critical)$")
    status: str = Field(pattern="^(open|in_progress|review|done|closed)$")
    remark: Optional[str] = Field(default=None, max_length=500)
    reviewer: Optional[int] = None
    expected_closure: Optional[datetime] = None

class TaskCreate(TaskBase):
    assigned_by: int
    created_by: int

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=2, max_length=200)
    description: Optional[str] = None
    assigned_to: Optional[int] = None
    priority: Optional[str] = Field(default=None, pattern="^(low|medium|high|critical)$")
    status: Optional[str] = Field(default=None, pattern="^(open|in_progress|review|done|closed)$")
    remark: Optional[str] = Field(default=None, max_length=500)
    reviewer: Optional[int] = None
    expected_closure: Optional[datetime] = None
    actual_closure: Optional[datetime] = None
    updated_by: Optional[int] = None

class TaskOut(BaseModel):
    taskid: int
    title: str
    description: Optional[str]
    assigned_to: int
    assigned_by: int
    assigned_at: datetime
    priority: str
    status: str
    remark: Optional[str]
    reviewer: Optional[int]
    expected_closure: Optional[datetime]
    actual_closure: Optional[datetime]
    updated_by: Optional[int]
    updated_at: Optional[datetime]
    created_by: int
