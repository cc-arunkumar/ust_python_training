from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.auth.jwt_auth import create_token

# Create a router for login-related API endpoints
login_router = APIRouter(prefix="/login", tags=["Login"])

# Define the data model for login credentials
class Login(BaseModel):
    username: str
    password: str

# POST endpoint to handle login and token generation
@login_router.post("/")
def login_user(data: Login):
    # Check if username and password are correct
    if data.username == "admin" and data.password == "password123":
        # Generate JWT token for valid login
        token = create_token({"username": data.username})
        return {"access_token": token}

    # Return error if login is invalid
    raise HTTPException(status_code=401, detail="Invalid username or password")
