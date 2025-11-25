
from pydantic import BaseModel
from typing import Optional, List

DEMO_USERNAME = "demo"
DEMO_PASSWORD = "demo"

tasks: List[dict] = [
    {
        "id": 1,
        "title": "Pay electricity bill",
        "description": "Pay the November electricity bill for home",
        "is_done": False,
        "owner": "demo",
    },
    {
        "id": 2,
        "title": "Buy groceries",
        "description": "Milk, eggs, rice, vegetables",
        "is_done": False,
        "owner": "demo",
    },
]

next_task_id: int = 3


class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pending" 


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_done: Optional[bool] = None


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_done: bool = False
    owner: str
