#import libraries
from typing import List, Optional
from pydantic import BaseModel,Field


#Employee Details
class Employee(BaseModel):
    emp_id : int = Field(...,ge=1000,le=999999,description="Employee Id not valid")
    name: str = Field(...,min_length=2,description="name should be minimum of length 2")
    department : Optional[str] = Field(default="General", description="Department name")

#Sim Card details
class Sim(BaseModel):
    number : str = Field(...,pattern=r"^\d{10}$",description="Must be exactly 10 digits")
    provider : str = Field(default="Jio", description="Department name")
    activation_year : int = Field(...,ge=2000,le=2025,description="Year Must be from 2020 to 2025")

class Registration(BaseModel):
    employee : Employee 
    sim : Sim 


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
data = {
 "employee": {
 "emp_id": 12345,
 "name": "Asha"
 },
 "sim": {
 "number": "9876543210",
 "activation_year": 2023
 }
}

emp=Employee(**data["employee"])
s=Sim(**data["sim"])
reg=Registration(**data)
print(reg)
print(emp)
print(s)

#Sample Output 
# emp_id=12345 name='Asha' department='Engineering'
# number='9876543210' provider='Airtel' activation_year=2023
# employee=Employee(emp_id=12345, name='Asha', department='Engineering') sim=Sim(number='9876543210', provider='Airtel', activation_year=2023)

# employee=Employee(emp_id=12345, name='Asha', department='General') sim=Sim(number='9876543210', provider='Jio', activation_year=2023)     
# emp_id=12345 name='Asha' department='General'

# number='9876543210' provider='Jio' activation_year=2023
