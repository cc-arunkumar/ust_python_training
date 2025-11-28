from datetime import timedelta
from fastapi import FastAPI, HTTPException, status, APIRouter
from ..auth.jwt_auth import create_access_token
import os
from dotenv import load_dotenv
from ..models.user_model import Token, LoginRequest

# Load environment variables from a .env file
# This allows sensitive data (like demo credentials) to be stored securely outside the codebase
load_dotenv()

# Define a router for login-related endpoints with a prefix "/login"
login_router = APIRouter(prefix="/login")

# Retrieve demo credentials from environment variables
# These should be set in the .env file for testing/demo purposes
DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")


# Retrieve token expiration time (in minutes) from environment variables
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


@login_router.post("", response_model=Token)
def login(data: LoginRequest):
    """
    Login endpoint that validates user credentials against demo values
    and generates a JWT access token if authentication succeeds.
    
    Args:
        data (LoginRequest): Object containing username and password.
    
    Returns:
        Token: JWT access token with type "bearer".
    
    Raises:
        HTTPException: If credentials are invalid, returns 401 Unauthorized.
    """

    # Validate provided credentials against demo credentials
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Username or Password"
        )

    # Set token expiration using timedelta
    expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

    # Generate JWT access token with subject as username
    token = create_access_token(subject=data.username, expires_delta=expires)

    # Return token in the expected response model format
    return Token(access_token=token, token_type="bearer")