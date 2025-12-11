# Models.py
from pydantic import BaseModel

class TaskResponse(BaseModel):
    id:int
    title:str
    description:str
    completed:bool
    
class TaskPost(BaseModel):
    title:str
    description:str
    completed:bool

class TaskModel(BaseModel):
    title:str
    description:str    

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserName(BaseModel):
    username: str