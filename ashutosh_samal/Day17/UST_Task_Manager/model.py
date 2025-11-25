from pydantic import BaseModel, Field
from typing import Optional

class Task(BaseModel):
    id : Optional[int]=None
    title : str
    description : str
    completed : bool = "false"

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str

tasks = []
task_id = 1