


from pydantic import BaseModel,Field
from typing import List
from fastapi import FastAPI


# Employee model with validation constraints
class Employee(BaseModel):
    emp_id:int=Field(...,ge=100,le=99999)  # emp_id should be between 100 and 99999
    name:str=Field(...,min_length=2)  # name should have a minimum length of 2 characters
    department:str="General"  # Default department is "General"


# SimModel model with validation constraints
class SimModel(BaseModel):
    number:str=Field(...,pattern=r"^\d{10}$")  # number should be a 10-digit string
    provider:str="Jio"  # Default provider is "Jio"
    activation_year:int=Field(...,ge=2020,le=2025)  # activation_year should be between 2020 and 2025


# Registration model that combines Employee and SimModel
class Registration(BaseModel):
    employee:Employee  # employee details
    sim:SimModel  # sim details
    
# Sample data for testing
data ={
 "employee": {
 "emp_id":12345,
 "name":"Asha",
 "department":"Engineering"
 },
 "sim": {
 "number": "9876543210",
 "provider": "Airtel",
 "activation_year":2023
 }
 }

# Example of creating an Employee and SimModel instance
employee=Employee(emp_id=1, name='Asha', department='Engineering')  # Create Employee instance
sim=SimModel(number='9876543210', provider='Airtel', activation_year=2023)  # Create SimModel instance
