from pydantic import BaseModel
from typing import List

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str

class TaskModel(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False
