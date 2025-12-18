from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "medium"
    expected_closure: Optional[datetime] = None

# ---------- Base ----------
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

    assigned_to_id: Optional[int] = None
    assigned_by_id: Optional[int] = None
    created_by_id: Optional[int] = None

    reviewer: Optional[int] = None
    remarks: Optional[str] = None

    status: Optional[str] = "TO_DO"
    priority: Optional[str] = None

    expected_closure: Optional[datetime] = None
    actual_closure: Optional[datetime] = None


# ---------- Assign ----------
class TaskAssign(BaseModel):
    assigned_to_id: int
    reviewer: Optional[int] = None



# ---------- Status ----------
class TaskStatusUpdate(BaseModel):
    status: str


# ---------- Review decision ----------
class TaskReviewDecision(BaseModel):
    action: str  # APPROVE | REJECT
    remarks: Optional[str] = None


# ---------- Priority update ----------
class TaskPriorityUpdate(BaseModel):
    priority: str

class TaskResponse(TaskBase):
    id: int
    assigned_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None   # <-- add here
    updated_by: Optional[int] = None
    
    class Config:
        from_attributes = True
