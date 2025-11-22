from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field
from typing import List,Optional

app = FastAPI(title="UST Employee Telecom DeviceRegistration")

class EmployeeModel(BaseModel):
    emp_id:int = Field(...,ge=1000,le=999999,description="id in between 1000 and 999999")
    name:str = Field(...,min_length=2)
    department:Optional[str] = Field(default="General")
    
class SimModel(BaseModel):
    number:str = Field(...,max_length=10,min_length=10)
    provider:Optional[str] = Field(default="Jio")
    activation_year:int = Field(...,ge=2020,le=2025)
    
class RegistrationModel(BaseModel):
    employee:EmployeeModel
    sim:SimModel
    
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
obj = RegistrationModel(
    employee=data["employee"],
    sim=data["sim"]
)
print(obj.__dict__)