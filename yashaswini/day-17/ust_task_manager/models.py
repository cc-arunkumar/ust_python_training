from pydantic import BaseModel

# Login request model
class LoginRequest(BaseModel):
    username: str
    password: str

# Task input model
class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

# Task response model (adds id)
class TaskResponse(Task):
    id: int
