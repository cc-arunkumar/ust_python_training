from fastapi import FastAPI
from pydantic import BaseModel,validator,Field
from typing import Optional

app=FastAPI()
class Employee(BaseModel):
    empid: int = Field(..., alias="emp_id", ge=1000, le=99999)
    name: str = Field(..., min_length=2)
    department: Optional[str] = Field(default="General")
    

class Sim(BaseModel):
    number:str=Field(...,pattern=r"^\d{10}$",min_length=10)
    provider:Optional[str]=Field(default="Jio")
    activation_year:int=Field(...,ge=2020,le=2025)
    
class Registration(BaseModel):
    employee:Employee
    sim:Sim 
    
data = {
 "employee": {
 "emp_id": 12345,
 "name": "Asha",
 "department": "Engineering"
 },
 "sim": {
 "number": "3456789072",
 "provider": "Airtel",
 "activation_year": 2021
 }
}
# data = {
#  "employee": {
#  "emp_id": 12345,
#  "name": "Asha"
#  },
#  "sim": {
#  "number": "9876543210",
#  "activation_year": 2023
#  }
# }


registration=Registration(employee=data["employee"],sim=data["sim"])
print(registration.__dict__)




#sample execution
# {'employee': Employee(empid=12345, name='Asha', department='Engineering'), 'sim': Sim(number='9876543210', provider='Airtel', activation_year=2023)}
# {'employee': Employee(empid=12345, name='Asha', department='General'), 'sim': Sim(number='9876543210', provider='Jio', activation_year=2023)}


#ERROR VAlidation
# employee.emp_id
# Input should be greater than or equal to 1000 [type=greater_than_equal, input_value=999, input_type=int]

# employee.name
#  String should have at least 2 characters [type=string_too_short, input_value='A', input_type=str]

# sim.number
#  String should have at least 10 characters [type=string_too_short, input_value='12345', input_type=str]

# sim.activation_year
# Input should be greater than or equal to 2020 [type=greater_than_equal, input_value=2019, input_type=int]


# sim.activation_year
#  Input should be less than or equal to 2025 [type=less_than_equal, input_value=2030, input_type=int]