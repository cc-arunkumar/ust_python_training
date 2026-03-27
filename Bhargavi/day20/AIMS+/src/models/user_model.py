# src/models/user_model.py

from pydantic import BaseModel

class User(BaseModel):
    username: str
