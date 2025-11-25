from pydantic import BaseModel, Field
users = {
    "rahul": {
        "username": "rahul",
        "password": "password123"
    }
}
class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str  
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)

class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    completed: bool