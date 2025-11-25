from jose import jwt, JWTError
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta, timezone
from typing import Optional
from models import User

SECRECT_KEY = "abcdefg"   # Used to sign JWT tokens (keep this secret in real apps!)
ALGORITHM = "HS256"       # Hashing algorithm for JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiry time
COUNT = 1

# Demo credentials (entered at runtime)
users = {
 "rahul": {
 "username": "rahul",
 "password": "password123"
 }
}

DEMO_USERNAME = users["rahul"]["username"]
DEMO_PASSWORD = users["rahul"]["password"]

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    """
    Create a JWT access token with subject (username) and expiry.
    """
    to_encode = {"sub": subject}

    # Set expiry time
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    # Encode JWT
    encoded = jwt.encode(to_encode, SECRECT_KEY, algorithm=ALGORITHM)
    return encoded

# ------------------ Security Dependency ------------------

security = HTTPBearer()  # Extracts Authorization header

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Validate JWT token and return current user.
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRECT_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    username = payload.get("sub")
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return User(username=username)