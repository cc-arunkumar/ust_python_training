from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import re

# Employee class defines the basic details of an employee.
# Used to validate and parse employee-related data.
class Employee(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee ID. Must be a unique integer between 1000 and 999999.")
    name: str = Field(..., min_length=2, description="Employee's full name. Minimum length should be 2 characters.")
    department: str = Field("General", max_length=100, description="Department where the employee works. Default is 'General'.")

# Sim_model class defines the structure for the employee's SIM card details.
# This includes the SIM number, provider, and activation year.
class Sim_model(BaseModel):
    number: str = Field(..., pattern=r"^\d{10}$", description="SIM card number. Must be exactly 10 digits.")
    provider: str = "Jio"  # Default provider is set to Jio. Can be overridden.
    activation_year: int = Field(..., ge=2020, le=2025, description="Year of SIM card activation. Must be between 2020 and 2025.")

# Registration class combines the Employee and Sim_model.
# This is used to create a complete profile of an employee's telecom information.
class Registration(BaseModel):
    employee: Employee
    sim: Sim_model

# Sample data to simulate an employee and their SIM details.
# This data could be passed as input for API requests or used for testing purposes.
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

# Create an instance of the Employee class by passing the employee data.
emp = Employee(**data["employee"])

# Create an instance of the Sim_model class by passing the SIM details.
s = Sim_model(**data["sim"])

# Print the employee and sim model objects to check the data.
# The output will be a Pydantic model instance with validated data.
print(emp)
print(s)

# Sample Output Section:

# Sample data input:
# {
#     "employee": {
#         "emp_id": 12345,
#         "name": "Asha",
#         "department": "Engineering"
#     },
#     "sim": {
#         "number": "9876543210",
#         "provider": "Airtel",
#         "activation_year": 2023
#     }
# }

# Sample Output when the employee and sim model objects are printed:
# Employee(emp_id=12345, name='Asha', department='Engineering')
# Sim_model(number='9876543210', provider='Airtel', activation_year=2023)

