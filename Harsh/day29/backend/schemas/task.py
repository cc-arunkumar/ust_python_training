from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

ALLOWED_STATUSES = ["TODO", "ON_PROCESS", "REVIEW", "DONE", "BLOCKED"]
ALLOWED_PRIORITIES = ["high", "medium", "low"]

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: Optional[int] = None
    reviewer: Optional[int] = None
    priority: Optional[str] = None
    status: Optional[str] = "TODO"
    expected_closure: Optional[datetime] = None

    @field_validator("priority")
    def validate_priority(cls, v):
        if v and v.lower() not in ALLOWED_PRIORITIES:
            raise ValueError(f"priority must be one of {ALLOWED_PRIORITIES}")
        return v.lower() if v else v

    @field_validator("status")
    def validate_status(cls, v):
        if v not in ALLOWED_STATUSES:
            raise ValueError(f"status must be one of {ALLOWED_STATUSES}")
        return v

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    assigned_to: Optional[int] = None
    reviewer: Optional[int] = None
    priority: Optional[str] = None
    expected_closure: Optional[datetime] = None

    @field_validator("priority")
    def validate_priority(cls, v):
        if v and v.lower() not in ALLOWED_PRIORITIES:
            raise ValueError(f"priority must be one of {ALLOWED_PRIORITIES}")
        return v.lower() if v else v

class TaskStatusPatch(BaseModel):
    status: str
    review: Optional[str] = None

    @field_validator("status")
    def validate_status(cls, v):
        if v not in ALLOWED_STATUSES:
            raise ValueError(f"status must be one of {ALLOWED_STATUSES}")
        return v

class TaskPriorityUpdate(BaseModel):
    priority: str

    @field_validator("priority")
    def validate_priority(cls, v):
        if v.lower() not in ALLOWED_PRIORITIES:
            raise ValueError(f"priority must be one of {ALLOWED_PRIORITIES}")
        return v.lower()

class TaskResponse(TaskCreate):
    task_id: int

    class Config:
        from_attributes = True
