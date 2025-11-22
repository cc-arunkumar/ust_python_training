
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)
    name: str = Field(..., min_length=2)
    department: str = "General"   # fixed typo

class SIM(BaseModel):
    number: str = Field(..., pattern=r"^\d{10}$")
    provider: str = "Jio"
    activation_year: int = Field(..., ge=2020, le=2025)

class Registration(BaseModel):
    employee: Employee=Field(...)
    sim: SIM=Field(...)

data ={ 
    "employee":{
        "emp_id": 12345,
        "name": "Asha",
        "department": "Engineering"
    },
    "sim":{
        "number": "9876543210",
        "provider": "Airtel",
        "activation_year": 2023
    }
}

reg= Registration(**data)
print(reg)

data_optional = {
    "employee": {"emp_id": 12345, "name": "Asha"},
    "sim": {"number": "9876543210", "activation_year": 2023}
}
reg=Registration(**data_optional)
print(reg)

try:
    Registration(employee={"emp_id": 999, "name": "Asha"}, sim={"number": "9876543210", "activation_year": 2023})
except Exception as e:
    print("emp_id error:", e)

# name too short
try:
    Registration(employee={"emp_id": 12345, "name": "A"}, sim={"number": "9876543210", "activation_year": 2023})
except Exception as e:
    print("name error:", e)

# SIM number not 10 digits
try:
    Registration(employee={"emp_id": 12345, "name": "Asha"}, sim={"number": "12345", "activation_year": 2023})
except Exception as e:
    print("number error:", e)

# activation_year too low
try:
    Registration(employee={"emp_id": 12345, "name": "Asha"}, sim={"number": "9876543210", "activation_year": 2019})
except Exception as e:
    print("activation_year low error:", e)

# activation_year too high
try:
    Registration(employee={"emp_id": 12345, "name": "Asha"}, sim={"number": "9876543210", "activation_year": 2030})
except Exception as e:
    print("activation_year high error:", e)