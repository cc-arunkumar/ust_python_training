from pydantic import BaseModel
from typing import Literal

class UserSchema(BaseModel):
    emp_id: int
    role: Literal["admin", "manager", "developer"]
    status: Literal["active", "inactive"]="inactive"

class LoginRequest(BaseModel):
    emp_id: int
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
