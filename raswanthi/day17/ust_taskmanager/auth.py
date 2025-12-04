from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from raswanthi.day17.ust_task_manager.ust_taskmanager.models import User

# -------------------------
# JWT Configuration
# -------------------------
SECRET_KEY = "UST-TaskTracker-Secret"   # Secret key used to sign JWTs
ALGORITHM = "HS256"                     # Algorithm used for encoding/decoding JWTs
ACCESS_TOKEN_EXPIRE_MINUTES = 30        # Token expiration time in minutes

# -------------------------
# Demo User (Hardcoded)
# -------------------------
users = {
    "rahul": {
        "username": "rahul",
        "password": "password123"
    }
}

# -------------------------
# Security Scheme
# -------------------------
# HTTPBearer ensures endpoints require "Authorization: Bearer <token>"
security = HTTPBearer()

# -------------------------
# Helper: Create JWT Token
# -------------------------
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    """
    Generate a JWT access token.
    - subject: the username (stored in 'sub' claim)
    - expires_delta: optional expiration time (defaults to ACCESS_TOKEN_EXPIRE_MINUTES)
    """
    to_encode = {"sub": subject}
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})  # Add expiration claim
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

# -------------------------
# Helper: Verify JWT Token
# -------------------------
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Decode and validate JWT token.
    - Extracts token from Authorization header.
    - Verifies signature and expiration.
    - Ensures user exists in demo users.
    - Returns a User object if valid.
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # Raised if token is invalid or expired
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    username = payload.get("sub")
    if username not in users:
        # Reject if username in token doesn't match demo user
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return User(username=username)
