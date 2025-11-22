from pydantic import BaseModel,Field
from typing import List,Optional,Dict

class Employee(BaseModel):
    emp_id : int = Field(...,ge=1000,le=999999)
    name : str = Field(...,min_length=2)
    department : str = Field("General")

class SIM(BaseModel):
    number : str = Field(...,min_length=10,max_length=10)
    provider : str = Field("Jio")
    activation_year : int = Field(...,ge=2020 , le=2025)

class Register(BaseModel):
    employee : Employee
    sim : SIM

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

obj=Register(employee=data["employee"],sim=data["sim"])
print(obj.__dict__)