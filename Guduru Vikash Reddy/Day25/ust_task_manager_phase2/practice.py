# from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
# from enum import Enum
# from typing import List, Optional
# from datetime import date
# import re
 
 
# class BandEnum(str, Enum):
#     B1 = "B1"
#     B2 = "B2"
#     B3 = "B3"
#     M1 = "M1"
 
 
# class PriorityEnum(str, Enum):
#     low = "low"
#     medium = "medium"
#     high = "high"
 
 
# class EmployeeTask(BaseModel):
 
#     # ---------------- EMPLOYEE INFO ----------------
#     employee_id: int = Field(..., gt=0, description="employee_id must be positive")
#     employee_name: str = Field(..., min_length=3, description="employee_name must be at least 3 characters")
#     email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@ust\.com$', description="email must end with @ust.com")
#     mobile: str = Field(..., pattern=r"^[6-9]\d{9}$", description="mobile must start with 6,7,8, or 9")
#     band: BandEnum
 
#     # ---------------- TASK INFO ----------------
#     task_id: int = Field(..., gt=0, description="task_id must be positive")
#     task_title: str = Field(..., max_length=50, description="task_title must not exceed 50 characters")
#     task_description: str = Field(..., max_length=300, description="task_description must not exceed 300 characters")
#     priority: PriorityEnum
#     hours_spent: int = Field(..., ge=1, le=12, description="hours_spent must be between 1 and 12")
#     completed: bool = False
 
#     # ---------------- PROJECT INFO ----------------
#     project_code: str = Field(...,pattern=r"^[A-Z0-9]{3,8}$",description="project_code must be 3–8 uppercase letters/numbers")
#     cost_center: str = Field(...,pattern=r"^[A-Z]{2}-\d{3}$",description="cost_center must be in format XX-123")
#     asset_code: str = Field(...,pattern=r"^[A-Z]{2,}[0-9]{2,}$",description="asset_code must be 5-10 characters: uppercase letters + digits")
#     supervisor_id: int = Field(...,gt=0,description="supervisor_id must be positive and not equal to employee_id")
#     department: str = Field(...,pattern=r"^[A-Za-z]{3,}$",description="department must contain only letters (min 3 characters)")
#     location: str = Field(...,pattern=r"^[A-Za-z ]+$",description="location must contain only letters")
 
#     # ---------------- DATES ----------------
#     start_date: date
#     end_date: date
 
#     # ---------------- EXTRA ----------------
#     skills: List[str]
#     attachments: List[str]
#     remarks: Optional[str] = None
 
# @field_validator("employee_name")
# def validate_employee_name(class_, value):
#     if not re.fullmatch(r"[A-Za-z ]+", value):
#         raise ValueError("employee_name must contain only letters and spaces")
#     return value
 
# @field_validator("skills")
# def validate_skills(class_, value):
#     if not value:
#         raise ValueError("skills list must contain at least one skill")
#     if len(set(value)) != len(value):
#         raise ValueError("skills cannot contain duplicates")
#     for skill in value:
#         if len(skill) < 2:
#             raise ValueError("each skill must be at least 2 characters")
#     return value
 
# @field_validator("attachments")
# def validate_attachments(class_, value):
#     for file in value:
#         if not file or not file.endswith(".pdf"):
#             raise ValueError("all attachments must be PDF files and non-empty")
#     return value
 
# @field_validator("remarks")
# def validate_remarks(class_, value):
#     if value and len(value.strip()) < 5:
#         raise ValueError("remarks must be at least 5 characters")
#     return value
 
 