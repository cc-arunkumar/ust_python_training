from pydantic import BaseModel

# ---------- Auth ----------
class LoginRequest(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool  

class CreateTask(BaseModel):
    title: str
    description: str

class UpdateTask(BaseModel):
    title: str
    description: str
    completed: bool
