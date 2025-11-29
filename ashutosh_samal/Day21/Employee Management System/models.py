from pydantic import BaseModel, Field, field_validator
from typing import Optional, ClassVar, List
from datetime import date
import re


class Employee(BaseModel):
    # Fields representing employee attributes
    employee_id : int 
    first_name : str = Field(...,max_length=50)
    last_name : str = Field(...,max_length=50)
    email : str = Field(...,max_length=100)
    position : Optional[str] = Field(max_length=50)
    salary : Optional[float] = Field(gt=0)
    hire_date : date
    
    # Validator for first name: Must only contain alphabets, spaces or hyphens
    @field_validator("first_name")
    def validate_first_name(cls,v):
        if not v.strip():
            raise ValueError("first_name must not be empty")
        if not re.match(r"^[A-Za-z\s-]+$",v):
            raise ValueError("first_name should contain only alphabets, spaces, or hyphens")
        return v
    
    
    # Validator for last name: Must only contain alphabets, spaces or hyphen
    @field_validator("last_name")
    def validate_last_name(cls,v):
        if not v.strip():
            raise ValueError("last_name must not be empty")
        if not re.match(r"^[A-Za-z\s-]+$",v):
            raise ValueError("last_name should contain only alphabets, spaces, or hyphens")
        return v
    
    # Validator for email        
    @field_validator("email")
    def validate_email(cls,v):
        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",v):
            raise ValueError("Incorrect email")
        return v
    
    # Validator for position
    @field_validator("position")
    def validate_position(cls,v):
        if not re.match(r"^[A-Za-z0-9\s-]{1,50}$",v):
            raise ValueError("Invalid Position")
        return v
    
    # Validator for salary: Must be positive value
    @field_validator("salary")
    def val_sal(cls,v):
        if v<0:
            raise ValueError("Must be positive number")
        return v
    
    
    # Validator for join date: Must not be a future date
    @field_validator("hire_date")
    def validate_join_date(cls, v):
        if v > date.today():
            raise ValueError("Hire date cannot be a future date")
        return v
    
    