from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from enum import Enum

class Status(str,Enum):
    pending = 'pending'
    approved = 'approved'
    rejected = 'rejected'

class TrainingRequest(BaseModel):
    id : Optional[int]
    employee_id : str  = Field(...,pattern=r'^UST\d+$')
    employee_name : str = Field(...,pattern=r'^[A-Za-z ]+$')
    training_title : str = Field(...,min_length=5)
    training_description : str = Field(...,min_length=10)
    requested_date : date = Field(lt=date.today())
    status : Status = Field(default='pending')
    manager_id : str = Field(...,pattern=r'^UST\d+$')
    last_updated : Optional[datetime] = Field(default=datetime.now())


class Token(BaseModel):
    access_token : str
    token_type : str 

class LoginRequest(BaseModel):
    username : str 
    password : str 
    
class User(BaseModel):
    username: str