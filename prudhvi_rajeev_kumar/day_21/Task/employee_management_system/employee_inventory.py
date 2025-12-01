from pydantic import BaseModel, field_validator, Field
from datetime import date, datetime
import re

class Employee(BaseModel):
    first_name: str = Field(..., max_length=50, description="should not be empty.")
    last_name: str = Field(..., max_length=50, description="should not be empty.")
    email: str
    position: str = Field(..., max_length=50, description="max length should be 50.")
    salary: float = Field(..., gt=0, description="Salary should be greater than 0.")
    hire_date: date = Field(..., description="Cannot be a future date.")

    @field_validator('first_name')
    def validate_first_name(cls, v):
        if not v:
            raise ValueError("Must not be empty")
        if not re.fullmatch(r"^[A-Za-z -]+$", v):
            raise ValueError("First name may only contain letters, spaces, or hyphens.")
        return v

    @field_validator('last_name')
    def validate_last_name(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("Must not be empty")
        if not re.fullmatch(r"^[A-Za-z -]+$", v):
            raise ValueError("Last name may only contain letters, spaces, or hyphens.")
        return v
    
    @field_validator('email')
    def validate_email_id(cls, v: str) -> str:
        if len(v) > 100:
            raise ValueError("Cannot exceed 100 characters.")
        if " " in v:
            raise ValueError("Email must not contain spaces")
        # Regex for email format
        if not re.fullmatch(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', v):
            raise ValueError("Invalid email format.")
        return v
        
    @field_validator('position')
    def validate_position(cls, v):
        v = v.strip()
        if len(v) > 50:
            raise ValueError("Position should not have more than 50 characters.")
        if not re.fullmatch(r"^[A-Za-z -]+$", v):
            raise ValueError("Position may only contain letters, spaces, or hyphens.")
        return v
    
    @field_validator('hire_date')
    def validate_hire_date(cls, v):
        if v > datetime.now().date():
            raise ValueError("Date cannot be in future")
        return v
