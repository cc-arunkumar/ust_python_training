# JWT utilities for creating and validating access tokens used by FastAPI routes.
# This module provides a token creation helper and a dependency to extract the current user
# from the HTTP Bearer authorization header.

from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from ..models.user_model import User
import os
from dotenv import load_dotenv

# Load environment variables from a .env file so SECRET_KEY and ALGORITHM are available.
load_dotenv()

# Secret and algorithm used for signing and verifying JWTs.
SECRET_KEY = os.getenv("SECRET_KEY") 
ALGORITHM = os.getenv("ALGORITHM")
# A demo username used to validate tokens in this simple auth setup.
DEMO_USERNAME = os.getenv("DEMO_USERNAME")

def create_access_token(subject:str,expires_delta : Optional[timedelta] = None):
    # Prepare payload with the subject (usually username or user id)
    to_encode = {"sub":subject}
    
    # Calculate token expiration time. If expires_delta is provided, add to current UTC time,
    # otherwise default to 15 minutes.
    if expires_delta:
        expires_delta = datetime.now(timezone.utc) + expires_delta
    else:
        expires_delta = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    # Add expiration claim to payload and encode the JWT using configured SECRET_KEY and ALGORITHM.
    to_encode.update({"exp":expires_delta})
    encoded = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    
    return encoded

# FastAPI security dependency that expects an Authorization: Bearer <token> header.
security = HTTPBearer()

def get_current_user(credentials : HTTPAuthorizationCredentials = Depends(security)) -> User:
    # Extract raw token string from HTTPAuthorizationCredentials provided by HTTPBearer.
    token = credentials.credentials
    try:
        # Decode and validate the JWT. This will raise JWTError on invalid or expired tokens.
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except JWTError:
        # Convert JWT errors into a 401 response for clients.
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    # Extract the subject (username) from token payload.
    username = payload.get("sub")
    
    # Basic check to ensure token subject matches a known demo username.
    # In a real application replace this with lookup in users store / database.
    if username!=DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    # Return a User model instance representing the authenticated user.
    return User(username=username)