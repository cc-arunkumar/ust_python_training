from fastapi import FastAPI
from pydantic import BaseModel, Field, ValidationError

app = FastAPI()

class EmployeeModel(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)
    name: str = Field(..., min_length=2)
    department: str = Field("General")

class SimModel(BaseModel):
    number: str = Field(..., regex=r"^\d{10}$")   
    provider: str = Field("Jio")
    activation_year: int = Field(..., ge=2020, le=2025)

class Registration(BaseModel):
    employee: EmployeeModel
    sim: SimModel

# Valid data
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

print("\n--- Success Case ---")
reg = Registration(**data)
print(reg)

print("\n--- Default Assignment Case ---")
data_defaults = {
    "employee": {"emp_id": 12345, "name": "Asha"},
    "sim": {"number": "9876543210", "activation_year": 2023}
}
reg2 = Registration(**data_defaults)
print(reg2)


# emp_id too small
try:
    Registration(employee={"emp_id": 999, "name": "Asha"}, sim={"number": "9876543210", "activation_year": 2023})
except ValidationError as e:
    print("emp_id=999 error:\n", e)

# name too short
try:
    Registration(employee={"emp_id": 12345, "name": "A"}, sim={"number": "9876543210", "activation_year": 2023})
except ValidationError as e:
    print("name='A' error:\n", e)

# number not 10 digits
try:
    Registration(employee={"emp_id": 12345, "name": "Asha"}, sim={"number": "12345", "activation_year": 2023})
except ValidationError as e:
    print("number='12345' error:\n", e)

# activation_year too small
try:
    Registration(employee={"emp_id": 12345, "name": "Asha"}, sim={"number": "9876543210", "activation_year": 2019})
except ValidationError as e:
    print("activation_year=2019 error:\n", e)

# activation_year too large
try:
    Registration(employee={"emp_id": 12345, "name": "Asha"}, sim={"number": "9876543210", "activation_year": 2030})
except ValidationError as e:
    print("activation_year=2030 error:\n", e)
    

# --------------------------------------------------------------------------------------

# Sample output

# --- Success Case ---
# employee=EmployeeModel(emp_id=12345, name='Asha', department='Engineering') sim=SimModel(number='9876543210', provider='Airtel', activation_year=2023)

# --- Default Assignment Case ---
# employee=EmployeeModel(emp_id=12345, name='Asha', department='General') sim=SimModel(number='9876543210', provider='Jio', activation_year=2023)

# emp_id=999 error:
#  1 validation error for Registration
#  employee -> emp_id
#    ensure this value is greater than or equal to 1000 (type=value_error.number.not_ge; limit_value=1000)

# name='A' error:
#  1 validation error for Registration
#  employee -> name
#    ensure this value has at least 2 characters (type=value_error.str.min_length; limit_value=2)

# number='12345' error:
#  1 validation error for Registration
#  sim -> number
#    string does not match regex "^\\d{10}$" (type=value_error.str.regex; pattern='^\\d{10}$')

# activation_year=2019 error:
#  1 validation error for Registration
#  sim -> activation_year
#    ensure this value is greater than or equal to 2020 (type=value_error.number.not_ge; limit_value=2020)

# activation_year=2030 error:
#  1 validation error for Registration
#  sim -> activation_year
#    ensure this value is less than or equal to 2025 (type=value_error.number.not_le; limit_value=2025)
