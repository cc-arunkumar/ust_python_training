from enum import Enum
from pydantic import BaseModel, field_validator, Field
from datetime import date, datetime
import re

class Status(str, Enum):
    pending = "PENDING"
    approved = "APPROVED"
    rejected = "REJECTED"

class TrainingRequest(BaseModel):
    employee_id : str = Field(...,description="Must follow the proper format.")
    employee_name : str = Field(...,description="Name of the employee.")
    training_title : str = Field(...,min_length=5, description="Title of the training.")
    training_description : str = Field(...,min_length=10, description="Reason and details.")
    request_date : date = Field(..., description="Request submission date.")
    status : Status
    manager_id : str = Field(...,description="Approver or manager id.")
    last_updated: datetime | None = None
    
    
    @field_validator("employee_id")
    def validate_employee_id(cls, v):
        if not re.fullmatch(r"^UST\d+$", v):
            raise ValueError("Not in proper format.")
        return v
    
    @field_validator("employee_name")
    def validate_employee_name(cls, v):
        if not v:
            raise ValueError("Employee name cannot be empty.")
        if not re.fullmatch(r"^[A-Za-z ]+$", v):
            raise ValueError("Cannot contain other than letters.")
        return v
    
    @field_validator("request_date")
    def validate_requested_date(cls, v):
        if v > date.today():
            raise ValueError("Date cannot be in future.")
        return v
    
    @field_validator("manager_id")
    def validate_manager_id(cls, v):
        if not re.fullmatch(r"^UST\d+$", v):
            raise ValueError("Not in proper format.")
        return v
    
    @field_validator("status")
    def validate_status(cls, v):
        allowed = {"PENDING", "APPROVED", "REJECTED"}
        if v not in allowed:
            raise ValueError("Status should be in these three only.")
        return v
    