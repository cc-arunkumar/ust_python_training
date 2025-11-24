#Task Ust Telecom Device Registration
from fastapi import FastAPI
from pydantic import BaseModel, Field
import re

# Employee model with validation rules
class Employee(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)   # Employee ID must be between 1000 and 999999
    name: str = Field(..., min_length=2)           # Name must have at least 2 characters
    department: str = "General"                    # Default department is "General"

# Example employee instance
e = Employee(emp_id=12345, name="Asha", department="Engineering")

# Sim model with validation rules
class Sim(BaseModel):
    number: str = Field(..., pattern=r"^\d{10}$")  # Must be a 10-digit number
    provider: str = "Jio"                          # Default provider is "Jio"
    activation_year: int = Field(..., ge=2020, le=2025)  # Year must be between 2020 and 2025

# Registration model combining Employee and Sim
class Registration(BaseModel):
    employee: Employee = Field(...)
    sim: Sim = Field(...)

# Example data for registration
data = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha",
        "department": "Engineering"
    },
    "sim": {
        "number": "9876543210",
        "provider": "Airtel",
        "activation_year": 2023
    }
}

# Create Registration instance from data
registration = Registration(**data)
print(registration)

#Sample Execution
# employee=Employee(emp_id=12345, name='Asha', department='Engineering') sim=Sim(number='9876543210', provider='Airtel', activation_year=2023)
