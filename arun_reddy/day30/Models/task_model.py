from typing import Literal, Optional,List
from pydantic import BaseModel
from datetime import datetime

class Remark(BaseModel):
    description: str

class Task(BaseModel):
    title: str
    description: str
    assigned_to: Optional[int]   # employee id
    assigned_at: Optional[datetime]
    assigned_by: Optional[int]   # manager id
    updated_by: int
    updated_at: Optional[datetime] = None
    priority: Literal["low", "medium", "high"] = "low"
    status: Literal["to-do", "in_progress", "review", "completed"] = "to-do"
    remarks: Optional[List[dict]] = None
    expected_closure: datetime
    actual_closure: Optional[datetime] = None

class TaskCreate(BaseModel):
    title: str
    description: str
    assigned_to: Optional[int]   # employee id
    assigned_at: Optional[datetime]
    assigned_by: Optional[int]   # manager id
    priority: Literal["low", "medium", "high"] = "low"
    status: Literal["to-do", "in_progress", "review", "completed"] = "to-do"
    remarks: Optional[List[dict]] = None
    expected_closure: datetime
    actual_closure: Optional[datetime] = None
    updated_by: int
    
    
class TaskStatus(BaseModel):
    status:Literal["to-do", "in_progress", "review", "completed"] = "to-do"

class AssignTaskRequest(BaseModel):
    task_id: str 
    employee_id: int

    