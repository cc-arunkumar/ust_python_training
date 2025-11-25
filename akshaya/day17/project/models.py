# models.py
from pydantic import BaseModel
from typing import Optional


class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    username: str


class Task(BaseModel):
    id:int
    title: str
    description: str
    completed:bool
