from pydantic import BaseModel, field_validator, ValidationError, model_validator
from datetime import datetime
from typing import Optional
import re
import csv
import os

# Define custom exceptions (kept for your use)
class ValidationErrorException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Predefined valid values
valid_departments = ['HR', 'IT', 'Admin', 'Finance']
valid_locations = ['Bangalore', 'Kolkata', 'Chennai', 'Mumbai', 'Hyderabad', 'Delhi']
valid_statuses = ['Active', 'Inactive', 'Resigned']

class Employee(BaseModel):
    emp_code: str
    full_name: str
    email: str
    phone: str
    department: str
    location: str
    join_date: str
    status: str

    # Field Validators
    @field_validator('emp_code')
    def validate_emp_code(cls, v):
        if not v.startswith('USTEMP-'):
            raise ValueError(f"Invalid emp_code: {v}")
        return v

    @field_validator('full_name')
    def validate_full_name(cls, v):
        if not re.match(r"^[A-Za-z\s]+$", v):
            raise ValueError(f"Invalid full_name: {v}")
        return v

    @field_validator('email')
    def validate_email(cls, v):
        if not v.endswith('@ust.com'):
            raise ValueError(f"Invalid email: {v}")
        return v

    @field_validator('phone')
    def validate_phone(cls, v):
        if not re.match(r"^[6-9]\d{9}$", str(v)):
            raise ValueError(f"Invalid phone: {v}")
        return v

    @field_validator('department')
    def validate_department(cls, v):
        if v not in valid_departments:
            raise ValueError(f"Invalid department: {v}")
        return v

    @field_validator('location')
    def validate_location(cls, v):
        if v not in valid_locations:
            raise ValueError(f"Invalid location: {v}")
        return v

    @field_validator('join_date')
    def validate_join_date(cls, v):
        try:
            join_date_obj = datetime.strptime(v, "%Y-%m-%d")
            if join_date_obj > datetime.today():
                raise ValueError(f"Invalid join_date: {v}")
        except ValueError:
            raise ValueError(f"Invalid date format for join_date: {v}")
        return v

    @field_validator('status')
    def validate_status(cls, v):
        if v not in valid_statuses:
            raise ValueError(f"Invalid status: {v}")
        return v

    # Optional root_validator to check all fields at once if needed
    @model_validator(mode="after")
    def check_all_fields(cls, values):
        # You can add any cross-field validation logic here if needed.
        return values
