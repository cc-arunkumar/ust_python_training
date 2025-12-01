from fastapi import APIRouter, HTTPException, status
from ..models.user_model import UserModel
from ..models.user_model import Token
from ..auth.jwt_auth import create_asset_token
import os
from dotenv import load_dotenv

# Create a router instance for login-related endpoints
login_router = APIRouter(prefix="/login")

# Load environment variables from a .env file
load_dotenv()
USER_NAME = os.getenv("USER_NAME")   # Expected username stored in environment variables
PASSWORD = os.getenv("PASSWORD")     # Expected password stored in environment variables

@login_router.post("", response_model=Token)
def login(user: UserModel):
    """
    Login endpoint that validates user credentials and returns a JWT token.
    - Accepts a UserModel containing username and password.
    - Compares credentials against environment variables.
    - Returns a bearer token if authentication succeeds.
    """

    # Extract username and password from the request body
    username = user.username
    password = user.password

    # Validate credentials against environment variables
    if username != USER_NAME or password != PASSWORD:
        # Raise HTTP 401 Unauthorized if credentials are invalid
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    # Generate JWT token for the authenticated user
    token = create_asset_token(username)

    # Return token response in the expected format
    return Token(token=token, token_type="bearer")