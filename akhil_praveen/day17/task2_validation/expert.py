from pydantic import BaseModel, EmailStr, validator,Field,model_validator
from enum import Enum
from typing import List, Optional
from datetime import datetime,date,timedelta
from fastapi import FastAPI,HTTPException,status
from functools import reduce

app = FastAPI(title="Validation")

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
    subtasks: Optional[List[SubTask]] = []
    hours_spent: int 
    completed: bool = False
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
    def valid_or_not(self):
        subtask = self.subtasks 
        total = sum(x.hours_spent for x in subtask)
        if self.hours_spent<total:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,detail="sum subtask should be less than hours spent")
        if self.completed == True:
            for sub in self.subtasks:
                if sub.completed != self.completed:
                    raise HTTPException(status_code=422 , detail="cannot complete task with incomplete subtasks")
                
        if self.priority=="low":
            for skill in self.skills:
                if skill=="Python":
                    raise HTTPException(status_code=422,detail="tasks with Python skill cannot have low priority")
        for attach in self.attachments:
            if attach.file_name.endswith(".docx"):
                if str(self.task_id) not in attach.file_name:
                    raise HTTPException(status_code=422,detail="docx attachments must include task_id")
        if self.hours_spent>8 and self.remarks==None:
            raise HTTPException(status_code=422,detail="remarks required when hours > 8")
        if self.band=="B3"and self.cost_center.startswith("HR"):
                raise HTTPException(status_code=422,detail="B3 band cannot work on HR cost centers")
        
        if self.completed and self.priority=="high" and len(self.client_feedback)<10:
            raise HTTPException(status_code=422,detail="client_feedback must be >=10 chars for high priority completed tasks")
        
        fiscal_start = date(self.start_date.year, 4, 1)

        fiscal_end = date(self.start_date.year + 1, 3, 31)

        if not (fiscal_start <= self.start_date <= fiscal_end and fiscal_start <= self.end_date <= fiscal_end):

            raise HTTPException(status_code=422,

                detail="task dates must be within fiscal year")
        
        for att in self.attachments:
            if att.size_kb > 2000:
                raise HTTPException(status_code=422,
                    detail="subtask attachment size cannot exceed 2000 KB")
                
        return self
    
    
emp_list : List[EmployeeTask] = [] 
    
@app.post("/validation")
def create(task:EmployeeTask):
    emp_list.append(task)
    return task    
# {
#     "employee_id": 101,
#     "employee_name": "Rahul Sharma",
#     "email": "rahul.sharma@example.com",
#     "mobile": "+91-9876543210",
#     "band": "B2",
#     "emergency_contact": "+91-9123456789",
#     "task_id": 5001,
#     "task_title": "Develop Employee Portal",
#     "task_description": "Create a web-based portal for employees to manage HR-related tasks.",
#     "priority": "high",
#     "subtasks": [
#         {
#             "subtask_id": 1,
#             "title": "Design UI",
#             "hours_spent": 15,
#             "completed": true
#         },
#         {
#             "subtask_id": 2,
#             "title": "Backend API Development",
#             "hours_spent": 25,
#             "completed": false
#         },
#         {
#             "subtask_id": 3,
#             "title": "Integration Testing",
#             "hours_spent": 10,
#             "completed": false
#         }
#     ],
#     "hours_spent": 55,
#     "completed": false,
#     "project_code": "PRJ-EMP-2025",
#     "cost_center": "CC-IT-001",
#     "asset_code": "AST-DEV-123",
#     "supervisor_id": 2001,
#     "department": "Information Technology",
#     "location": "Mumbai",
#     "start_date": "2025-11-01",
#     "end_date": "2025-12-15",
#     "skills": ["Python", "Django", "React", "SQL"],
#     "attachments": [
#         {
#             "file_name": "requirements.docx",
#             "size_kb": 120
#         },
#         {
#             "file_name": "design_mockup.png",
#             "size_kb": 450
#         }
#     ],
#     "remarks": "Pending integration with payroll system.",
#     "client_feedback": "UI design appreciated, backend performance needs improvement."
# }