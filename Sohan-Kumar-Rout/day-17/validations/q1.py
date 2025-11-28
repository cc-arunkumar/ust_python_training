from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import List
from datetime import date, timedelta
from fastapi import FastAPI, HTTPException
import re

app = FastAPI(title="Validations")

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
    employee_id: int
    employee_name: str
    email: EmailStr
    mobile: str
    band: BandEnum
    task_id: int
    task_title: str
    task_description: str
    priority: PriorityEnum
    hours_spent: int
    completed: bool = False
    project_code: str
    cost_center: str
    asset_code: str
    supervisor_id: int
    department: str
    location: str
    start_date: date
    end_date: date
    skills: List[str]
    attachments: List[str]
    remarks: str

@app.post("/employee/tasks")
def create_employee(employee: EmployeeTask):
    # Regex patterns
    project_pattern = r"^[A-Z0-9]{3,8}$"
    cost_center_pattern = r"^[A-Z]{2}-\d{3}$"
    asset_pattern = r"^[A-Z]{3}\d{4}$"
    name_pattern = r"^[A-Za-z ]+$"

    # Project code validation
    if not re.match(project_pattern, employee.project_code):
        raise HTTPException(status_code=400, detail="project_code must be 3-8 uppercase letters/numbers")

    # Cost center validation
    if not re.match(cost_center_pattern, employee.cost_center):
        raise HTTPException(status_code=400, detail="cost_center format invalid (e.g., AB-123)")

    # Asset code validation
    if not re.match(asset_pattern, employee.asset_code):
        raise HTTPException(status_code=400, detail="asset_code format invalid (e.g., ABC1234)")

    # Supervisor validation
    if employee.supervisor_id <= 0:
        raise HTTPException(status_code=400, detail="supervisor_id must be positive")
    if employee.supervisor_id == employee.employee_id:
        raise HTTPException(status_code=400, detail="supervisor_id cannot be same as employee_id")

    # Department validation
    if len(employee.department) < 3 or not employee.department.isalpha():
        raise HTTPException(status_code=400, detail="department must contain at least 3 letters")

    # Location validation
    if not employee.location.isalpha():
        raise HTTPException(status_code=400, detail="location must contain only letters")

    # Date validation
    if employee.start_date >= employee.end_date:
        raise HTTPException(status_code=400, detail="end_date must be after start_date")
    if employee.start_date < date.today():
        raise HTTPException(status_code=400, detail="start_date cannot be in past")
    if employee.end_date != employee.start_date + timedelta(days=30):
        raise HTTPException(status_code=400, detail="end_date must be exactly 30 days after start_date")

    # Skills validation
    if len(employee.skills) == 0:
        raise HTTPException(status_code=400, detail="Skills list must contain at least one skill")
    for skill in employee.skills:
        if len(skill) < 2:
            raise HTTPException(status_code=400, detail="Each skill must be at least 2 characters")

    # Attachments validation
    for attachment in employee.attachments:
        if not attachment.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="All attachments must be PDF files")

    # Remarks validation
    if len(employee.remarks) < 5:
        raise HTTPException(status_code=400, detail="remarks must be at least 5 characters")

    # Hours spent validation
    if not 1 <= employee.hours_spent <= 12:
        raise HTTPException(status_code=400, detail="hours_spent must be between 1-12")

    # Employee name validation
    if not re.match(name_pattern, employee.employee_name):
        raise HTTPException(status_code=400, detail="employee_name must contain only letters and spaces")

    # Mobile validation
    if employee.mobile[0] not in ["6", "7", "8", "9"]:
        raise HTTPException(status_code=400, detail="mobile number must start with 6,7,8,9")

    # Email validation
    if not employee.email.endswith("@ust.com"):
        raise HTTPException(status_code=400, detail="email must end with @ust.com")

    # Task title validation
    if len(employee.task_title) > 50:
        raise HTTPException(status_code=400, detail="task_title must not exceed 50 characters")

    # Task description validation
    if len(employee.task_description) > 300:
        raise HTTPException(status_code=400, detail="task_description must be less than 300 characters")

    return {"message": "Employee task created successfully"}
