# Updated Model Class (Extended for Expert Level)
from pydantic import BaseModel, EmailStr, validator
from enum import Enum
from typing import List, Optional
from datetime import date



class BandEnum(str, Enum):
 B1 = "B1"
 B2 = "B2"
 B3 = "B3"
 M1 = "M1"
class PriorityEnum(str, Enum):
 low = "low"
 medium ="medium"
 high = "high"
class Attachment(BaseModel):
 file_name: str
 size_kb: int
 
 
class SubTask(BaseModel):
 subtask_id: int
 title: str
 hours_spent: int
 completed: bool = False
 
 
class EmployeeTask(BaseModel):
 employee_id: int
 employee_name: str
 email: EmailStr
 mobile: str
 band: BandEnum
 emergency_contact: str
 # Task Info
 task_id: int
 task_title: str
 task_description: str
 priority: PriorityEnum
 hours_spent: int
 completed: bool = False
 subtasks: Optional[List[SubTask]] = []
 # Project Info
 project_code: str
 cost_center: str
 asset_code: str
 supervisor_id: int
 department: str
 location: str
 # Dates
 start_date: date
 end_date: date
 # Additional Info
 skills: List[str]
 attachments: List[Attachment]
 remarks: Optional[str]
 client_feedback: Optional[str]
 
#  Scenario 61 — Subtask hours
# Validation: Sum of subtasks.hours_spent ≤ task.hours_spent
# Valid: task hours=10, subtasks=5+5
# Invalid: task hours=10, subtasks=6+5
# Error: "sum of subtask hours cannot exceed task hours"

# @validator('subtasks', pre=True, always=True)
    # def validate_subtask_hours(cls, v, values):
    #     # Check if subtasks are provided and sum up the hours spent on them
    #     task_hours = values.get('hours_spent', 0)
    #     if v:
    #         total_subtask_hours = sum(subtask.hours_spent for subtask in v)
    #         if total_subtask_hours > task_hours:
    #             raise ValueError("Sum of subtask hours cannot exceed task hours")
    #     return v