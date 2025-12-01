from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime
from typing import ClassVar, List
import re

class EmployeeTraining(BaseModel):
    # Allowed constant list for validation of status
    allowed_status: ClassVar[List[str]] = ["PENDING", "APPROVED", "REJECTED"]

    # Training request fields with validation rules
    employee_id: str = Field(..., max_length=20)
    employee_name: str = Field(..., max_length=100)
    training_title: str = Field(..., min_length=5, max_length=200)
    training_description: str = Field(..., min_length=10)
    requested_date: date = Field(...)
    status: str = Field(...)
    manager_id: str = Field(..., max_length=20)
    last_updated: datetime

    # Validate Employee ID (Ex: UST12345)
    @field_validator("employee_id")
    def validate_employee_id(cls, v):
        if not re.match(r"^[UST\d]+$", v):
            raise ValueError("Invalid Employee ID")
        return v

    # Validate Employee Name (alphabets + spaces only)
    @field_validator("employee_name")
    def validate_employee_name(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be empty")
        if not re.match(r"^[A-Za-z\s]+$", v):
            raise ValueError("Name should only contain alphabets and spaces")
        return v

    # Validate Requested Date should not be a future date
    @field_validator("requested_date")
    def validate_requested_date(cls, v):
        if v > date.today():
            raise ValueError("Date cannot be a future date")
        return v

    # Validate Status must match allowed values
    @field_validator("status")
    def validate_status(cls, v):
        if v not in cls.allowed_status:
            raise ValueError(f"Status must be one of {cls.allowed_status}")
        return v

    # Validate Manager ID format (same as employee_id)
    @field_validator("manager_id")
    def validate_manager_id(cls, v):
        if not re.match(r"^[UST\d]+$", v):
            raise ValueError("Invalid Manager ID")
        return v
    