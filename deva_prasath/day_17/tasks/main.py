from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from enum import Enum

class BandEnum(str, Enum):
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    M1 = "M1"

class EmployeeTask(BaseModel):
    employee_id: int
    employee_name: str
    email: EmailStr
    mobile: str
    band: BandEnum
    task_id: int
    task_title: str
    task_description: str
    hours_spent: int
    completed: bool = False

def validate_employee_task(task: EmployeeTask):
    if task.employee_id<=0:
        raise ValueError('employee_id must be positive')
    if task.task_id<=0:
        raise ValueError('task_id must be positive')
    if task.task_id==task.employee_id:
        raise ValueError('task_id cannot be the same as employee_id')

    if len(task.employee_name)<3 or task.employee_name==" ":
        raise ValueError('employee_name must be at least 3 characters long')

    if len(task.mobile)!=10:
        raise ValueError('mobile must be exactly 10 digits')

    if len(task.task_title)<3:
        raise ValueError('task_title must be at least 3 characters long')

    if len(task.task_description)<10:
        raise ValueError('task_description must be at least 10 characters long')

    if task.hours_spent<1 or task.hours_spent>12:
        raise ValueError('hours_spent must be between 1 and 12')
    
    if '@' not in task.email and '.' not in task.email.split('@')[1]:
        raise ValueError('Email eroor')

    
    return task

app = FastAPI()

@app.post("/task/")
async def create_task(task: EmployeeTask):
    try:
        validated_task = validate_employee_task(task)
        return {"message": "Task created successfully", "task": validated_task}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    





from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import date
from typing import List
import re
from datetime import date,timedelta

class BandEnum(str, Enum):
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    M1 = "M1"
    
class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    
    
class EmployeeTask(BaseModel):
 # Employee Info
    employee_id: int
    employee_name: str
    email: EmailStr
    mobile: str
    band: BandEnum
    
    # Task Info
    task_id: int
    task_title: str
    task_description: str
    priority: PriorityEnum
    hours_spent: int
    completed: bool= False
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
    
    skills: List[str]
    attachments: List[str]
    remarks: str


def validate_task(task:EmployeeTask):
    if not task.project_code.isalnum() or not task.project_code.isupper() or not len(task.project_code)>3 or not len(task.project_code)<8:
        raise HTTPException(status_code=400,detail="Invalid project code")

    if not re.match(r'^[A-Z]{2}-\d{3}$', task.cost_center):
        raise HTTPException(status_code=400, detail="cost_center format invalid")
    
    if not re.match(r'^[A-Z]{3}\d{2,7}$',task.cost_center):
        raise HTTPException(status_code=400,detail="Wrong asset code")
    
    if task.supervisor_id>0:
        raise HTTPException(status_code=400,detail="Positive employee_id must")
    
    if task.employee_id==task.supervisor_id:
        raise HTTPException(status_code=400,detail="Employee_id and supervisor id must not be same")
    
    if not re.match(r'^[A-Za-z]{3,}$',task.department):
        raise HTTPException(status_code=400,detail="department must contain only letters")

    if not re.match(r'^[A-Za-z]{1}[A-za-z]$',task.location):
        raise HTTPException(status_code=400,detail="location must contain only letters")

    if task.start_date>task.end_date:
        raise HTTPException(status_code=400,detail="end_date must be after start_date")
    
    if len(task.skills)>0:
        raise HTTPException(status_code=400,detail="skills list must contain at least one skill")
    if len(task.skills)!=len(set(task.skills)):
        raise HTTPException(status_code=400,detail="skills cannot contain duplicates")
    for i in task.skills:
        if len(i)<2:
            raise HTTPException(status_code=400,detail="each skill must be at least 2 characters")
        
    if len(task.attachments) == 0:
        raise HTTPException(status_code=400, detail="all attachments must be PDF files and non-empty")
    
    for attachment in task.attachments:
        if not attachment or not attachment.endswith('.pdf'):
            raise HTTPException(status_code=400, detail="all attachments must be PDF files and non-empty")
    
    if task.remarks and len(task.remarks) < 5:
        raise HTTPException(status_code=400, detail="remarks must be at least 5 characters")
    
    if task.priority not in PriorityEnum.__members__:
        raise HTTPException(status_code=400, detail="priority must be one of: low, medium, high")
    
    if task.hours_spent<1 or task.hours_spent>12:
        raise ValueError('hours_spent must be between 1 and 12')
    
    if not re.match(r'^[A-Za-z]+(\s[A-za-z]+)*$',task.employee_name):
        raise HTTPException(status_code=400,detail="employee_name must contain only letters and spaces")
    
    if not re.match(r'^[6-9]\d{9}$',task.mobile):
        raise HTTPException(status_code=400,detail="Invalid phone number")
    
    if not re.match(r'^[A-Za-z0-9+-%_.]+@ust.com]$',task.email):
        raise HTTPException(status_code=400,detail="Invalid email")
    
    if len(task.task_title)>50:
        raise HTTPException(status_code=400, detail="task_title must not exceed 50 characters")
    
    if len(task.task_description)>300:
        raise HTTPException(status_code=400, detail="task_description must not exceed 300 characters")
    
    if task.start_date<date.today():
        raise HTTPException(status_code=400, detail="start_date cannot be in the past")

    if task.end_date>task.start_date+timedelta(days=30):
        raise HTTPException(status_code=400, detail="end_date must be within 30 days of start_date")




from pydantic import BaseModel, EmailStr, validator
from enum import Enum
from typing import List, Optional,Set
from datetime import date

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
    completed: bool =False
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
    # Optional conditional field
    client_feedback: Optional[str]


used_employee_ids: Set[int] = set()

def validate_task(task: EmployeeTask):
    # Scenario 31: Check if employee_id is unique
    if task.employee_id in used_employee_ids:
        raise HTTPException(status_code=400, detail="employee_id must be unique")
    
    # If unique, add employee_id to the in-memory set
    used_employee_ids.add(task.employee_id)

    return task
