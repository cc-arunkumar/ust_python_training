from pydantic import BaseModel,Field
from typing import List

#Login 
class LoginRequest(BaseModel):
    username: str
    password: str

#Token
class Token(BaseModel):
    access_token: str
    token_type: str

#User
class User(BaseModel):
    username: str

#Task
class Task(BaseModel):
    id : int = Field(...,gt=0)
    title : str = Field(...)
    description : str = Field(...)
    completed : bool = Field(default=False)

task_list : List[Task] = []

class CreateTask(BaseModel):
    title : str = Field(...)
    description : str = Field(...)
    completed : bool = Field(default=False)


