from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re
from datetime import datetime, date

class Employee(BaseModel):
    employee_id: str = Field(..., max_length=20)
    employee_name: str = Field(..., max_length=100)
    training_title: str = Field(..., max_length=200)
    training_description: str
    requested_date: str
    status: str
    manager_id: str = Field(..., max_length=20)
    last_updated: Optional[str] = None

    @field_validator('employee_id', 'manager_id')
    def validate_id(cls, v):
        if not re.match(r'^UST\d+$', v):
            raise ValueError("Must follow UST format (e.g., UST12345)")
        return v

    @field_validator('employee_name')
    def validate_name(cls, v):
        if not v.strip() or any(c.isdigit() for c in v):
            raise ValueError("Name cannot be empty or contain numbers")
        return v

    @field_validator('training_title')
    def validate_training_title(cls, v):
        if len(v) < 5:
            raise ValueError("Training title must be at least 5 characters")
        return v

    @field_validator('training_description')
    def validate_training_description(cls, v):
        if len(v) < 10:
            raise ValueError("Training description must be at least 10 characters")
        return v

    @field_validator('requested_date')
    def validate_requested_date(cls, v):
        try:
            dt = datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("requested_date must be YYYY-MM-DD")
        if dt > date.today():
            raise ValueError("requested_date cannot be in the future")
        return v

    @field_validator('status')
    def validate_status(cls, v):
        allowed = ["PENDING", "APPROVED", "REJECTED"]
        if v not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return v
