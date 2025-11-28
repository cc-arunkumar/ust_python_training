from pydantic import BaseModel, field_validator, model_validator
from datetime import date, datetime
import re

class EmployeeDirectory(BaseModel):
    emp_code: str
    full_name: str
    email: str
    phone: str
    department: str
    location: str
    join_date: date
    status: str

    @field_validator("emp_code")
    def emp_code_valid(cls, v):
        if not re.match(r"^USTEMP-\d+$", v):
            raise ValueError("emp_code must start with USTEMP- followed by digits")
        return v

    @field_validator("full_name")
    def full_name_valid(cls, v):
        if not re.match(r"^[A-Za-z ]+$", v):
            raise ValueError("full_name must contain only alphabets and spaces")
        return v

    @field_validator("email")
    def email_valid(cls, v):
        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", v):
            raise ValueError("Invalid email format")
        return v

    @field_validator("phone")
    def phone_valid(cls, v):
        if not re.match(r"^\d{10}$", v):
            raise ValueError("Phone must be exactly 10 digits")
        return v

    @field_validator("department")
    def department_valid(cls, v):
        valid = {"IT", "HR", "Finance", "Admin", "Sales", "Support"}
        if v not in valid:
            raise ValueError("Invalid department")
        return v

    @field_validator("location")
    def location_valid(cls, v):
        valid = {"Trivandrum", "Bangalore", "Chennai", "Hyderabad"}
        if v not in valid:
            raise ValueError("Invalid location")
        return v

    @field_validator("status")
    def status_valid(cls, v):
        valid = {"Active", "Inactive", "Resigned"}
        if v not in valid:
            raise ValueError("Invalid status")
        return v

    @field_validator("join_date")
    def join_date_not_future(cls, v: date):
        if v > date.today():
            raise ValueError("join_date cannot be in the future")
        return v

