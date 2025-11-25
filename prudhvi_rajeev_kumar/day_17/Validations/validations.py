from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from enum import Enum
from typing import List, Optional
from datetime import date
import re

# Enums
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
    size_kb: int = Field(..., le=5000, description="Each file must be ≤ 5000 KB")

class SubTask(BaseModel):
    subtask_id: int
    title: str = Field(..., min_length=3)
    hours_spent: int = Field(..., ge=1, le=12)
    completed: bool = False

class EmployeeTask(BaseModel):
    employee_id: int = Field(..., gt=0, description="Must be positive")
    employee_name: str = Field(..., min_length=3, max_length=50, pattern=r"^[A-Za-z ]+$")
    email: EmailStr
    mobile: str = Field(..., pattern=r"^[6-9]\d{9}$")
    band: BandEnum
    emergency_contact: str = Field(..., pattern=r"^[6-9]\d{9}$")
    task_id: int = Field(..., gt=0)
    task_title: str = Field(..., min_length=3, max_length=50)
    task_description: str = Field(..., min_length=10, max_length=300)
    priority: PriorityEnum
    hours_spent: int = Field(..., ge=1, le=12)
    completed: bool = False
    subtasks: Optional[List[SubTask]] = []
    project_code: str = Field(..., min_length=3, max_length=8, pattern=r"^[A-Z0-9]+$")
    cost_center: str = Field(..., pattern=r"^[A-Z]{2}-\d{3}$")
    asset_code: str = Field(..., min_length=5, max_length=10, pattern=r"^[A-Z0-9]+$")
    supervisor_id: int = Field(..., gt=0)
    department: str = Field(..., min_length=3, pattern=r"^[A-Za-z]+$")
    location: str = Field(..., pattern=r"^[A-Za-z ]+$")

    # Dates
    start_date: date
    end_date: date

    # Additional Info
    skills: List[str]
    attachments: List[Attachment]
    remarks: Optional[str] = Field(None, max_length=200)
    client_feedback: Optional[str] = Field(None, max_length=500)

    # Validators
    @field_validator("email")
    def validate_email_domain(cls, v):
        if not v.endswith("@ust.com"):
            raise ValueError("email must end with @ust.com")
        return v

    @field_validator("task_id")
    def validate_task_id(cls, v, info):
        if v == info.data.get("employee_id"):
            raise ValueError("task_id cannot be same as employee_id")
        return v

    @field_validator("supervisor_id")
    def validate_supervisor_id(cls, v, info):
        if v == info.data.get("employee_id"):
            raise ValueError("supervisor_id cannot be same as employee_id")
        return v

    @field_validator("end_date")
    def validate_dates(cls, v, info):
        start_date = info.data.get("start_date")
        if start_date:
            if v <= start_date:
                raise ValueError("end_date must be after start_date")
            if (v - start_date).days > 30:
                raise ValueError("end_date must be within 30 days of start_date")
        return v

    @field_validator("start_date")
    def validate_start_date(cls, v):
        if v < date.today():
            raise ValueError("start_date cannot be in the past")
        return v

    @field_validator("skills")
    def validate_skills(cls, v):
        if not v:
            raise ValueError("skills list must contain at least one skill")
        if any(len(skill) < 2 for skill in v):
            raise ValueError("each skill must be at least 2 characters")
        if len(v) != len(set(v)):
            raise ValueError("skills cannot contain duplicates")
        if "hacking" in v:
            raise ValueError("skills contain forbidden items: hacking")
        return v

    @field_validator("attachments")
    def validate_attachments(cls, v):
        if not any(att.file_name.endswith(".pdf") for att in v):
            raise ValueError("attachments must include at least one PDF")
        if not any(att.file_name.endswith(".docx") for att in v):
            raise ValueError("attachments must include at least one DOCX")
        total_size = sum(att.size_kb for att in v)
        if total_size > 10000:
            raise ValueError("total attachment size exceeds limit")
        for att in v:
            if not re.match(r"^[A-Za-z0-9]+\.(pdf|docx)$", att.file_name):
                raise ValueError("attachment filename invalid")
        return v

    @field_validator("client_feedback")
    def validate_client_feedback(cls, v, info):
        if info.data.get("completed") and not v:
            raise ValueError("client_feedback required when task is completed")
        if info.data.get("priority") == PriorityEnum.high and info.data.get("completed") and (not v or len(v) < 10):
            raise ValueError("client_feedback must be ≥10 chars for high priority completed tasks")
        return v

    @field_validator("hours_spent")
    def validate_hours_spent(cls, v, info):
        if info.data.get("priority") == PriorityEnum.high and v > 8:
            raise ValueError("hours_spent exceeds daily limit for high priority")
        if info.data.get("band") == BandEnum.M1 and v > 10:
            raise ValueError("M1 band cannot have hours_spent > 10")
        return v
    
    @model_validator(mode="after")
    def check_band_priority(self):
        if self.band == BandEnum.B1 and self.priority == PriorityEnum.high:
            raise ValueError("B1 band cannot have high priority tasks")
        return self
    
    @model_validator(mode="after")
    def check_startswith(self):
        if not self.cost_center.startswith(self.department[:2].upper()):
            raise ValueError("cost_center must start with department abbreviation")
        return self
    
    @field_validator("task_title")
    def check_task_title(cls, v):
        banned = ["urgent", "fix"]
        if any(word.lower() in v.lower() for word in banned):
            raise ValueError("Contains critical words.")
        return v
    
    @field_validator("task_description")
    def check_taskdescription(cls, v):
        required = ["finance", "guidelines", "report"]
        if not any(word in v.lower() for word in required):
            raise ValueError("It should contain at least one required word")
        return v


# Sample Data 
sample_task = {
    "employee_id": 101,
    "employee_name": "Rahul Menon",
    "email": "rahul.menon@ust.com",
    "mobile": "9876543210",
    "band": "B2",
    "emergency_contact": "9123456789",

    "task_id": 501,
    "task_title": "Prepare monthly report",
    "task_description": "Complete the monthly finance report with detailed analysis and submit to supervisor.",
    "priority": "medium",
    "hours_spent": 8,
    "completed": False,

    "subtasks": [
        {"subtask_id": 1, "title": "Collect data", "hours_spent": 3, "completed": True},
        {"subtask_id": 2, "title": "Draft report", "hours_spent": 5, "completed": False}
    ],

    "project_code": "FIN123",
    "cost_center": "FI-202",   
    "asset_code": "AST9001",
    "supervisor_id": 200,
    "department": "Finance",
    "location": "Kochi",

    "start_date": "2025-12-01",
    "end_date": "2025-12-20",

    "skills": ["python", "excel", "analysis"],
    "attachments": [
        {"file_name": "plan.pdf", "size_kb": 2000},
        {"file_name": "notes.docx", "size_kb": 1500}
    ],
    "remarks": "Completed initial draft on time",
    "client_feedback": "Well done, detailed and clear"
}

task = EmployeeTask(**sample_task)
print(task)
