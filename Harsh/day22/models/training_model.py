from datetime import date
from enum import Enum
from pydantic import BaseModel, Field, field_validator
from typing import Optional


class StatusEnum(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class TrainingRequest(BaseModel):
    employee_id: str = Field(..., pattern=r"^UST[0-9]+$", max_length=20)
    employee_name: str = Field(..., pattern=r"^[A-Za-z ]+$", max_length=100)
    training_title: str = Field(..., min_length=5, max_length=200)
    training_description: str = Field(..., min_length=10)
    requested_date: date
    status: StatusEnum  
    manager_id: str = Field(..., pattern=r"^UST[0-9]+$", max_length=20)
    last_updated: Optional[date] = None

    @field_validator("requested_date")
    def validate_requested_date(cls, v):
        if v > date.today():
            raise ValueError("requested_date cannot be a future date")
        return v

    
    @field_validator("status")
    def validate_status(cls, v):
        allowed = {"PENDING", "APPROVED", "REJECTED"}
        if v not in allowed:
            raise ValueError("status must be one of PENDING, APPROVED, REJECTED")
        return v

    @field_validator("employee_name")
    def validate_employee_name(cls, v):
        if not v:
            raise ValueError("employee_name cannot be empty")
        return v