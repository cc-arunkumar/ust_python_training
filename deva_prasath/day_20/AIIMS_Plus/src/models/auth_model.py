from pydantic import BaseModel  # Import Pydantic for model validation

class LoginRequest(BaseModel):
    username: str
    password: str
 
class Token(BaseModel):
    access_token: str
    token_type: str
 
class User(BaseModel):
    username: str