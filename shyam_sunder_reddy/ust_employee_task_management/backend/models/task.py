from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TaskReqRes(BaseModel):
    t_id: Optional[int] = None
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=250)
    assigned_to: Optional[int] = None
    assigned_by: Optional[int] = None
    assigned_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    updated_at: Optional[datetime] = None
    priority: str = Field(..., description="high, medium, low")
    status: Optional[str] = Field(default="TO_DO")
    reviewer: Optional[int] = None
    created_by: Optional[int] = None
    expected_closure: datetime
    actual_closure: Optional[datetime] = None

    class Config:
        orm_mode = True
        from_attributes = True
