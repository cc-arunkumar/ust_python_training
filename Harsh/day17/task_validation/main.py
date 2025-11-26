from pydantic import BaseModel, Field,field_validator
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
    medium = "medium"
    high = "high"

class EmployeeTask(BaseModel):
    # Employee Info
    employee_id: int = Field(..., ge=1, description="Must be positive integer (>0)")
    employee_name: str = Field(..., min_length=3, pattern=r'^[A-Za-z ]+$', description="Only letters and spaces")
    email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@ust\.com$',description="Must be a valid email address")
    mobile: str = Field(..., pattern=r'^[6-9]\d{9}$', description="Must be 10 digits starting with 6,7,8,9")
    band: BandEnum

    # Task Info
    task_id: int = Field(..., ge=1, description="task_id must be positive")
    task_title: str = Field(...,pattern=r'^[A-Za-z ]+$', min_length=3, max_length=50, description="task_title must be 3-50 characters")
    task_description: str = Field(..., min_length=10, max_length=300, description="task_description must be 10–300 characters")
    priority: PriorityEnum
    hours_spent: int = Field(..., ge=1, le=12, description="hours_spent must be between 1 and 12")

    # Project Info
    project_code: str = Field(..., pattern=r'^[A-Z0-9]{3,8}$', description="3-8 uppercase letters/numbers")
    cost_center: str = Field(..., pattern=r'^[A-Z]{2}-\d{3}$', description="Format: 2 uppercase letters + '-' + 3 digits")
    asset_code: str = Field(..., pattern=r'^[A-Z]{2,}[0-9]{2,}$', min_length=5, max_length=10, description="Prefix letters + digits, length 5-10")
    supervisor_id: int = Field(..., ge=1, description="Must be positive integer")
    department: str = Field(..., min_length=3, pattern=r'^[A-Za-z]+$', description="Letters only, min 3 chars")
    location: str = Field(..., pattern=r'^[A-Za-z]+$', description="City name letters only")

    # Dates
    start_date: date
    end_date: date

    # Additional Info
    skills: List[str] = Field(..., min_items=1, description="At least one skill, each ≥2 chars")
    attachments: List[str] = Field(..., description="All must be non-empty and end with .pdf")
    remarks: Optional[str] = Field(None, min_length=5, description="Optional, if present must be ≥5 chars")
    completed: bool = Field(default=False, description="Boolean, default False")

    
    @field_validator("supervisor_id")
    def validate_supervisor_id(cls, supervisor_id, info):
        employee_id = info.data.get("employee_id")
        if employee_id is not None and supervisor_id == employee_id:
            raise ValueError("supervisor_id cannot be same as employee_id")
        return supervisor_id

    @field_validator("end_date")
    def validate_end_date(cls, end_date, info):
        start_date = info.data.get("start_date")
        if start_date is not None:
            if end_date <= start_date:
                raise ValueError("end_date must be after start_date")
            if (end_date - start_date).days > 30:
                raise ValueError("end_date must be within 30 days of start_date")
        return end_date
    
    @field_validator("skills")
    def validate_skills(cls,value):
        if len(value)<1:
            raise ValueError("skills must contain atleast one skill")
        for skill in value:
            if len(skill)<2:
                raise ValueError("each skill must be at least 2 characters")
        
        if len(value)!=len(set(value)):
            raise ValueError("skills cannot contain duplicates")
        return value
    
    @field_validator("attachments")
    def validate_attachments(cls,value):
        for v in value:
            if not v.endswith(".pdf") or v=="":
                raise ValueError("all attachments must be PDF files and non-empty")
        return value
    
    @field_validator("priority")
    def validate_priority(cls, value):
        allowed = {"low", "medium", "high"}
        if value not in allowed:
            raise ValueError("priority must be one of: low, medium, high")
        return value 

try:
    task = EmployeeTask(
        employee_id=101,
        employee_name="Rahul Menon",
        email="rahul.menon@ust.com",
        mobile="9876543210",
        band="B1",
        task_id=501,
        task_title="A"*51,
        task_description="Complete the monthly report thoroughly with detailed analysis",
        priority="less",
        hours_spent=8,
        project_code="FIN123",
        cost_center="HR-202",
        asset_code="DEV0012",
        supervisor_id=101,
        department="Finance",
        location="Kochi",
        start_date="2025-03-10",
        end_date="2025-01-25",
        skills=["python", "python"],
        attachments=["", "design.pdf"],
        remarks="Completed on time",
        completed=True
    )
    print(" Task created successfully")
    print(task)
except Exception as e:
    print(" Validation Error:", e)
