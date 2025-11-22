from typing import List,Optional
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field


class Employee(BaseModel):
    emp_id : int = Field(...,ge=1000,le=999999,description="Employee id should be in between 1000 and 999999")
    name : str = Field(...,min_length=2)
    department : Optional[str] = Field("General")
    
class Sim(BaseModel):
    number : str = Field(...,min_length=10,max_length=10,description="Length shoulf be exactly 10")
    provider : Optional[str] = Field("Jio")
    activation_year : int = Field(...,ge=2020,le=2025,description="Employee id should be in between 2020 and 2025")
    
class Register(BaseModel):
    employee : Employee
    sim : Sim
    
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

obj = Register(employee=data["employee"],sim=data["sim"])
print(obj.__dict__)