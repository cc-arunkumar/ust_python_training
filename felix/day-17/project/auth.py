from typing import Optional
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, status, Depends
from pydantic import BaseModel,Field
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

# -----------------------------
# JWT CONFIGURATION
# -----------------------------
SECRET_KEY = "UST-TaskTracker-Secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token validity duration


# -----------------------------
# REQUEST/RESPONSE MODELS
# -----------------------------
class LoginRequest(BaseModel):
    """Schema for user login"""
    username: str = Field(..., description="username is missing")
    password: str = Field(..., description="password is missing")


class Token(BaseModel):
    """Response model for generated JWT token"""
    access_token: str
    token_type: str


class User(BaseModel):
    """Represents authenticated user"""
    username: str

# Hardcoded user for demo purposes
users = {
    "felix": {
        "username": "felix",
        "password": "password123"
    }
}

# -----------------------------
# TOKEN CREATION FUNCTION
# -----------------------------
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    """
    Generates a JWT access token.
    :param subject: Username or user identifier
    :param expires_delta: Optional token expiry duration
    """
    to_encode = {"sub": subject}

    # Set expiration time
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})

    # Encode JWT token
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded


# Security scheme for authorization headers
security = HTTPBearer()


# -----------------------------
# AUTHENTICATION DEPENDENCY
# -----------------------------
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Validates the JWT token and returns the authenticated user.
    Raises 401 errors for invalid/expired tokens.
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    username = payload.get("sub")

    # Validate user exists
    if username != users["felix"]["username"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return User(username=username)

