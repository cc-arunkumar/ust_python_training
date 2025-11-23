from pydantic import BaseModel, Field
import re

class EmployeeModel(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)  
    name: str = Field(..., min_length=2)  
    department: str = Field("General")  

class SIMModel(BaseModel):
    number: str = Field(..., min_length=10, max_length=10) 
    provider: str = Field("Jio")  
    activation_year: int = Field(..., ge=2020, le=2025)  

    def validate_number(cls, value):
        pattern=r'^\d{10}$'
        if not re.match(pattern, value):
            raise ValueError('SIM number must be exactly 10 digits')
        return value


class RegistrationModel(BaseModel):
    employee: EmployeeModel = Field(...)  
    sim: SIMModel = Field(...)  

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

registration_default = RegistrationModel(**default_fields_data)
print("\nRegistration with default values:")
print(registration_default)

# 1. Invalid emp_id (less than 1000)
invalid_emp_id = {
    "employee": {
        "emp_id": 999,  
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
    print("ge rule violated",e)

# 2. Invalid name (less than 2 characters)
invalid_name = {
    "employee": {
        "emp_id": 12345,
        "name": "A",  
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
    print("min_length violated",e)
    
    
# 3. Invalid SIM number (not exactly 10 digits)
invalid_data_sim_number = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha",
        "department": "Engineering"
    },
    "sim": {
        "number": "12345", 
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
        "activation_year": 2019  # Invalid activation year
    }
}
try:
    registration_activation_year = RegistrationModel(**invalid_activation_year_low)
except ValueError as e:
    print("\n ge rule violated:", e)

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
        "activation_year": 2030  # Invalid activation year
    }
}

try:
    registration_activation_year_high = RegistrationModel(**invalid_activation_year_high)
except ValueError as e:
    print("\n le rule violated):", e)

    