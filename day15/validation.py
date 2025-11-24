# UST Employee Telecom Device Registration

# This API allows UST employees to register their details along with the SIM card issued for official communication. The registration process involves validating employee and SIM details using Pydantic models:

# Employee Model:
# Validates employee ID (emp_id), name, and department.
# The employee ID must be between 1000 and 999999, the name should have at least 2 characters, and the department defaults to "General" if not provided.

# SIM Model:
# Validates the SIM card details, including the 10-digit SIM number, telecom provider (defaults to "Jio"), and activation year (between 2020 and 2025).

# Registration Model:
# Combines both the Employee and SIM models, enabling a nested structure for validation and easier registration of employee-SIM pairs.

# Test cases include scenarios for both valid and invalid inputs, with appropriate validation error messages for missing fields, length violations, pattern mismatches, and numeric constraints. 
# The models ensure data integrity and proper registration flow.


from pydantic import BaseModel, Field
from typing import Optional

# Employee Model
class Employee(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee Id not valid")
    name: str = Field(..., min_length=2, description="Name should be a minimum of length 2")
    department: Optional[str] = Field(default="General", description="Department name")

# SIM Model
class Sim(BaseModel):
    number: str = Field(..., pattern=r"^\d{10}$", description="Must be exactly 10 digits")
    provider: Optional[str] = Field(default="Jio", description="Provider name")
    activation_year: int = Field(..., ge=2020, le=2025, description="Year must be from 2020 to 2025")

# Registration Model (Nesting Employee and SIM models)
class Registration(BaseModel):
    employee: Employee
    sim: Sim

# Example of a valid input
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

# Creating and printing the registration object
registration = Registration(**data)
print(registration)  # This should print the valid registration object

# Example of an invalid input (to test validation)
invalid_data = {
    "employee": {
        "emp_id": 999,  # Invalid emp_id
        "name": "A"  # Invalid name (too short)
    },
    "sim": {
        "number": "12345",  # Invalid number (not 10 digits)
        "activation_year": 2019  # Invalid year (too early)
    }
}

try:
    registration_invalid = Registration(**invalid_data)
except Exception as e:
    print(e)  # This will print the validation error



# sample output


# employee=Employee(emp_id=12345, name='Asha', department='Engineering') sim=Sim(number='9876543210', provider='Airtel', activation_year=2023)
# 4 validation errors for Registration

# employee.emp_id
#   Input should be greater than or equal to 1000 [type=greater_than_equal, input_value=999, input_type=int] 
 
# employee.name
#   String should have at least 2 characters [type=string_too_short, input_value='A', input_type=str]

# sim.number
#   String should match pattern '^\d{10}$' [type=string_pattern_mismatch, input_value='12345', input_type=str]

# sim.activation_year
#   Input should be greater than or equal to 2020 [type=greater_than_equal, input_value=2019, input_type=int] 