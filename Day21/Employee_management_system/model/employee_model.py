from pydantic import BaseModel,Field,EmailStr,field_validator
from typing import Optional
from datetime import date,datetime
import re

date_pattern = r"^\d{4}-\d{2}-\d{2}$"


class EmployeeModel(BaseModel):
    first_name: str = Field(...,max_length=50)
    last_name: str = Field(...,max_length=50)
    email:EmailStr
    position:Optional[str] = Field(...,max_length=50)
    salary:float = Field(...,ge=1)
    hire_date:date
    
    @field_validator('first_name')
    def validate_first_name(cls,v):
        if not re.match('^[A-Za-z]$',v):
            raise ValueError("Enter valid First Name")
        return v.strip()
    
    @field_validator('last_name')
    def validate_last_name(cls,v):
        if not re.match('^[A-Za-z\s-]+$',v):
            raise ValueError("Enter valid first name")
        return v.strip()
    
    @field_validator('email')
    def validate_email(cls,v):
        if not re.match('^[\w\.\+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$',v):
            raise ValueError("Enter valid Email")
        return v
    
    @field_validator('position')
    def validate_position(cls,v):
        if not re.match('^[A-Za-z0-9]+$',v):
            raise ValueError("Enter valid position")
        return v
    
    @field_validator('salary')
    def validate_salary(cls,v):
        if v<1:
            raise ValueError("Enter valid phone number")
        return v

    @field_validator('hire_date')
    def validate_hire_date(cls,v):
        if not re.match(date_pattern,v):
            raise ValueError("Date format is wrong")
        try:
            date_obj = datetime.strptime(v,"%y-%m-%d")
            if date_obj.date() > datetime.today().date():
                raise ValueError("Future date cannot accepted")
        except ValueError:
            raise("Enter valid date")
        return v
        