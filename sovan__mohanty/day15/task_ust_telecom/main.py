from fastapi import FastAPI
from pydantic import BaseModel,Field
import re
class Employee(BaseModel):
    emp_id: int=Field(...,ge=1000,le=999999)
    name: str=Field(...,min_length=2)
    department: str="General"
e=Employee(emp_id=12345,
 name= "Asha",
 department= "Engineering")
class Sim(BaseModel):
    number: str=Field(...,pattern=r"^\d{10}$")
    provider: str="Jio"
    activation_year: int=Field(...,ge=2020,le=2025)
    
class Registration(BaseModel):
    employee: Employee=Field(...)
    sim: Sim=Field(...)
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
registration = Registration(employee=data["employee"],sim=data["sim"])
print(registration)

