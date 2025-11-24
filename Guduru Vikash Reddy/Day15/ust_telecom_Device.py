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
