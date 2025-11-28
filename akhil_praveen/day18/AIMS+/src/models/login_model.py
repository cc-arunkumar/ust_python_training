from pydantic import BaseModel

# Pydantic model for login request (username and password)
class LoginRequest(BaseModel):
    username: str
    password: str

# Pydantic model for JWT token response (access_token and token_type)
class Token(BaseModel):
    access_token: str
    token_type: str

# Pydantic model for the user (username)
class User(BaseModel):
    username: str