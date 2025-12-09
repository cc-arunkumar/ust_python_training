from pydantic import BaseModel,field_validator,Field
from datetime import date,datetime
from enum import Enum
from typing import Optional
import re

class Status(str,Enum):
    PENDING="PENDING"
    APPROVED="APPROVED"
    REJECTED="REJECTED" 
       
class LoginRequest(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class User(BaseModel):
    username:str
    
    
class EntityRequest(BaseModel):
    id: Optional[int]=None
    employee_id:str
    employee_name:str
    training_title:str=Field(...,min_length=5)
    training_description:str=Field(...,min_length=10)
    requested_date:date
    status:Status
    manager_id:str
    last_updated:Optional[datetime]=None

    
    @field_validator("employee_id")
    def val_emp(cls,v):
        if not re.match(r'UST-\d+$',v):
            raise ValueError("Employee id does not match")
        return v
    
    @field_validator("employee_name")
    def val_name(cls,v):
        if not v.strip():
            raise ValueError("Employee name cannot be empty")
        if not re.match(r'^[^0-9]*$',v):
            raise ValueError("Employee name should not have numbers")
        return v

    @field_validator("manager_id")
    def val_man(cls,v):
        if not re.match(r'UST-\d+$',v):
            raise ValueError("Manager id does not match")
        return v

        
    @field_validator("requested_date")
    def req_date(cls,v):
        if v>date.today():
            raise ValueError("Requested date cannot be a future date")
        return v

            
        
                    