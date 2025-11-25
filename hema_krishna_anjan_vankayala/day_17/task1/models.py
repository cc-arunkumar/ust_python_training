from pydantic import BaseModel, Field
from typing import Optional

class Task(BaseModel):
    id: Optional[int] = Field(default=1)
    title: str = Field(..., min_length=1, description="Task title")
    description: str = Field(..., description="description")
    completed: Optional[bool] = Field(default=False, description="Completion")

class LoginRequest(BaseModel):
    username: str                                      
    password: str       
    
class Token(BaseModel):
    access_token: str                                   
    token_type: str  

class User(BaseModel):
    username: str