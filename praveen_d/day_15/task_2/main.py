from pydantic import BaseModel, Field, validator
from typing import Optional

# Employee Model
class Employee(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)
    name: str = Field(..., min_length=2)
    department: str = Field(default="General")

    @validator("department", pre=True, always=True)
    def set_default_department(cls, v):
        return v or "General"

# SIM Model
class SIM(BaseModel):
    number: str = Field(..., regex=r"^\d{10}$")
    provider: str = Field(default="Jio")
    activation_year: int = Field(..., ge=2020, le=2025)

    @validator("provider", pre=True, always=True)
    def set_default_provider(cls, v):
        return v or "Jio"

# Registration Model
class Registration(BaseModel):
    employee: Employee
    sim: SIM

# Example of valid input data
valid_data = {
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

# Example of default field assignment (department missing, provider missing)
default_data = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha"
    },
    "sim": {
        "number": "9876543210",
        "activation_year": 2023
    }
}

# Function to test valid data
def test_registration(data):
    try:
        registration = Registration(**data)
        print("Registration created successfully:", registration)
    except Exception as e:
        print("Validation failed:", e)

# Test the valid data
test_registration(valid_data)

# Test the default assignment case
test_registration(default_data)

# Validation error test cases:
error_cases = [
    {"emp_id": 999, "name": "Asha", "sim": {"number": "9876543210", "activation_year": 2023}},  # emp_id violation
    {"emp_id": 12345, "name": "A", "sim": {"number": "9876543210", "activation_year": 2023}},  # name violation
    {"emp_id": 12345, "name": "Asha", "sim": {"number": "12345", "activation_year": 2023}},  # number violation
    {"emp_id": 12345, "name": "Asha", "sim": {"number": "9876543210", "activation_year": 2019}},  # activation_year violation (too low)
    {"emp_id": 12345, "name": "Asha", "sim": {"number": "9876543210", "activation_year": 2030}},  # activation_year violation (too high)
]

# Testing validation errors
for case in error_cases:
    print("\nTesting with invalid data:", case)
    test_registration(case)
