from typing import List,Optional
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
import re


class Employee(BaseModel):
    emp_id : int = Field(...,ge=1000,le=999999,description="Employee id should be in between 1000 and 999999")
    name : str = Field(...,min_length=2,description="Length must be greater than or equal to 2")
    official_email : str = Field(...,pattern=r'^[a-zA-Z0-9._%+-]+@ust\.com$',description="Must match the pattern")
    department : Optional[str] = Field("General")
    location : Optional[str] = Field("Bangaluru")
    
class Sim(BaseModel):
    sim_number : str = Field(...,patter = r"^\d{10}$"description="Length should be exactly 10")
    provider : Optional[str] = Field("Jio")
    is_esim : Optional[bool] = Field("False") 
    activation_year : int = Field(...,ge=2020,le=2025,description="Employee id should be in between 2020 and 2025")
    
class DataPlan(BaseModel):
    name : str = Field(...,min_length=3,max_length=50,description="Name should be in between 3 and 50 inclusive")
    monthly_gb : int = Field(...,gt=0,le=5000,description="Data volume should be less than 5000gb")
    speed_mbps :  Optional[int] = Field(...,50,ge=1,le=1000,description="Speed in mps should be less than 1000")
    is_roaming_included : 
    
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