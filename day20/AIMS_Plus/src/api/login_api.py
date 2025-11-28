from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.auth.jwt_auth import create_token

# Create a router for login-related endpoints
# Prefix "/login" means all routes here will start with /login
# Tag "Login" helps organize endpoints in API docs (Swagger UI)
login_router = APIRouter(prefix="/login", tags=["Login"])


# -----------------------------
# Pydantic model for Login data
# -----------------------------
class Login(BaseModel):
    """
    Defines the structure of login request data.
    Ensures that both username and password are provided as strings.
    """
    username: str
    password: str


# -----------------------------
# POST endpoint: Simple login
# -----------------------------
@login_router.post("/")
def login_user(data: Login):
    """
    A simple login endpoint without database integration.
    - Accepts username and password in the request body.
    - If credentials match hardcoded values, generates a JWT token.
    - Otherwise, raises HTTP 401 Unauthorized error.
    """

    # Hardcoded check for demo purposes
    if data.username == "admin" and data.password == "password123":
        # Generate JWT token with payload containing username
        token = create_token({"username": data.username})
        return {"access_token": token}  # Return token to client

    # If credentials don't match, raise Unauthorized error
    raise HTTPException(status_code=401, detail="Invalid username or password")
