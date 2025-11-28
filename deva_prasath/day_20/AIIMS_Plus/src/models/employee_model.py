from pydantic import BaseModel, Field, field_validator  # Import Pydantic for data validation
from datetime import date  # Import date class to handle date fields
from typing import ClassVar, List  # Import typing components for type hinting
import re  # Import regex for pattern matching
import csv  # Import csv module for reading and writing CSV files
from ..exceptions.custom_exceptions import ValidationErrorException



# EmployeeCreate model to validate employee data
class EmployeeCreate(BaseModel):
    # Class variables to define allowed values for departments, locations, and status
    allowed_depts: ClassVar[List[str]] = ["HR", "IT", "Admin", "Finance"]
    allowed_locations: ClassVar[List[str]] = ["Hyderabad", "Bangalore", "Chennai", "TVM"]
    allowed_status: ClassVar[List[str]] = ["Active", "Inactive", "Resigned"]

    # Employee attributes to validate
    emp_code: str
    full_name: str
    email: str
    phone: str
    department: str
    location: str
    join_date: date
    status: str
    @field_validator("emp_code")
    def validate_emp(cls, v):
        if not v.startswith("USTEMP-"):  # emp_code must start with 'USTEMP-'
            raise ValidationErrorException("emp_code must start with 'USTEMP-'")
        return v

    @field_validator("full_name")
    def validate_full_name(cls, v):
        if not v.replace(" ", "").isalpha():  # full_name must contain only alphabets and spaces
            raise ValidationErrorException("full_name must contain only alphabets and spaces")
        return v

    @field_validator("email")
    def validate_email(cls, v):
        if not v.endswith("@ust.com"):  # email must end with '@ust.com'
            raise ValidationErrorException("email must end with '@ust.com'")
        return v

    @field_validator("phone")
    def validate_phone(cls, v):
        digits = v.strip()
        if not digits.isdigit() or len(digits) != 10:  # phone must be a valid 10-digit number
            raise ValidationErrorException("phone must be a valid 10-digit Indian mobile number")
        if digits[0] not in "6789":  # phone must start with 6, 7, 8, or 9
            raise ValidationErrorException("phone must start with 6, 7, 8, or 9")
        return digits

    @field_validator("department")
    def validate_dept(cls, v):
        if v not in cls.allowed_depts:  # department must be one of the allowed values
            raise ValidationErrorException(f"department must be one of: {cls.allowed_depts}")
        return v

    @field_validator("location")
    def validate_location(cls, v):
        if v not in cls.allowed_locations:  # location must be one of the allowed values
            raise ValidationErrorException(f"location must be one of: {cls.allowed_locations}")
        return v

    @field_validator("join_date")
    def validate_join_date(cls, v):
        if v > date.today():  # join_date cannot be in the future
            raise ValidationErrorException("join_date cannot be a future date")
        return v

    @field_validator("status")
    def validate_status(cls, v):
        if v not in cls.allowed_status:  # status must be one of the allowed values
            raise ValidationErrorException(f"status must be one of: {cls.allowed_status}")
        return v
