from pydantic import BaseModel, Field
from typing import List, Optional, Dict

# Define Employee model with validation rules
class Employee(BaseModel):
    # emp_id must be between 1000 and 999999
    emp_id: int = Field(..., ge=1000, le=999999)
    # name must have at least 2 characters
    name: str = Field(..., min_length=2)
    # department defaults to "General" if not provided
    department: str = Field("General")

# Define SIM model with validation rules
class SIM(BaseModel):
    # number must be exactly 10 characters long
    number: str = Field(..., min_length=10, max_length=10)
    # provider defaults to "Jio" if not provided
    provider: str = Field("Jio")
    # activation_year must be between 2020 and 2025
    activation_year: int = Field(..., ge=2020, le=2025)

# Define Register model that combines Employee and SIM
class Register(BaseModel):
    employee: Employee
    sim: SIM

# Sample data dictionary
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

# Create Register object using nested Employee and SIM data
obj = Register(employee=data["employee"], sim=data["sim"])

# Print dictionary representation of the Register object
print(obj.__dict__)

# ---------------- SAMPLE OUTPUT ----------------
# {
#   'employee': Employee(emp_id=12345, name='Asha', department='Engineering'),
#   'sim': SIM(number='9876543210', provider='Airtel', activation_year=2023)
# }