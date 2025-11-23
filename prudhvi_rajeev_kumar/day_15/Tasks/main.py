from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import re

class Employee(BaseModel):
    emp_id : int = Field(...,ge=1000,le=999999)
    name : str = Field(...,min_length=2)
    department : str = Field("General",max_length=100)
   
class Sim_model(BaseModel):
    number : str = Field(...,pattern= r"^\d{10}$")
    provider : str = "Jio"
    activation_year : int =Field(...,ge=2020,le=2025)
    
class Registration(BaseModel):
    employee : Employee
    sim : Sim_model
    
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

emp= Employee(**data["employee"])
s = Sim_model(**data["sim"])
print(emp)
print(s)
