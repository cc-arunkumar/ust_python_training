from datetime import date
from pydantic import BaseModel,Field,field_validator
from fastapi import HTTPException
from typing import Optional

class Employee(BaseModel):
    first_name:str=Field(...,pattern=r"^[A-Za-z- ]+$",max_length=50,description="Employee's first name (alphabets only, max 50 characters)")
    last_name:str=Field(...,pattern=r"^[A-Za-z- ]+$",max_length=50,description="Employee's last name (alphabets only, max 50 characters)")
    email:str=Field(...,pattern=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",max_length=100,description="Employee's email address (must be valid format, unique, no spaces)")
    position:Optional[str]=Field(None,pattern=r"^[A-Za-z0-9- ]+$",max_length=50,description="")
    salary: Optional[float] = Field(None, gt=0,description="Must be positive")
    hire_date: date = Field(...)
    
    @field_validator("first_name")
    def validate_first_name(cls,v):
        if not v:
            raise ValueError("First name cannot be empty")
        return v

    @field_validator("hire_date")
    def validate_hire_date(cls, v):
        if v > date.today():
            raise ValueError("Hire date cannot be in the future")
        return v
    

 


