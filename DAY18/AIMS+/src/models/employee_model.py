from pydantic import BaseModel, Field, EmailStr, field_validator
from datetime import date
from typing import Optional

VALID_DEPARTMENTS = ["HR", "IT", "Admin", "Finance"]
VALID_LOCATIONS = ["TVM", "Bangalore", "Chennai", "Hyderabad"]
VALID_STATUSES = ["Active", "Inactive", "Resigned"]

class EmployeeCreate(BaseModel):
    emp_code: str = Field(..., pattern=r"^USTEMP-")
    full_name: str = Field(..., max_length=100)
    email: EmailStr
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$")
    department: str
    location: str
    join_date: date
    status: str = "Active"

    @field_validator('emp_code')
    def check_code(cls, v):
        if not v.startswith("USTEMP-"):
            raise ValueError("emp_code must start with USTEMP-")
        return v

    @field_validator('full_name')
    def name_only_alpha(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("full_name must contain only letters and spaces")
        return v.strip()

    @field_validator('email')
    def email_ust_only(cls, v):
        if not v.lower().endswith("@ust.com"):
            raise ValueError("email must end with @ust.com")
        return v.lower()

    @field_validator('department')
    def valid_dept(cls, v):
        if v not in VALID_DEPARTMENTS:
            raise ValueError(f"department must be one of {VALID_DEPARTMENTS}")
        return v

    @field_validator('location')
    def valid_loc(cls, v):
        if v not in VALID_LOCATIONS:
            raise ValueError(f"location must be one of {VALID_LOCATIONS}")
        return v

    @field_validator('join_date')
    def no_future_join(cls, v):
        if v > date.today():
            raise ValueError("join_date cannot be future date")
        return v

    @field_validator('status')
    def valid_status(cls, v):
        if v not in VALID_STATUSES:
            raise ValueError(f"status must be one of {VALID_STATUSES}")
        return v

class EmployeeUpdate(EmployeeCreate):
    pass