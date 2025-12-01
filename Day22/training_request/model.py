from pydantic import BaseModel, Field, EmailStr, field_validator
from datetime import date
import re

class TrainingRequestModel(BaseModel):
    employee_id: str = Field(..., max_length=20)
    employee_name: str = Field(..., max_length=100)
    training_title: str = Field(..., max_length=200)
    training_description: str = Field(..., max_length=1000)
    requested_date: date
    status: str = Field(..., max_length=20)
    manager_id: str = Field(..., max_length=20)
    
    @field_validator('employee_id')
    def validate_employee_id(cls, v):
        if not re.match(r"^UST\d+$", v):
            raise ValueError("Employee ID must start with 'UST' followed by digits")
        return v
    
    @field_validator('employee_name')
    def validate_employee_name(cls, v):
        if not re.match('^[A-Za-z\\s-]+$', v):
            raise ValueError("Employee name can only contain letters, spaces, and hyphens")
        return v.strip()
    
    @field_validator('training_title')
    def validate_training_title(cls, v):
        if len(v) < 5:
            raise ValueError("Training title must be at least 5 characters")
        return v.strip()
    
    @field_validator('training_description')
    def validate_training_description(cls, v):
        if len(v) < 10:
            raise ValueError("Training description must be at least 10 characters")
        return v.strip()
    
    @field_validator('requested_date')
    def validate_requested_date(cls, v):
        if v > date.today():
            raise ValueError("Requested date cannot be in the future")
        return v
    
    @field_validator('status')
    def validate_status(cls, v):
        allowed_status = ["PENDING", "APPROVED", "REJECTED"]
        if v not in allowed_status:
            raise ValueError("Status must be one of: PENDING, APPROVED, REJECTED")
        return v
    
    @field_validator('manager_id')
    def validate_manager_id(cls, v):
        if not re.match(r"^UST\d+$", v):
            raise ValueError("Manager ID must follow the same format as Employee ID ('UST' followed by digits)")
        return v.strip()
