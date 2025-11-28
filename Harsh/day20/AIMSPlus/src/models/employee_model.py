from pydantic import BaseModel, field_validator, model_validator
from datetime import date, datetime
import re

class EmployeeDirectory(BaseModel):
    emp_code: str          # employee code, must start with USTEMP-
    full_name: str         # employee full name, alphabets and spaces only
    email: str             # employee email, must be valid format
    phone: str             # phone number, must be 10 digits
    department: str        # department, must be one of allowed values
    location: str          # location, must be one of allowed cities
    join_date: date        # join date, cannot be in the future
    status: str            # status, must be Active/Inactive/Resigned

    @field_validator("emp_code")
    def emp_code_valid(cls, v):
        # emp_code must start with USTEMP- followed by digits
        if not re.match(r"^USTEMP[A-Za-z0-9-]+$", v):
            raise ValueError("emp_code must start with USTEMP- followed by digits")
        return v

    @field_validator("full_name")
    def full_name_valid(cls, v):
        # full_name must contain only alphabets and spaces
        if not re.match(r"^[A-Za-z ]+$", v):
            raise ValueError("full_name must contain only alphabets and spaces")
        return v

    @field_validator("email")
    def email_valid(cls, v):
        # email must follow proper format
        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", v):
            raise ValueError("Invalid email format")
        return v

    @field_validator("phone")
    def phone_valid(cls, v):
        # phone must be exactly 10 digits
        if not re.match(r"^[6-9]\d{9}$", v):
            raise ValueError("Phone must be exactly 10 digits")
        return v

    @field_validator("department")
    def department_valid(cls, v):
        # department must be one of the allowed set
        valid = {"IT", "HR", "Finance", "Admin", "Sales", "Support"}
        if v not in valid:
            raise ValueError("Invalid department")
        return v

    @field_validator("location")
    def location_valid(cls, v):
        # location must be one of allowed cities
        valid = {"Trivandrum", "Bangalore", "Chennai", "Hyderabad"}
        if v not in valid:
            raise ValueError("Invalid location")
        return v

    @field_validator("status")
    def status_valid(cls, v):
        # status must be Active, Inactive, or Resigned
        valid = {"Active", "Inactive", "Resigned"}
        if v not in valid:
            raise ValueError("Invalid status")
        return v

    @field_validator("join_date")
    def join_date_not_future(cls, v: date):
        # join_date cannot be in the future
        if v > date.today():
            raise ValueError("join_date cannot be in the future")
        return v
