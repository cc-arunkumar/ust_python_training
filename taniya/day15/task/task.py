from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field

app = FastAPI(title="UST Employee Telecom Device Registration")

class Employee(BaseModel):
    emp_id:int=Field(...,ge=1000,le=999999,description="emp_id should be between 1000 and 9999")
    name:str=Field(...,min_length=2,description="name length should me minimum 2")
    department:str=Field(default="General")

class SIM():
    number:str=Field(...,re=r"^\d{10}$")
    provider:str=Field(default="Jio")
    activation_year:int=Field(...,ge=2020,le=2025,description="year should be between 2020 to 2025")

class Registration():
    employee:Employee=Field(...)
    sim:SIM=Field(...)
 
@app.post("/register")
def register_device():
    print("\n Success Case:")
    data = {
        "employee": {"emp_id": 12345,"name": "Asha","department": "Engineering"},
        "sim": {"number": "9876543210","provider": "Airtel","activation_year": 2023}
    }
    reg1=Registration(**data)
    print(reg1)
    
    print("\nDefault Assignment Case:")
    data_defaults={
         "employee": {"emp_id": 12345,"name": "Asha","department": "Engineering"},
        "sim": {"number": "9876543210","provider": "Airtel","activation_year": 2023}
    }
    reg2= Registration(**data_defaults)
    print(reg2)
    
    print("\nValidation Error Cases:")
    test_cases=[{
            "employee": {"emp_id": 999, "name": "Asha", "department": "Engineering"},
            "sim": {"number": "9876543210", "provider": "Airtel", "activation_year": 2023}
        },
        {
            "employee": {"emp_id": 1000000, "name": "Asha", "department": "Engineering"},
            "sim": {"number": "9876543210", "provider": "Airtel", "activation_year": 2023}
        },
        {
            "employee": {"emp_id": 12345, "name": "A", "department": "Engineering"},
            "sim": {"number": "9876543210", "provider": "Airtel", "activation_year": 2023}
        },
        {
            "employee": {"emp_id": 12345, "name": "Asha", "department": "Engineering"},
            "sim": {"number": "12345", "provider": "Airtel", "activation_year": 2023}
        },
        {
            "employee": {"emp_id": 12345, "name": "Asha", "department": "Engineering"},
            "sim": {"number": "98765ABCD1", "provider": "Airtel", "activation_year": 2023}
        },
        {
            "employee": {"emp_id": 12345, "name": "Asha", "department": "Engineering"},
            "sim": {"number": "9876543210", "provider": "Airtel", "activation_year": 2019}
        }]
    for case in test_cases:
        try:
            reg = Registration(**case)
            print(reg)
        except Exception as e:
            print(f"Error: {e}")
