from pydantic import BaseModel

class User(BaseModel):
    username : str

class Token(BaseModel):
    token : str
    token_type : str

class LoginRequest(BaseModel):
    username : str
    password : str