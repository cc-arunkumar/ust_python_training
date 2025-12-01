from datetime import date
from pydantic import BaseModel,Field,EmailStr,model_validator
from typing import Optional

class EmployeeInfo(BaseModel):
    first_name: str=Field(...,pattern=r'^[A-Za-z -]+$',max_length=50)
    last_name: str=Field(...,pattern=r'^[A-Za-z -]+$',max_length=50)
    email: EmailStr=Field(...,max_length=100)
    position: str=Field(...,pattern=r'^[A-Za-z0-9 -]+$',max_length=50)
    salary: float
    hire_date: date
    
    @model_validator(mode="after")
    def validate_all(self):
        if self.salary is not None and self.salary <= 0:
            raise ValueError("Salary must be greater than 0")
        
        if self.hire_date > date.today():
            raise ValueError("hire_date cannot be in the future")
        return self 