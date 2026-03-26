from pydantic import BaseModel, Field,field_validator,EmailStr
from datetime import date,datetime
from typing import Optional
import re


class EmployeeModel(BaseModel):
    first_name:str=Field(...,max_length=50)
    last_name:str=Field(...,max_length=50)
    email:EmailStr=Field(...,max_length=100)
    position:Optional[str]=Field(...,max_length=50)
    salary:float=Field(...,ge=1)
    hire_date:date
    
    @field_validator('first_name')
    def validate_first_name(cls,v):
        if not re.match('^[A-Za-z]+$',v):
            raise ValueError("Please Enter a Valid Form")
        return v.strip()
    
    @field_validator('last_name')
    def validate_last_name(cls,v):
        if not re.match('^[A-Za-z\s-]+$',v):
            
            raise ValueError("Please Enter a valid form of last name")
        return v.strip()
        
    
    @field_validator('email')
    def validate_email(cls,v):
        if not re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',v):
            raise ValueError("Please Enter a valid form of email")
        return v
    
    @field_validator('position')
    def validate_position(cls,v):
        if not re.match('^[A-Za-z0-9\s\-]+$', v):
            raise ValueError("Please enter a valid form of Position")
        return v
    
    @field_validator('salary')
    def validate_salary(cls,v):
        if v <1 :
            raise ValueError("Please ENter a valid salary")
        return v
    
    @field_validator('hire_date')
    def validate_hire_date(cls, v):
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(v)):
            raise ValueError('Hire Date must be in the format YYYY-MM-DD')
        if v > datetime.today().date():
            raise ValueError('Hire Date cannot be a future date')       
        return v
