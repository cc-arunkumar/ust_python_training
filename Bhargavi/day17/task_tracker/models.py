from pydantic import BaseModel,Field
from typing import Optional
 
class Task(BaseModel):
    title:str=Field(...,min_length=1,max_length=255)
    description:str=Field(...,min_length=1,max_length=500)
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