# Import BaseModel from Pydantic to define data validation and serialization models
from pydantic import BaseModel

# Model for login request payload
class LoginRequest(BaseModel):
    username: str   # Username provided by the client
    password: str   # Password provided by the client

# Model for JWT token response
class Token(BaseModel):
    access_token: str  # The actual JWT access token string
    token_type: str    # Token type (usually "bearer")

# Model representing a user entity
class User(BaseModel):
    username: str   # Username of the user
