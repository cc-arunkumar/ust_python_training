from pydantic import BaseModel, Field, EmailStr, model_validator
from datetime import date
from typing import Literal

class StatusValidator(BaseModel):  # Validate allowed employee status values
    status: Literal['Active', 'Inactive', 'Resigned']

class EmployeeDirectory(BaseModel):  # Employee directory schema with validation rules
    emp_code: str = Field(..., pattern=r"^USTEMP[A-Za-z0-9-]+$")  # Employee code must start with USTEMP
    full_name: str = Field(..., pattern=r"^[A-Za-z ]+$")  # Full name must contain only letters and spaces
    email: EmailStr  # Valid email format
    phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")  # Phone must be a 10-digit Indian mobile number
    department: Literal['HR', 'IT', 'Admin', 'Finance', 'Support']  # Restrict department values
    location: Literal['Trivandrum', 'Bangalore', 'Chennai', 'Hyderabad', 'Mumbai', 'Delhi', 'Pune']  # Restrict location values
    join_date: date  # Employee joining date
    status: Literal['Active', 'Inactive', 'Resigned']  # Restrict employee status values

    @model_validator(mode="after")
    def validate(self):  # Ensure email domain and valid join_date
        if not self.email.endswith("@ust.com"):
            raise ValueError("Email must belong to @ust.com domain")
        if self.join_date > date.today():
            raise ValueError("join_date cannot be in the future")
        return self