from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import ClassVar, List
import re
import csv



class EmployeeCreate(BaseModel):
    # Lists of allowed values for departments, locations, and status
    allowed_depts: ClassVar[List[str]] = ["HR", "IT", "Admin", "Finance"]
    allowed_locations: ClassVar[List[str]] = ["Hyderabad", "Bangalore", "Chennai", "Trivandrum"]
    allowed_status: ClassVar[List[str]] = ["Active", "Inactive", "Resigned"]
    
    # Fields representing employee attributes
    emp_code: str
    full_name: str
    email: str
    phone: str
    department: str
    location: str
    join_date: date
    status: str

    # Validator for employee code: Must start with 'USTEMP-'
    @field_validator("emp_code")
    def validate_employee_code(cls, v):
        if not v.startswith("USTEMP-"):
            raise ValueError("emp_code must start with 'USTEMP-'")
        return v

    # Validator for full name: Must only contain alphabets and spaces
    @field_validator("full_name")
    def validate_full_name(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("full_name must contain only alphabets and spaces")
        return v

    # Validator for email: Must end with '@ust.com'
    @field_validator("email")
    def validate_email(cls, v):
        if not v.endswith("@ust.com"):
            raise ValueError("email must end with '@ust.com'")
        return v

    # Validator for phone: Must be a valid 10-digit Indian mobile number
    @field_validator("phone")
    def validate_phone_number(cls, v):
        digits = v.strip()
        if not digits.isdigit() or len(digits) != 10:
            raise ValueError("phone must be a valid 10-digit Indian mobile number")
        if digits[0] not in "6789":
            raise ValueError("phone must start with 6, 7, 8, or 9")
        return digits

    # Validator for department: Must be one of the allowed departments
    @field_validator("department")
    def validate_department(cls, v):
        if v not in cls.allowed_depts:
            raise ValueError(f"department must be one of: {cls.allowed_depts}")
        return v

    # Validator for location: Must be one of the allowed locations
    @field_validator("location")
    def validate_location(cls, v):
        if v not in cls.allowed_locations:
            raise ValueError(f"location must be one of: {cls.allowed_locations}")
        return v

    # Validator for join date: Must not be a future date
    @field_validator("join_date")
    def validate_join_date(cls, v):
        if v > date.today():
            raise ValueError("join_date cannot be a future date")
        return v

    # Validator for status: Must be one of the allowed statuses (Active, Inactive, Resigned)
    @field_validator("status")
    def validate_status(cls, v):
        if v not in cls.allowed_status:
            raise ValueError(f"status must be one of: {cls.allowed_status}")
        return v

