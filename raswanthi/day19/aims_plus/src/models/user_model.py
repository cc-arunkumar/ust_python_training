from pydantic import BaseModel
 
# Model representing a user with a username
class User(BaseModel):
    username: str
 
# Model representing an authentication token and its type
class Token(BaseModel):
    token: str
    token_type: str
 
# Model representing login request payload with username and password
class LoginRequest(BaseModel):
    username: str
    password: str