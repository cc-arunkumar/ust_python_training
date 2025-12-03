from pydantic import BaseModel, Field, EmailStr, field_validator
from enum import Enum
import re
from typing import List, Optional
from datetime import date ,timedelta

class BandEnum(str, Enum):
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    M1 = "M1"

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

existing_emp_ids=set()
active_project_codes=set()

class EmployeeTask(BaseModel):
    start_date: date
    end_date: date
    employee_id: int = Field(ge=1)
    employee_name: str = Field(min_length=3)
    email: EmailStr
    mobile_number: str = Field(regex=r'^\d{10}$')
    band: BandEnum
    task_id: int = Field(ge=1)
    task_title: str = Field(min_length=3)
    task_description: str = Field(min_length=10)
    hours_spent: int = Field(ge=1, le=12)
    completed: bool = Field(default=False)
    project_code: str = Field(regex=r'^[A-Z0-9]{3,8}$')
    cost_center: str = Field(regex=r'^[A-Z]{2}-\d{3}$')
    asset_code: str = Field(regex=r'^[A-Z]+[0-9]+$', min_length=5, max_length=10)
    supervisor_id: int = Field(ge=1)
    department: str = Field(regex=r'^[A-Za-z]+$',min_length=3)
    location: str = Field(regex=r'^[A-Za-z]+$')
    attachments: List[str]
    remarks: Optional[str] = None
    priority: PriorityEnum
    emergency_contact:str
    skills:List[str]=Field(ge=2)

    @field_validator("task_id")
    def validate_task_id(cls, v, values):
        if v <= 0:
            raise ValueError("task_id must be positive")
        if "employee_id" in values and v == values["employee_id"]:
            raise ValueError("task_id cannot be equals to employee id")
        return v

    @field_validator("supervisor_id")
    def validate_supervisor_id(cls, v, values):
        if v <= 0:
            raise ValueError("supervisor_id must be positive")
        if "employee_id" in values and v == values["employee_id"]:
            raise ValueError("supervisor_id cannot be same as employee_id")
        return v

    @field_validator("end_date")
    def validate_end_date(cls, v, values):
        start_date = values.get("start_date")
        if start_date and v <= start_date:
            raise ValueError("end_date must be after start_date")
        if start_date and (v - start_date).days > 30:
            raise ValueError("end_date must be within 30 days of start_date")
        return v

    @field_validator("start_date")
    def validate_start_date(cls, v):
        if v < date.today():
            raise ValueError("start_date cannot be in the past")
        if v.weekday() in (5,6):
            raise ValueError("start_date cannot be a weekend")
        return v

    @field_validator("employee_name")
    def validate_employee_name(cls, v):
        if not re.match(r'^[A-Za-z ]+$', v):
            raise ValueError("employee_name must contain only letters and spaces")
        return v

    @field_validator("mobile_number")
    def validate_mobile_number(cls, v):
        if not re.match(r'^[6-9]\d{9}$', v):
            raise ValueError("mobile must start with 6,7,8, or 9")
        return v

    @field_validator("email")
    def validate_email(cls, v):
        if not v.endswith("@ust.com"):
            raise ValueError("email must end with @ust.com")
        return v

    @field_validator("task_title")
    def validate_task_title(cls, v):
        if len(v) > 50:
            raise ValueError("task_title must not exceed 50 characters")
        return v

    @field_validator("task_description")
    def validate_task_description(cls, v):
        if len(v) > 300:
            raise ValueError("task_description must not exceed 300 characters")
        return v

    @field_validator("skills")
    def validate_skills(cls, v):
        if not v:
            raise ValueError("skills list must contain at least one skill")
        for skill in v:
            if len(skill) < 2:
                raise ValueError("each skill must be at least 2 characters")
        if len(v) != len(set(v)):
            raise ValueError("skills cannot be duplicate")
        forbidden = {"hacking","malware","phishing"}
        for skill in v:
            if skill.lower() in forbidden:
                raise ValueError(f"skills contain forbidden items: {skill}")
        return v

    @field_validator("attachments")
    def validate_attachments(cls, v):
        if not v:
            raise ValueError("attachments list cannot be empty")
        for att in v:
            if not att or not att.endswith(".pdf"):
                raise ValueError("all attachments must be PDF files and non-empty")
            match = re.search(r'_(\d+)KB\.pdf$', att)
            if match and int(match.group(1)) > 5000:
                raise ValueError("attachment size exceeds limit (5000 KB)")
        return v

    @field_validator("remarks")
    def validate_remarks(cls, v):
        if v is not None and len(v.strip()) < 5:
            raise ValueError("remarks must be at least 5 characters")
        return v

    @field_validator("employee_id")
    def unique_employee_id(cls,v):
        if v in existing_emp_ids:
            raise ValueError("employee_id must be unique")
        existing_emp_ids.add(v)
        return v

    @field_validator("emergency_contact")
    def emergency_contact(cls,v,values):
        mobile = values.get("mobile_number")
        if mobile and v == mobile:
            raise ValueError("emergency_contact cannot be same as mobile")
        return v

    @field_validator("hours_spent")
    def validate_hours_priority(cls, v, values):
        if values.get("priority") == PriorityEnum.high and v > 8:
            raise ValueError("hours_spent exceeds daily limit for high priority")
        return v

    @field_validator("completed")
    def validate_completed_feedback(cls, v, values):
        if v and not values.get("remarks"):
            raise ValueError("client_feedback required when task is completed")
        return v

    @field_validator("priority")
    def validate_band_priority(cls, v, values):
        if values.get("band") == BandEnum.B1 and v == PriorityEnum.high:
            raise ValueError("B1 band cannot have high priority tasks")
        return v

    @field_validator("cost_center")
    def validate_cost_center_department(cls, v, values):
        dept = values.get("department")
        if dept and not v.startswith(dept[:2].upper()):
            raise ValueError("cost_center must match department code")
        return v

    @field_validator("project_code")
    def validate_project_code_unique(cls, v):
        if v in active_project_codes:
            raise ValueError("project_code already in use")
        active_project_codes.add(v)
        return v


# try:
#     emp = EmployeeTask(
#         start_date=date.today(),
#         end_date=date.today() + timedelta(days=10),
#         employee_id=1,
#         employee_name="John Doe",
#         email="john.doe@ust.com",
#         mobile_number="9876543210",
#         band="B1",
#         task_id=2,
#         task_title="Build API",
#         task_description="Develop REST API for project",
#         hours_spent=5,
#         completed=False,
#         project_code="ABC123",
#         cost_center="HR-123",
#         asset_code="LAPTOP123",
#         supervisor_id=3,
#         department="IT",
#         location="Mumbai",
#         attachments=["specs.pdf"],
#         remarks="All good",
#         priority="high",
#         emergency_contact="9123456789",
#         skills=["Python", "SQL"]
#     )
#     print("Validation passed ✅")
#     print(emp)
# except Exception as e:
#     print("Validation failed ❌")
#     print(e)