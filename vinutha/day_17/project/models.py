from pydantic import BaseModel

# Task creation request body
class TaskIn(BaseModel):
    title: str
    description: str
    completed: bool = False

# Task response model
class Task(TaskIn):
    id: int

# User model for login request
class User(BaseModel):
    username: str

# Login Request model
class LoginRequest(BaseModel):
    username: str
    password: str

# Token response model
class Token(BaseModel):
    access_token: str
    token_type: str
