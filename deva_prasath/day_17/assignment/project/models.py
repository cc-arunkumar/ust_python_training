from pydantic import BaseModel
from typing import Optional

#class Taskmodel 
class TaskModel(BaseModel):
    id: Optional[int]=None
    title: str
    description: str
    completed: Optional[bool] = False

#class Loginrequest
class LoginRequest(BaseModel):
    username: str
    password: str

#class Token
class Token(BaseModel):
    access_token: str
    token_type: str

#class User
class User(BaseModel):
    username: str
