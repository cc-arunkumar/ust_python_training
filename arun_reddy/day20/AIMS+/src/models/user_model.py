from pydantic import BaseModel
class LoginRequest(BaseModel):
    username: str
    password: str
    
# Pydantic model for the token response
class Token(BaseModel):
    access_token: str
    token_type: str

# Pydantic model for the current logged-in user
class User(BaseModel):
    username: str