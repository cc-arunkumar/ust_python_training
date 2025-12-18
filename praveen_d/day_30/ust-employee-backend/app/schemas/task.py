from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime

class TaskSchema(BaseModel):
    task_id: str = Field(..., min_length=3, max_length=50)
    name: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5, max_length=500)

    assigned_to: str
    assigned_by: str
    reviewer: Optional[str] = None
    created_by: str
    updated_by: Optional[str] = None

    priority: str
    status: str

    assigned_at: Optional[datetime] = None
    expected_closure: datetime
    actual_closure: Optional[datetime] = None
    remarks: Optional[str] = None

    @field_validator("status")
    def validate_status(cls, value):
        allowed = {"TO_DO", "IN_PROGRESS", "REVIEW", "DONE"}
        if value not in allowed:
            raise ValueError(f"status must be one of {allowed}")
        return value

    @field_validator("priority")
    def validate_priority(cls, value):
        allowed = {"HIGH", "MEDIUM", "LOW"}
        value = value.upper()
        if value not in allowed:
            raise ValueError(f"priority must be one of {allowed}")
        return value

    # class Config:
    #     from_attributes = True
