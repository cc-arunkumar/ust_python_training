# UST Employee Telecom Device
# Registration
# Scenario
# UST provides company SIM cards to employees for official communication.
# When a SIM is issued, an employee must register their details and SIM details.
# You will create Pydantic models to validate the registration input.
# Model Requirements
# �� Employee Model
# Field Type Required Rules
# emp_id int YES ge=1000 , le=999999
# name str YES min_length=2
# department str NO default: "General"
# �� SIM Model
# Field Type Required Rules
# number str YES must be exactly 10 digits
# provider str NO default: "Jio"
# activation_year int YES ge=2020 , le=2025
# Regex for SIM number:
# pattern=r"^\d{10}$"
# �� Registration Model
# (Nesting practice — model inside model)
# UST Employee Telecom Device Registration 1
# Field Type Required
# employee Employee YES
# sim SIM YES
# �� Example of VALID input dictionary
# Students must test with this:
# data = {
#  "employee": {
#  "emp_id": 12345,
#  "name": "Asha",
#  "department": "Engineering"
#  },
#  "sim": {
#  "number": "9876543210",
#  "provider": "Airtel",
#  "activation_year": 2023
#  }
# }
# Expected: model should create successfully and print the object.
# Example of OPTIONAL fields
# Candidates must test with this too (provider + department missing):
# data = {
#  "employee": {
#  "emp_id": 12345,
#  "name": "Asha"
#  },
#  "sim": {
#  "number": "9876543210",
#  "activation_year": 2023
# UST Employee Telecom Device Registration 2
#  }
# }
# Expected:
# department should default to "General"
# provider should default to "Jio"
# Validation error test cases
# Each of these MUST show a ValidationError:
# Wrong Input Reason
# emp_id = 999 ge rule violated
# name = "A" min_length violated
# number = "12345" 10 digit violated
# activation_year = 2019 ge rule violated
# activation_year = 2030 le rule violated
# Students must try each test separately and observe error messages.
# Expected output examples
# Success case
# employee=Employee(emp_id=12345, name='Asha', department='Engineerin
# g')
# sim=SIM(number='9876543210', provider='Airtel', activation_year=2023)
# Default assignment case
# When department and provider missing:
# UST Employee Telecom Device Registration 3
# department='General'
# provider='Jio'
# Failure case examples
# Error message should mention:
# missing field, or
# minimum length, or
# pattern mismatch, or
# numeric constraints
# Deliverables from participants
# They need to submit:
# 1. All 3 model class definitions
# 2. Output of valid registration object printed
# 3. Output of default-field test printed
# 4. Validation error outputs for each failed case
# # UST Employee Telecom Device Registration 4


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Optional,List

app=FastAPI(tritle="UST Employee telecom Device ")

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
