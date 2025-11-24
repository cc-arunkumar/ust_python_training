# UST Employee Telecom Device Registration

from fastapi import FastAPI
from pydantic import BaseModel, Field, ValidationError

app = FastAPI(title="UST Employee Telecom Device Registration")

# Employee Model
class Employee(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee ID must be between 1000 and 999999")
    name: str = Field(..., min_length=2, description="Name must be at least 2 characters long")
    department: str = Field("General", description="Defaults to 'General' if not provided")

    # NOTE: In production, ensure that emp_id is unique across the system (e.g., use a database constraint)
    #       Additionally, employee data might be fetched from an external HR system.

# SIM Model
class Sim(BaseModel):
    number: str = Field(..., pattern=r"^\d{10}$", description="SIM number must be exactly 10 digits")
    provider: str = Field("Jio", description="Defaults to 'Jio' if not provided")
    activation_year: int = Field(..., ge=2020, le=2025, description="Activation year must be between 2020 and 2025")

    # NOTE: Ensure that the SIM number is validated against real-time databases for correctness (e.g., no duplicates).
    #       Provider might need validation against a list of authorized providers.

# Registration Model (nested)
class Registration(BaseModel):
    employee: Employee  # Employee information
    sim: Sim  # SIM card details

    # NOTE: The Registration model ties together employee and SIM data and will require proper error handling and validations.

#  Success Case
data_valid = {
    "employee": {"emp_id": 12345, "name": "Asha", "department": "Engineering"},
    "sim": {"number": "9876543210", "provider": "Airtel", "activation_year": 2023}
}
registration_valid = Registration(**data_valid)
print(" Success case:\n", registration_valid)

#  Defaults Case (provider + department missing)
data_defaults = {
    "employee": {"emp_id": 12345, "name": "Asha"},
    "sim": {"number": "9876543210", "activation_year": 2023}
}
registration_defaults = Registration(**data_defaults)
print("\n Defaults case:\n", registration_defaults)

#  Validation Error Cases
def try_registration(data, label):
    try:
        Registration(**data)
    except ValidationError as e:
        # NOTE: Production should log these errors to a centralized logging service for better traceability and troubleshooting.
        print(f"\n {label}:\n", e)

# emp_id too small
try_registration(
    {"employee": {"emp_id": 999, "name": "Asha"},
     "sim": {"number": "9876543210", "activation_year": 2023}},
    "emp_id error"
)

# name too short
try_registration(
    {"employee": {"emp_id": 12345, "name": "A"},
     "sim": {"number": "9876543210", "activation_year": 2023}},
    "name error"
)

# SIM number not 10 digits
try_registration(
    {"employee": {"emp_id": 12345, "name": "Asha"},
     "sim": {"number": "12345", "activation_year": 2023}},
    "SIM number error"
)

# activation_year too low
try_registration(
    {"employee": {"emp_id": 12345, "name": "Asha"},
     "sim": {"number": "9876543210", "activation_year": 2019}},
    "activation_year too low"
)

# activation_year too high
try_registration(
    {"employee": {"emp_id": 12345, "name": "Asha"},
     "sim": {"number": "9876543210", "activation_year": 2030}},
    "activation_year too high"
)
