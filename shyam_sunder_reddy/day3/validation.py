from pydantic import BaseModel, Field
from typing import Optional

# -----------------------------
# Data Models (Schemas)
# -----------------------------

class Employee(BaseModel):
    """
    Employee schema with validation rules:
    - emp_id: must be between 1000 and 999999
    - name: must be at least 2 characters long
    - department: optional, defaults to "General" if not provided
    """
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee Id not valid")
    name: str = Field(..., min_length=2, description="name should be minimum of length 2")
    department: Optional[str] = Field(default="General", description="Department name")


class Sim(BaseModel):
    """
    SIM schema with validation rules:
    - number: must be exactly 10 digits
    - provider: optional, defaults to "Jio" if not provided
    - activation_year: must be between 2020 and 2025
    """
    number: str = Field(..., pattern=r"^\d{10}$", description="Must be exactly 10 digits")
    provider: Optional[str] = Field(default="Jio", description="Provider name")
    activation_year: int = Field(..., ge=2020, le=2025, description="Year Must be from 2020 to 2025")


class Registration(BaseModel):
    """
    Registration schema combining Employee and Sim.
    Demonstrates nested Pydantic models.
    """
    employee: Employee
    sim: Sim


# -----------------------------
# Example Data
# -----------------------------

# Case 1: All fields provided
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

# Case 2: Missing optional fields (uncomment to test)
# data = {
#     "employee": {
#         "emp_id": 12345,
#         "name": "Asha"
#     },
#     "sim": {
#         "number": "9876543210",
#         "activation_year": 2023
#     }
# }

# -----------------------------
# Object Creation + Validation
# -----------------------------

emp = Employee(**data["employee"])   # Validates Employee fields
s = Sim(**data["sim"])               # Validates Sim fields
reg = Registration(**data)           # Validates nested Registration

# -----------------------------
# Output Demonstration
# -----------------------------

print(reg)   # Full Registration object
print(emp)   # Employee object
print(s)     # Sim object

# -----------------------------
# Sample Outputs
# -----------------------------

# Case 1: All fields provided
# Registration(employee=Employee(emp_id=12345, name='Asha', department='Engineering'),
#              sim=Sim(number='9876543210', provider='Airtel', activation_year=2023))
# emp_id=12345 name='Asha' department='Engineering'
# number='9876543210' provider='Airtel' activation_year=2023

# Case 2: Missing optional fields
# Registration(employee=Employee(emp_id=12345, name='Asha', department='General'),
#              sim=Sim(number='9876543210', provider='Jio', activation_year=2023))
# emp_id=12345 name='Asha' department='General'
# number='9876543210' provider='Jio' activation_year=2023
