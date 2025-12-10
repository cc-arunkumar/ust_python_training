from enum import Enum
from pydantic import Field,field_validator,model_validator,BaseModel
from typing import List,Optional
from datetime import date,datetime


class Status(str,Enum):
    pending="PENDING"
    accepted="ACCEPTED"
    rejected="REJECTED"
    
    
class TrackingRequest(BaseModel):
    employee_id:str=Field(...,pattern=r"^UST\d+$")
    employee_name:str=Field(...,pattern=r"^[A-Za-z ]+$")
    training_title:str=Field(...)
    training_description:str=Field(...)
    requested_date:date=Field(...)
    status:Status=Field(...)
    manager_id:str=Field(...,pattern=r"^UST\d+$")
    last_updated:datetime=Field(...)
    @field_validator("requested_date")
    def val_date(cls,v):
        if v> date.today():
            raise ValueError("Requested date ntot valid !!")
        return v



#===model to validate logins======

class LoginRequest(BaseModel):
    """Model for login request body"""
    username: str
    password: str

class Token(BaseModel):
    """Response model for returned JWT token"""
    access_token: str
    token_type: str

class User(BaseModel):
    """Model representing a user"""
    username: str
