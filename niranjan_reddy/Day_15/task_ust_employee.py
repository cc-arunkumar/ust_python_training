# UST Employee Telecom Device
# Registration
# Scenario
# UST provides company SIM cards to employees for official communication.
# When a SIM is issued, an employee must register their details and SIM details.
# You will create Pydantic models to validate the registration input.

from pydantic import BaseModel, Field
import re

# Define a model for Employee data
class EmployeeModel(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)  # emp_id must be between 1000 and 999999
    name: str = Field(..., min_length=2)  # Name must be at least 2 characters
    department: str = Field("General")  # Default department is 'General'

# Define a model for SIM data
class SIMModel(BaseModel):
    number: str = Field(..., min_length=10, max_length=10)  # SIM number must be exactly 10 digits
    provider: str = Field("Jio")  # Default provider is 'Jio'
    activation_year: int = Field(..., ge=2020, le=2025)  # Activation year must be between 2020 and 2025

    # Custom validator for SIM number format (must be exactly 10 digits)
    def validate_number(cls, value):
        pattern = r'^\d{10}$'  # Regex pattern for 10 digits
        if not re.match(pattern, value):
            raise ValueError('SIM number must be exactly 10 digits')
        return value

# Define a registration model that ties the Employee and SIM models together
class RegistrationModel(BaseModel):
    employee: EmployeeModel = Field(...)  # Employee data
    sim: SIMModel = Field(...)  # SIM data

# Valid data for testing
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

# Test with valid data
registration_valid = RegistrationModel(**valid_data)
print("Valid Registration:")
print(registration_valid)

# Input dictionary with missing optional fields (provider + department missing)
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

# Test with default field values (department and provider)
registration_default = RegistrationModel(**default_fields_data)
print("\nRegistration with default values:")
print(registration_default)

# 1. Invalid emp_id (less than 1000)
invalid_emp_id = {
    "employee": {
        "emp_id": 999,  # Invalid emp_id
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

# 2. Invalid name (less than 2 characters)
invalid_name = {
    "employee": {
        "emp_id": 12345,
        "name": "A",  # Invalid name (less than 2 characters)
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

# 3. Invalid SIM number (not exactly 10 digits)
invalid_data_sim_number = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha",
        "department": "Engineering"
    },
    "sim": {
        "number": "12345",  # Invalid SIM number (less than 10 digits)
        "provider": "Airtel",
        "activation_year": 2023
    }
}

try:
    registration_invalid_sim_number = RegistrationModel(**invalid_data_sim_number)
except ValueError as e:
    print("\n10 digit violated:", e)

# 4. Invalid activation_year (less than 2020)
invalid_activation_year_low = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha",
        "department": "Engineering"
    },
    "sim": {
        "number": "9876543210",
        "provider": "Airtel",
        "activation_year": 2019  # Invalid activation year (below 2020)
    }
}

try:
    registration_activation_year = RegistrationModel(**invalid_activation_year_low)
except ValueError as e:
    print("\nge rule violated:", e)

# 5. Invalid activation_year (greater than 2025)
invalid_activation_year_high = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha",
        "department": "Engineering"
    },
    "sim": {
        "number": "9876543210",
        "provider": "Airtel",
        "activation_year": 2030  # Invalid activation year (above 2025)
    }
}

try:
    registration_activation_year_high = RegistrationModel(**invalid_activation_year_high)
except ValueError as e:
    print("\nle rule violated:", e)

#Sample ouput


# **Output for registration with default values:**
# Registration with default values:
# employee=EmployeeModel(emp_id=12345, name='Asha', department='General') 
# sim=SIMModel(number='9876543210', provider='Jio', activation_year=2023)

# **Output for valid registration:**
# Valid Registration:
# employee=EmployeeModel(emp_id=12345, name='Asha', department='Engineering') 
# sim=SIMModel(number='9876543210', provider='Airtel', activation_year=2023)


# **Output for invalid emp_id:**
# ge rule violated:  value is not a valid integer (type=value_error.integer)


# **Output for invalid SIM number:**
# 10 digit violated: SIM number must be exactly 10 digits (type=value_error)


# **Output for invalid name:**
# min_length violated:  ensure this value has at least 2 characters (type=value_error.any_str.min_length; limit_value=2)


# **Output for invalid activation year (below 2020):**
# ge rule violated:  ensure this value is greater than or equal to 2020 (type=value_error.number.ge; limit_value=2020)


# **Output for invalid activation year (above 2025):**
# le rule violated:  ensure this value is less than or equal to 2025 (type=value_error.number.le; limit_value=2025)
