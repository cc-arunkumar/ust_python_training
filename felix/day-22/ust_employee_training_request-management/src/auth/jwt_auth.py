from jose import jwt, JWTError
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException, status
import os
from dotenv import load_dotenv
from datetime import timedelta, timezone, datetime
from ..models.user_model import User

# Load environment variables from .env file
load_dotenv()
USER_NAME = os.getenv("USER_NAME")   # Expected username stored in environment variables
SECRET_KEY = os.getenv("SECRET_KEY") # Secret key used for JWT encoding/decoding
ALGORITHM = "HS256"                  # Algorithm used for JWT signing

def create_asset_token(subject: str):
    """
    Generate a JWT access token for a given subject (username).
    - Includes 'sub' claim for subject identification.
    - Includes 'exp' claim for token expiration (15 minutes from now).
    """
    # Payload with subject claim
    to_encode = {"sub": subject}
    # Add expiration time to payload
    to_encode.update({"exp": datetime.now(timezone.utc) + timedelta(minutes=15)})
    # Encode payload into JWT using secret key and algorithm
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

# HTTP Bearer authentication scheme for token extraction
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Dependency function to retrieve the current authenticated user.
    - Extracts JWT token from Authorization header.
    - Decodes and validates token using SECRET_KEY and ALGORITHM.
    - Ensures 'sub' claim matches expected USER_NAME.
    - Returns a User model instance if validation succeeds.
    """
    # Extract raw token string from credentials
    token = credentials.credentials
    try:
        # Decode JWT token and validate signature/expiration
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except JWTError:
        # Raise 401 Unauthorized if token is invalid or expired
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    # Retrieve username from token payload
    username = payload.get("sub")

    # Validate username against expected environment variable
    if username != USER_NAME:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    # Return authenticated user object
    return User(username=username)