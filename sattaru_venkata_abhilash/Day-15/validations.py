from typing import List, Optional
from pydantic import BaseModel, Field

# Pydantic model for Employee details
class Employee(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee Id not valid")  # Employee ID must be between 1000 and 999999
    name: str = Field(..., min_length=2, description="name should be minimum of length 2")  # Employee name must have at least 2 characters
    department: Optional[str] = Field(default="General", description="Department name")  # Default department is "General"

# Pydantic model for SIM details
class Sim(BaseModel):
    number: str = Field(..., pattern=r"^\d{10}$", description="Must be exactly 10 digits")  # SIM number must be exactly 10 digits
    provider: str = Field(default="Jio", description="SIM provider name")  # Default provider is "Jio"
    activation_year: int = Field(..., ge=2000, le=2025, description="Year Must be from 2020 to 2025")  # SIM activation year must be between 2020 and 2025

# Pydantic model for Registration, which combines Employee and SIM details
class Registration(BaseModel):
    employee: Employee  # Employee details
    sim: Sim  # SIM details

# Sample data to create Employee and SIM objects
data = {
    "employee": {
        "emp_id": 12345,  # Employee ID
        "name": "Asha"  # Employee name
    },
    "sim": {
        "number": "9876543210",  # SIM number
        "activation_year": 2023  # SIM activation year
    }
}

# Creating an Employee instance using data from the dictionary
emp = Employee(**data["employee"])

# Creating a Sim instance using data from the dictionary
s = Sim(**data["sim"])

# Creating a Registration instance, which includes both Employee and Sim instances
reg = Registration(**data)

# Printing the Registration object, which combines Employee and Sim
print(reg)

# Printing the individual Employee instance
print(emp)

# Printing the individual Sim instance
print(s)

# Sample Output
# emp_id=12345 name='Asha' department='Engineering'
# number='9876543210' provider='Airtel' activation_year=2023
# employee=Employee(emp_id=12345, name='Asha', department='Engineering') sim=Sim(number='9876543210', provider='Airtel', activation_year=2023)

# Output when default values are used (department='General' and provider='Jio'):
# employee=Employee(emp_id=12345, name='Asha', department='General') sim=Sim(number='9876543210', provider='Jio', activation_year=2023)     
# emp_id=12345 name='Asha' department='General'
# number='9876543210' provider='Jio' activation_year=2023
