"""from pydantic import BaseModel
from enum import Enum
from typing import Optional
from datetime import datetime, date


class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TaskStatus(str, Enum):
    TO_DO = "TO_DO"
    IN_PROGRESS = "IN_PROGRESS"
    REVIEW = "REVIEW"
    COMPLETED = "COMPLETED"


class TaskCreate(BaseModel):
    title: str
    remarks: Optional[str] = None
    priority: TaskPriority = TaskPriority.medium
    assigned_to: int
    reviewer: int
    expected_closure: Optional[date] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    remarks: Optional[str] = None
    priority: Optional[TaskPriority] = None
    assigned_to: Optional[int] = None
    reviewer: Optional[int] = None
    expected_closure: Optional[date] = None
    actual_closure: Optional[date] = None


class TaskStatusUpdate(BaseModel):
    status: TaskStatus


class TaskResponse(BaseModel):
    task_id: int
    title: str
    remarks: Optional[str]
    priority: TaskPriority
    status: TaskStatus

    assigned_to: int
    assigned_by: int
    reviewer: int

    created_by: int
    updated_by: Optional[int]

    assigned_at: datetime
    updated_at: Optional[datetime]

    expected_closure: Optional[date]
    actual_closure: Optional[date]

    class Config:
        from_attributes = True


from pydantic import BaseModel
from enum import Enum

class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskStatusUpdate(BaseModel):
    status: StatusEnum
    priority: PriorityEnum
"""

from pydantic import BaseModel
from enum import Enum
from typing import Optional, List
from datetime import datetime, date

class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskStatus(str, Enum):
    TO_DO = "TO_DO"
    IN_PROGRESS = "IN_PROGRESS"
    REVIEW = "REVIEW"
    COMPLETED = "COMPLETED"

class TaskCreate(BaseModel):
    title: str
    remarks: Optional[str] = None
    priority: TaskPriority = TaskPriority.medium
    assigned_to: int
    reviewer: int
    expected_closure: Optional[date] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    remarks: Optional[str] = None
    priority: Optional[TaskPriority] = None
    assigned_to: Optional[int] = None
    reviewer: Optional[int] = None
    expected_closure: Optional[date] = None
    actual_closure: Optional[date] = None

class TaskStatusUpdate(BaseModel):
    status: TaskStatus
    priority: TaskPriority

class TaskRemarksUpdate(BaseModel):
    remarks: str

class TaskResponse(BaseModel):
    task_id: int
    title: str
    remarks: Optional[str]
    priority: TaskPriority
    status: TaskStatus
    assigned_to: int
    assigned_by: int
    reviewer: int
    created_by: int
    updated_by: Optional[int]
    assigned_at: datetime
    updated_at: Optional[datetime]
    expected_closure: Optional[date]
    actual_closure: Optional[date]

    class Config:
        from_attributes = True

class PaginatedTaskResponse(BaseModel):
    tasks: List[TaskResponse]
    total: int
    page: int
    limit: int