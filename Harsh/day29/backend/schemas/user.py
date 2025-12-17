from pydantic import BaseModel
from typing import List

class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    role: str
    token_type: str = "bearer"


class CurrentUser(BaseModel):
    user_id: int
    emp_id: int
    role: List[str]