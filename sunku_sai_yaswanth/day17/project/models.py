from pydantic import BaseModel,Field
from typing import Optional

class Task(BaseModel):
    title:str
    description:str
    completed:bool=False
    
    class Config:
        orm_mode=True

class TaskInResponse(Task):
    id:int
    
class TaskCreate(Task):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    
class LoginRequest(BaseModel):
    username: str
    password: str