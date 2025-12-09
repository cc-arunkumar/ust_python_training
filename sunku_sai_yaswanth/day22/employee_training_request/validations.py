from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
from enum import Enum

class EmployeeValidations(BaseModel):

    employee_id: str = Field(..., pattern=r"^UST\d+$", description="The employee id should start with UST")
    
    employee_name: str = Field(..., description="The employee full name")

    # Validator for employee_name
    @field_validator("employee_name")
    def employee_name(cls, value):
        if not value.strip():
            raise ValueError("Employee name cannot be empty")
        if any(char.isdigit() for char in value):
            raise ValueError("Employee name cannot contain numbers")
        return value

    training_title: str = Field(..., min_length=5, description="Length of the title cannot be less than 5 characters")
    training_description: str = Field(..., min_length=10, description="Minimum 10 characters required for description")

    # Declare requested_date properly and validate it
    requested_date: date = Field(..., description="Date of request (cannot be in the future)")
    
    @field_validator("requested_date")
    def requested_date(cls, value):
        if value > date.today():
            raise ValueError("Requested date cannot be in the future")
        return value

    class Status(str, Enum):
        PENDING = "Pending"
        APPROVED = "Approved"
        SELECTED = "Selected"

    status: Status
    manager_id: str = Field(..., pattern=r"^UST\d+$", description="The manager id should start with UST")

