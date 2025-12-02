from pydantic import BaseModel
# Request body model for login endpoint
class LoginRequest(BaseModel):
    username: str
    password: str

# Response model for token
class Token(BaseModel):
    access_token: str
    token_type: str

# User model (used for protected endpoints)
class User(BaseModel):
    username: str

