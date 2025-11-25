from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int = 0
    title: str
    description: str
    completed: bool = False

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str

# In-memory storage
Tasks: List[Task] = []
ID_COUNT: int = 1
