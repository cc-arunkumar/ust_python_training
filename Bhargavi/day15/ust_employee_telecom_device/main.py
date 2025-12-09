# UST Employee Telecom Device registration

# Scenario
# UST provides company SIM cards to employees for official communication.
# When a SIM is issued, an employee must register their details and SIM details.
# You will create Pydantic models to validate the registration input.

# Model Requirements
# �� Employee Model
# Field Type Required Rules
# emp_id int YES ge=1000 , le=999999
# name str YES min_length=2
# department str NO default: "General"
# �� SIM Model
# Field Type Required Rules
# number str YES must be exactly 10 digits
# provider str NO default: "Jio"
# activation_year int YES ge=2020 , le=2025
# Regex for SIM number:
# pattern=r"^\d{10}$"
# �� Registration Model
# (Nesting practice — model inside model)
# UST Employee Telecom Device Registration 1
# Field Type Required
# employee Employee YES
# sim SIM YES
# �� Example of VALID input dictionary
# Students must test with this:
# data = {
#  "employee": {
#  "emp_id": 12345,
#  "name": "Asha",
#  "department": "Engineering"
#  },
#  "sim": {
#  "number": "9876543210",
#  "provider": "Airtel",
#  "activation_year": 2023
#  }
# }
# Expected: model should create successfully and print the object.
# Example of OPTIONAL fields
# Candidates must test with this too (provider + department missing):
# data = {
#  "employee": {
#  "emp_id": 12345,
#  "name": "Asha"
#  },
#  "sim": {
#  "number": "9876543210",
#  "activation_year": 2023
# UST Employee Telecom Device Registration 2
#  }
# }
# Expected:
# department should default to "General"
# provider should default to "Jio"
# Validation error test cases
# Each of these MUST show a ValidationError:
# Wrong Input Reason
# emp_id = 999 ge rule violated
# name = "A" min_length violated
# number = "12345" 10 digit violated
# activation_year = 2019 ge rule violated
# activation_year = 2030 le rule violated
# Students must try each test separately and observe error messages.
# Expected output examples
# Success case
# employee=Employee(emp_id=12345, name='Asha', department='Engineerin
# g')
# sim=SIM(number='9876543210', provider='Airtel', activation_year=2023)
# Default assignment case
# When department and provider missing:
# UST Employee Telecom Device Registration 3
# department='General'
# provider='Jio'
# Failure case examples
# Error message should mention:
# missing field, or
# minimum length, or
# pattern mismatch, or
# numeric constraints
# Deliverables from participants
# They need to submit:
# 1. All 3 model class definitions
# 2. Output of valid registration object printed
# 3. Output of default-field test printed
# 4. Validation error outputs for each failed case
# # UST Employee Telecom Device Registration 4

# UST Employee Telecom Device
# Registration
# Scenario
# UST provides company SIM cards to employees for official communication.
# When a SIM is issued, an employee must register their details and SIM details.
# You will create Pydantic models to validate the registration input.
# Model Requirements
# 1. Employee Model
# 2. SIM Model
# 3. Registration Model
# (Nesting practice — model inside model)
# Expected output examples
# Success case
# employee=Employee(emp_id=12345, name='Asha', department='Engineerin
# g')
# sim=SIM(number='9876543210', provider='Airtel', activation_year=2023)
# Default assignment case
# When department and provider missing:
# UST Employee Telecom Device Registration 3
# department='General'
# provider='Jio'
# Failure case examples
# Error message should mention:
# missing field, or
# minimum length, or
# pattern mismatch, or
# numeric constraints


from pydantic import BaseModel, Field
from typing import Optional


# Employee Model

class Employee(BaseModel):
    """
    Represents basic employee details.
    Includes validation for employee ID and name.
    """
    # Employee ID must be between 1000 and 999999
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee Id not valid")
    
    # Name must be at least 2 characters long
    name: str = Field(..., min_length=2, description="Name should be a minimum of length 2")
    
    # Department is optional, defaults to "General"
    department: Optional[str] = Field(default="General", description="Department name")


# SIM Model

class Sim(BaseModel):
    """
    Represents SIM card details for an employee.
    Includes validation for SIM number and activation year.
    """
    # SIM number must be exactly 10 digits
    number: str = Field(..., pattern=r"^\d{10}$", description="Must be exactly 10 digits")
    
    # Provider is optional, defaults to "Jio"
    provider: Optional[str] = Field(default="Jio", description="Provider name")
    
    # Activation year must be between 2020 and 2025
    activation_year: int = Field(..., ge=2020, le=2025, description="Year must be from 2020 to 2025")



# Registration Model

class Registration(BaseModel):
    """
    Combines Employee and SIM models into a single registration object.
    Demonstrates nested Pydantic models.
    """
    employee: Employee
    sim: Sim


# Example of a valid input

data = {
    "employee": {
        "emp_id": 12345,          # Valid employee ID
        "name": "Asha",           # Valid name (>= 2 chars)
        "department": "Engineering"
    },
    "sim": {
        "number": "9876543210",   # Valid 10-digit SIM number
        "provider": "Airtel",     # Custom provider
        "activation_year": 2023   # Valid year within range
    }
}

# Creating and printing the registration object
registration = Registration(**data)
print(registration)  # This should print the valid registration object


# Example of an invalid input

invalid_data = {
    "employee": {
        "emp_id": 999,   # Invalid emp_id (too small)
        "name": "A"      # Invalid name (too short)
    },
    "sim": {
        "number": "12345",        # Invalid SIM number (not 10 digits)
        "activation_year": 2019   # Invalid year (too early)
    }
}

# Attempt to create invalid registration object
try:
    registration_invalid = Registration(**invalid_data)
except Exception as e:
    # Prints validation errors raised by Pydantic
    print(e)  # This will show detailed validation error messages



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
