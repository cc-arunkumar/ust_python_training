# Import FastAPI utilities for routing and exception handling
from fastapi import HTTPException, status, APIRouter
# Import timedelta to handle token expiration duration
from datetime import timedelta

# Import authentication-related models, constants, and functions
from src.auth.jwt_auth import (
    Token,                      # Response model for JWT token
    LoginRequest,               # Request model for login payload (username & password)
    DEMO_PASSWORD,              # Demo password (for testing purposes only)
    DEMO_USERNAME,              # Demo username (for testing purposes only)
    ACCESS_TOKEN_EXPIRE_MINUTES,# Token expiration time in minutes
    create_access_token          # Function to generate JWT access tokens
)

# Define a router with prefix "/jwt" for all JWT-related endpoints
jwt_router = APIRouter(prefix="/jwt")

@jwt_router.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Login endpoint:
    - Validates provided username and password.
    - If valid, generates and returns a JWT access token.
    - If invalid, raises HTTP 401 Unauthorized.
    """

    # Check if provided credentials match demo credentials
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        # Raise 401 Unauthorized if credentials are incorrect
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    # Set token expiration time using timedelta
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Generate JWT token with subject set to the username
    token = create_access_token(subject=data.username, expires_delta=expires)

    # Return token in the expected response format
    return Token(access_token=token, token_type="bearer")
