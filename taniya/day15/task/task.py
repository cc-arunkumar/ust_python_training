from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="UST Employee Telecom Device Registration")

# Employee model with validation rules
class Employee(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999, description="emp_id should be between 1000 and 999999")
    name: str = Field(..., min_length=2, description="name length should be minimum 2")
    department: str = Field(default="General")

# SIM model with validation rules
class SIM(BaseModel):   # ⚠️ should inherit from BaseModel for validation
    number: str = Field(..., regex=r"^\d{10}$")   # must be exactly 10 digits
    provider: str = Field(default="Jio")
    activation_year: int = Field(..., ge=2020, le=2025, description="year should be between 2020 to 2025")

# Registration model combining Employee and SIM
class Registration(BaseModel):   # ⚠️ should inherit from BaseModel
    employee: Employee = Field(...)
    sim: SIM = Field(...)

@app.post("/register")
def register_device():
    # Success Case
    print("\nSuccess Case:")
    data = {
        "employee": {"emp_id": 12345, "name": "Asha", "department": "Engineering"},
        "sim": {"number": "9876543210", "provider": "Airtel", "activation_year": 2023}
    }
    reg1 = Registration(**data)
    print(reg1)

    # Default Assignment Case
    print("\nDefault Assignment Case:")
    data_defaults = {
        "employee": {"emp_id": 12345, "name": "Asha"},  # department defaults to "General"
        "sim": {"number": "9876543210", "activation_year": 2023}  # provider defaults to "Jio"
    }
    reg2 = Registration(**data_defaults)
    print(reg2)

    # Validation Error Cases
    print("\nValidation Error Cases:")
    test_cases = [
        # emp_id too small
        {"employee": {"emp_id": 999, "name": "Asha", "department": "Engineering"},
         "sim": {"number": "9876543210", "provider": "Airtel", "activation_year": 2023}},
        # emp_id too large
        {"employee": {"emp_id": 1000000, "name": "Asha", "department": "Engineering"},
         "sim": {"number": "9876543210", "provider": "Airtel", "activation_year": 2023}},
        # name too short
        {"employee": {"emp_id": 12345, "name": "A", "department": "Engineering"},
         "sim": {"number": "9876543210", "provider": "Airtel", "activation_year": 2023}},
        # SIM number too short
        {"employee": {"emp_id": 12345, "name": "Asha", "department": "Engineering"},
         "sim": {"number": "12345", "provider": "Airtel", "activation_year": 2023}},
        # SIM number contains letters
        {"employee": {"emp_id": 12345, "name": "Asha", "department": "Engineering"},
         "sim": {"number": "98765ABCD1", "provider": "Airtel", "activation_year": 2023}},
        # activation_year out of range
        {"employee": {"emp_id": 12345, "name": "Asha", "department": "Engineering"},
         "sim": {"number": "9876543210", "provider": "Airtel", "activation_year": 2019}}
    ]

    for case in test_cases:
        try:
            reg = Registration(**case)
            print(reg)
        except Exception as e:
            print(f"Error: {e}")
            
# Output
# Success Case:
# employee=Employee(emp_id=12345, name='Asha', department='Engineering') 
# sim=SIM(number='9876543210', provider='Airtel', activation_year=2023)

# Default Assignment Case:
# employee=Employee(emp_id=12345, name='Asha', department='General') 
# sim=SIM(number='9876543210', provider='Jio', activation_year=2023)

# Validation Error Cases:
# Error: 1 validation error for Registration
# employee -> emp_id
#   ensure this value is greater than or equal to 1000 (type=value_error.number.not_ge)

# Error: 1 validation error for Registration
# employee -> emp_id
#   ensure this value is less than or equal to 999999 (type=value_error.number.not_le)

# Error: 1 validation error for Registration
# employee -> name
#   ensure this value has at least 2 characters (type=value_error.any_str.min_length)

# Error: 1 validation error for Registration
# sim -> number
#   string does not match regex "^\d{10}$" (type=value_error.str.regex)

# Error: 1 validation error for Registration
# sim -> number
#   string does not match regex "^\d{10}$" (type=value_error.str.regex)

# Error: 1 validation error for Registration
# sim -> activation_year
#   ensure this value is greater than or equal to 2020 (type=value_error.number.not_ge)