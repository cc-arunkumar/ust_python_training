from pydantic import BaseModel
from typing import Literal, List

class UserModel(BaseModel):
    emp_id: int
    password: str
    role: List[str]
    status: Literal["active","inactive"] = "active"
  
class UserUpdate(BaseModel):
    password: str
    role: List[str]
    status: Literal["active","inactive"] = "active"
    
class UpdateRole(BaseModel):
    role: List[str]
    
class LoginModel(BaseModel):
    emp_id: int
    password: str
    
class Token(BaseModel):
    token: str
    token_type: str