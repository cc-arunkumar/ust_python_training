from pydantic import BaseModel, Field, field_validator
from typing import Optional,List
from datetime import date
from exceptions.custom_exception import ValidationExeption
import re

# Employee model to validate incoming employee data using Pydantic
class Employee(BaseModel):
    employee_id : Optional[int]=None   # Optional ID, usually auto-incremented in DB
    first_name : str = Field(...,max_length=50)  # Required, max 50 chars
    last_name : str = Field(...,max_length=50)   # Required, max 50 chars
    email : str = Field(...,max_length=100)      # Required, max 100 chars
    position : Optional[str] = Field(max_length=50)  # Optional, max 50 chars
    salary : Optional[float] = Field(gt=0)       # Optional, must be > 0
    hire_date : date                              # Required, date only

    # Validate first_name
    @field_validator("first_name")
    def validate_first_name(cls,v):
        if not v.strip():  # Check empty or spaces only
            raise ValidationExeption("first_name must not be empty")
        if not re.match(r"^[A-Za-z\s-]+$",v):  # Only alphabets, spaces, hyphens
            raise ValidationExeption("first_name should contain only alphabets, spaces, or hyphens")
        return v
    
    # Validate last_name
    @field_validator("last_name")
    def validate_last_name(cls,v):
        if not v.strip():  # Check empty values
            raise ValidationExeption("last_name must not be empty")
        if not re.match(r"^[A-Za-z\s-]+$",v):  # Only alphabets, spaces, hyphens
            raise ValidationExeption("last_name should contain only alphabets, spaces, or hyphens")
        return v
    
    # Validate email format
    @field_validator("email")
    def validate_email(cls,v):
        # Standard email regex pattern
        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",v):
            raise ValidationExeption("Incorrect email")
        return v
    
    # Validate position (optional)
    @field_validator("position")
    def validate_position(cls,v):
        # Only letters, digits, spaces and hyphens allowed, max length already controlled by Field
        if not re.match(r"^[A-Za-z0-9\s-]{1,50}$",v):
            raise ValidationExeption("Invalid Position")
        return v
    
    # Validate salary (optional)
    @field_validator("salary")
    def val_sal(cls,v):
        if v<0:  # Salary must be positive
            raise ValidationExeption("Must be positive number")
        return v
    
    # Validate hire date (cannot be future)
    @field_validator("hire_date")
    def validate_join_date(cls, v):
        if v > date.today():  # Future date not allowed
            raise ValidationExeption("Hire date cannot be a future date")
        return v
