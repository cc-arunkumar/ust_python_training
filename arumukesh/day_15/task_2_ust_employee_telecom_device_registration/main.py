from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)  
    name: str = Field(..., min_length=2)           
    department: str = "General"  

e = Employee(emp_id=1234, name="Asha", department="Information Technology")
print(e)

class SIM(BaseModel):
    number: str = Field(..., pattern=r"^\d{10}$") 
    provider: str = Field(default="Jio")           
    activation_year: int = Field(..., ge=2020, le=2025) 
    

class Registration(BaseModel):
    employee: Employee
    sim: SIM

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

reg = Registration(employee=data["employee"],sim=data["sim"])
print(reg)

# #Output
# emp_id=1234 name='Asha' department='Information Technology'
# employee=Employee(emp_id=12345, name='Asha', department='Engineering') sim=SIM(number='9876543210', provider='Airtel', activation_year=2023)