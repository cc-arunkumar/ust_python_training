from pydantic import BaseModel
from typing import Optional
from models.user import UserReqRes


class LoginRequest(BaseModel):
    e_id: int
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AuthResponse(Token):
    user: Optional[UserReqRes] = None
