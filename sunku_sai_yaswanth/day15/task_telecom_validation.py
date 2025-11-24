# Task: telecom validation
from pydantic import BaseModel, Field
import re

# -----------------------------
# Employee model with validation
# -----------------------------
class EmployeeModel(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)   # Employee ID must be between 1000 and 999999
    name: str = Field(..., min_length=2)           # Name must have at least 2 characters
    department: str = Field("General")             # Default department is "General" if not provided

# -----------------------------
# SIM model with validation
# -----------------------------
class SIMModel(BaseModel):
    number: str = Field(..., min_length=10, max_length=10)  # SIM number must be exactly 10 characters
    provider: str = Field("Jio")                            # Default provider is "Jio"
    activation_year: int = Field(..., ge=2020, le=2025)     # Activation year must be between 2020 and 2025

    # Custom validator for SIM number
    def validate_number(cls, value):
        pattern = r'^\d{10}$'
        if not re.match(pattern, value):
            raise ValueError('SIM number must be exactly 10 digits')
        return value

# -----------------------------
# Registration model combining Employee + SIM
# -----------------------------
class RegistrationModel(BaseModel):
    employee: EmployeeModel = Field(...)   # Nested Employee model
    sim: SIMModel = Field(...)             # Nested SIM model

# -----------------------------
# 1. Valid input data
# -----------------------------
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
registration_valid = RegistrationModel(**valid_data)
print("Valid Registration:")
print(registration_valid)

# -----------------------------
# 2. Input with default values (department + provider omitted)
# -----------------------------
default_fields_data = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha"
    },
    "sim": {
        "number": "9876543210",
        "activation_year": 2023
    }
}
registration_default = RegistrationModel(**default_fields_data)
print("\nRegistration with default values:")
print(registration_default)

# -----------------------------
# 3. Invalid emp_id (less than 1000)
# -----------------------------
invalid_emp_id = {
    "employee": {
        "emp_id": 999,   # Invalid: less than 1000
        "name": "Asha",
        "department": "Engineering"
    },
    "sim": {
        "number": "9876543210",
        "provider": "Airtel",
        "activation_year": 2023
    }
}
try:
    registration_invalid_emp_id = RegistrationModel(**invalid_emp_id)
except ValueError as e:
    print("ge rule violated:", e)

# -----------------------------
# 4. Invalid name (less than 2 characters)
# -----------------------------
invalid_name = {
    "employee": {
        "emp_id": 12345,
        "name": "A",   # Invalid: only 1 character
        "department": "Engineering"
    },
    "sim": {
        "number": "9876543210",
        "provider": "Airtel",
        "activation_year": 2023
    }
}
try:
    registration_invalid_name = RegistrationModel(**invalid_name)
except ValueError as e:
    print("min_length violated:", e)

# -----------------------------
# 5. Invalid SIM number (not 10 digits)
# -----------------------------
invalid_data_sim_number = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha",
        "department": "Engineering"
    },
    "sim": {
        "number": "12345",   # Invalid: only 5 digits
        "provider": "Airtel",
        "activation_year": 2023
    }
}
try:
    registration_invalid_sim_number = RegistrationModel(**invalid_data_sim_number)
except ValueError as e:
    print("\n10 digit violated:", e)

# -----------------------------
# 6. Invalid activation_year (less than 2020)
# -----------------------------
invalid_activation_year_low = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha",
        "department": "Engineering"
    },
    "sim": {
        "number": "9876543210",
        "provider": "Airtel",
        "activation_year": 2019   # Invalid: less than 2020
    }
}
try:
    registration_activation_year = RegistrationModel(**invalid_activation_year_low)
except ValueError as e:
    print("\n ge rule violated:", e)

# -----------------------------
# 7. Invalid activation_year (greater than 2025)
# -----------------------------
invalid_activation_year_high = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha",
        "department": "Engineering"
    },
    "sim": {
        "number": "9876543210",
        "provider": "Airtel",
        "activation_year": 2030   # Invalid: greater than 2025
    }
}
try:
    registration_activation_year_high = RegistrationModel(**invalid_activation_year_high)
except ValueError as e:
    print("\n le rule violated:", e)



# output
# Valid Registration:
# employee=EmployeeModel(emp_id=12345, name='Asha', department='Engineering') sim=SIMModel(number='9876543210', provider='Airtel', activation_year=2023)

# Registration with default values:
# employee=EmployeeModel(emp_id=12345, name='Asha', department='General') sim=SIMModel(number='9876543210', provider='Jio', activation_year=2023)
# ge rule violated: 1 validation error for RegistrationModel
# employee.emp_id
#   Input should be greater than or equal to 1000 [type=greater_than_equal, input_value=999, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/greater_than_equal
# min_length violated: 1 validation error for RegistrationModel
# employee.name
#   String should have at least 2 characters [type=string_too_short, input_value='A', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.12/v/string_too_short

# 10 digit violated: 1 validation error for RegistrationModel
# sim.number
#   String should have at least 10 characters [type=string_too_short, input_value='12345', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.12/v/string_too_short

#  ge rule violated: 1 validation error for RegistrationModel
# sim.activation_year
#   Input should be greater than or equal to 2020 [type=greater_than_equal, input_value=2019, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/greater_than_equal

#  le rule violated: 1 validation error for RegistrationModel
# sim.activation_year
#   Input should be less than or equal to 2025 [type=less_than_equal, input_value=2030, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/less_than_equal
