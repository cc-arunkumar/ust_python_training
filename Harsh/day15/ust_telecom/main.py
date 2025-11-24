from pydantic import BaseModel, Field
import re

# Employee model with constraints
class Employee(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)   # must be between 1000 and 999999
    name: str = Field(..., min_length=2)           # must have at least 2 characters
    department: str = "General"                    # default value if not provided

# SIM model with constraints
class SIM(BaseModel):
    number: str = Field(..., pattern=r"^\d{10}$")  # must be exactly 10 digits
    provider: str = "Jio"                          # default provider
    activation_year: int = Field(..., ge=2020, le=2025)  # must be between 2020–2025

# Registration model combining Employee and SIM
class Registration(BaseModel):
    employee: Employee = Field(...)
    sim: SIM = Field(...)

# -----------------------------
# Valid data with all fields
# -----------------------------
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

reg = Registration(**data)
print(reg)   # ✅ should succeed

# -----------------------------
# Valid data with optional defaults
# -----------------------------
data_optional = {
    "employee": {"emp_id": 12345, "name": "Asha"},   # department defaults to "General"
    "sim": {"number": "9876543210", "activation_year": 2023}  # provider defaults to "Jio"
}
reg = Registration(**data_optional)
print(reg)   # ✅ should succeed

# -----------------------------
# Invalid cases
# -----------------------------

# emp_id too low (<1000)
try:
    Registration(employee={"emp_id": 999, "name": "Asha"}, sim={"number": "9876543210", "activation_year": 2023})
except Exception as e:
    print("emp_id error:", e)

# name too short (<2 chars)
try:
    Registration(employee={"emp_id": 12345, "name": "A"}, sim={"number": "9876543210", "activation_year": 2023})
except Exception as e:
    print("name error:", e)

# SIM number not 10 digits
try:
    Registration(employee={"emp_id": 12345, "name": "Asha"}, sim={"number": "12345", "activation_year": 2023})
except Exception as e:
    print("number error:", e)

# activation_year too low (<2020)
try:
    Registration(employee={"emp_id": 12345, "name": "Asha"}, sim={"number": "9876543210", "activation_year": 2019})
except Exception as e:
    print("activation_year low error:", e)

# activation_year too high (>2025)
try:
    Registration(employee={"emp_id": 12345, "name": "Asha"}, sim={"number": "9876543210", "activation_year": 2030})
except Exception as e:
    print("activation_year high error:", e)

# Valid Cases
# employee=Employee(emp_id=12345, name='Asha', department='Engineering') 
# sim=SIM(number='9876543210', provider='Airtel', activation_year=2023)

# employee=Employee(emp_id=12345, name='Asha', department='General') 
# sim=SIM(number='9876543210', provider='Jio', activation_year=2023)

# Invalid Cases
# emp_id error: 1 validation error for Registration
# employee -> emp_id
#   ensure this value is greater than or equal to 1000 (type=value_error.number.not_ge; limit_value=1000)

# name error: 1 validation error for Registration
# employee -> name
#   ensure this value has at least 2 characters (type=value_error.any_str.min_length; limit_value=2)

# number error: 1 validation error for Registration
# sim -> number
#   string does not match regex "^\d{10}$" (type=value_error.str.regex; pattern=^\d{10}$)

# activation_year low error: 1 validation error for Registration
# sim -> activation_year
#   ensure this value is greater than or equal to 2020 (type=value_error.number.not_ge; limit_value=2020)

# activation_year high error: 1 validation error for Registration
# sim -> activation_year
#   ensure this value is less than or equal to 2025 (type=value_error.number.not_le; limit_value=2025)

