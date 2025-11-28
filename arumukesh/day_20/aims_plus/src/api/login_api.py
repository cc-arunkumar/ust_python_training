from fastapi import Depends, APIRouter, HTTPException, status
from datetime import timedelta

# Import models and authentication utilities
from src.model.model_maintenance_log import MaintenanceLog
from src.auth.jwt_authentication import (
    get_current_user,
    User,
    DEMO_PASSWORD,
    DEMO_USERNAME,
    LoginRequest,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token
)
from src.model.model_login import User, LoginRequest, Token


# APIRouter for authentication related endpoints
router = APIRouter(prefix="/jwt")


@router.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Authenticates a user and generates a JWT access token.

    Args:
        data (LoginRequest): Contains the username and password entered by the user.

    Returns:
        Token: Contains the generated JWT and token type.

    Raises:
        HTTPException: If the credentials do not match the stored demo credentials.
    """

    # Validate username and password against stored credentials
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Set expiration time for JWT token
    expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    
    # Create the JWT access token
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")
