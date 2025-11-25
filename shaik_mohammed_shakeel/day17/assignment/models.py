# Models.py
from pydantic import BaseModel
 
class Task(BaseModel):
    id:int
    title:str
    description:str
    completed:bool
 
 
class LoginRequest(BaseModel):
    username: str
    password: str
 
class Token(BaseModel):
    access_token: str
    token_type: str
 
class User(BaseModel):
    username: str