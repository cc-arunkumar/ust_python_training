import re
from typing import Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date

email_Set = set()

class Employee(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50, pattern=r"^[A-Za-z- ]+$")
    last_name: str = Field(..., min_length=1, max_length=50, pattern=r"^[A-Za-z- ]+$")
    email: str = Field(..., max_length=100)
    position: Optional[str] = Field(None, max_length=50, pattern=r"^[A-Za-z0-9- ]+$")
    salary: float = Field(gt=0)
    hire_date: date = Field(...)

    @field_validator("email")
    def validate_email(cls, v):
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com$"
        if not re.match(pattern, v):
            raise ValueError("Invalid email format")
        if v in email_Set:
            raise ValueError(f"Duplicate email: {v}")
        email_Set.add(v)
        return v

    @field_validator("hire_date")
    def validate_hire_date(cls, v):
        if v > date.today():
            raise ValueError("Hire date cannot be a future date")
        return v
