from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from typing import Optional
from datetime import datetime, timedelta, timezone
from ..models.user_model import User
from dotenv import load_dotenv
import os
 
# Load environment variables from .env file
load_dotenv()
 
# Secret key and algorithm used for JWT encoding/decoding
SECRECT_KEY = os.getenv("SECRECT_KEY")
ALGORITHM = os.getenv("ALGORITHM")
 
# Expected username for validation
USERNAME = os.getenv("USER_NAME")
 
 
# -------------------- JWT Token Creation --------------------
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    """
    Create a JWT access token with subject (username) and expiration time.
    Default expiration is 15 minutes if not provided.
    """
    to_encode = {"sub": subject}
    if expires_delta:
        expires = datetime.now(timezone.utc) + expires_delta
    else:
        expires = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expires})
 
    # Encode payload into JWT using secret key and algorithm
    encoded = jwt.encode(to_encode, SECRECT_KEY, algorithm=ALGORITHM)
    return encoded
 
 
# -------------------- Security Dependency --------------------
# HTTPBearer enforces Authorization header with Bearer token
security = HTTPBearer()
 
 
# -------------------- Current User Retrieval --------------------
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Validate JWT token from Authorization header and return current user.
    Raises HTTP 401 if token is invalid/expired or user not found.
    """
    token = credentials.credentials
    try:
        # Decode JWT token using secret key and algorithm
        payload = jwt.decode(token, SECRECT_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
 
    # Extract username from token payload
    username = payload.get("sub")
    if username != USERNAME:
        raise HTTPException(status_code=401, detail="User not found")
 
    # Return validated user object
    return User(username=username)
 
