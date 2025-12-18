from pydantic import BaseModel,field_validator
from typing import Optional,Literal,List
from datetime import datetime,date

class Task(BaseModel): 
    title: str
    description: str
    assigned_to: Optional[int]
    assigned_by: Optional[int] = None
    reviewer: int 
    assigned_at: Optional[datetime] = None
    updated_by: int
    updated_at: datetime = datetime.now()
    priority: Literal['Low', 'Medium', 'High']
    status: Literal['To Do', 'In Progress','Review', 'Done']
    remarks: Optional[List[dict]] = None
    expected_completion_date: datetime
    actual_completion_date: Optional[datetime] = None
    
class TaskCreate(BaseModel):
    title: str
    description: str
    assigned_to: Optional[int]
    reviewer: int 
    assigned_by: Optional[int] = None
    assigned_at: Optional[datetime] = None
    updated_by: int
    priority: Literal['Low', 'Medium', 'High'] = 'Low'
    status: Literal['To Do', 'In Progress','Review', 'Done']
    remarks: Optional[List[dict]] = None
    expected_completion_date: datetime
    actual_completion_date: Optional[datetime] = None

    @field_validator("expected_completion_date", "actual_completion_date", mode="before")
    @classmethod
    def normalize_date(cls, value):
        if value is None:
            return value

        if isinstance(value, str):
            value = datetime.fromisoformat(value.replace("Z", "+00:00"))

        return value

class TaskUpdate(BaseModel):
    status: Optional[Literal['To Do', 'In Progress','Review', 'Done']] = None
    remarks: Optional[List[dict]] = None
    assigned_to: Optional[int] = None
    assigned_by: Optional[int] = None
    assigned_at: Optional[datetime] = None
    updated_by: int
    updated_at: datetime = datetime.now()
    actual_completion_date: Optional[date] = None
    priority: Optional[Literal['Low', 'Medium', 'High']] ='Low'
    
class TaskStatusUpdate(BaseModel):
    status: Literal['To Do', 'In Progress','Review', 'Done']
    
class TaskRemarksUpdate(BaseModel):
    remarks: str