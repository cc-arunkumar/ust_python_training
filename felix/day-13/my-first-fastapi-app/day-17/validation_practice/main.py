from pydantic import BaseModel ,EmailStr, validator ,model_validator,Field
from enum import Enum
from typing import List, Optional
from datetime import date
from fastapi import FastAPI

app = FastAPI()

class BandEnum(str, Enum):
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    M1 = "M1"
class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
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
    # Employee Info
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
    
    @model_validator(mode="after")
    def check_completion(self):
        completed = self.completed
        subtasks = self.subtasks or []
        if completed and not all(i.completed for i in subtasks):
            raise ValueError("Cannot complete task with incomplete subtasks")
        return self
    
    @model_validator(mode="after")
    def sub_task_validator(self):
        task_hours = self.hours_spent
        subtasks = self.subtasks or []
        total_subtask_hours = sum(i.hours_spent for i in subtasks)
        if total_subtask_hours > task_hours:
            raise ValueError("sum of subtask hours cannot exceed task hours")
        return self
    
    @model_validator(mode="after")
    def skill_validate(self):
        skill_set = self.skills
        priority_val = self.priority
        if "python" in skill_set and priority_val == "low":
            raise ValueError( "tasks with Python skill cannot have low priority")
        return self
    
    @model_validator(mode="after")
    def emergency_contact(self):
        if self.emergency_contact == self.supervisor_id:
            raise ValueError("emergency_contact cannot match supervisor_id")
        return self
    
    @model_validator(mode="after")
    def dependent_remark(self):
        if self.hours_spent>8 and self.remarks == None:
            raise ValueError( "remarks required when hours > 8")
        return self
    
    @model_validator(mode="after")
    def band_and_project(self):
        if self.band == "B3" and self.cost_center.split("-")[0] == "HR":
            raise ValueError("B3 band cannot work on HR cost centers")
        return self
    
    @model_validator(mode="after")
    def client_feedback(self):
        if self.completed and self.priority == "high" and (self.client_feedback == None or len(self.client_feedback)<10):
            raise ValueError("client_feedback must be ≥10 chars for high priority completed tasks")
        return self
    
    @model_validator(mode="after")
    def cross_check(self):
        fy_start = date(self.start_date.year,4,1)
        fy_end = date(self.start_date.year+1,3,31)
        if not (fy_start <= self.start_date <= fy_end) or not (fy_start <= self.end_date <= fy_end):
            raise ValueError("task dates must be within fiscal year")
        return self

    @model_validator(mode="after")
    def attachment(self):
        file = self.attachments
        for i in file:
            if i.size_kb>2000:
                raise ValueError("subtask attachment size cannot exceed 2000 KB")
        return self

@app.post("/sub_task")
def sub_task_hours(employee:EmployeeTask):
    return employee