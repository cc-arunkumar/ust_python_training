# ---------------- IMPORTS ----------------
from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from models import LoginRequest, Token, UserSchema
from database import fetch_all_users
from mongodb_logger import logger   # <-- Custom MongoDB logger

# ---------------- CONFIGURATION ----------------
SECRET_KEY = "UST-TaskTracker-Secret"   # Secret key for JWT signing
ALGORITHM = "HS256"                     # Algorithm used for JWT encoding/decoding
ACCESS_TOKEN_EXPIRE_MINUTES = 30        # Token expiration time in minutes


# ---------------- TOKEN CREATION ----------------
# Create a JWT access token for a given subject (user_id).
# - subject: user_id of the authenticated user (stored in "sub" claim)
# - expires_delta: optional expiration time (default: 15 minutes)
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}   # Payload with subject (user_id)
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})   # Add expiration claim
    # Log token creation event
    logger.info(f"Created access token for user_id={subject}")
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# ---------------- SECURITY SCHEME ----------------
# HTTP Bearer authentication (expects "Authorization: Bearer <token>")
security = HTTPBearer()


# ---------------- CURRENT USER VALIDATION ----------------
# Validate JWT token and return the current authenticated user.
# - credentials: Authorization header containing Bearer token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> UserSchema:
    token = credentials.credentials
    try:
        # Decode JWT token using secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # Log invalid/expired token attempt
        logger.warning("Invalid or expired JWT token provided")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    # Extract user_id from token payload
    user_id = payload.get("sub")
    users = fetch_all_users()  # Query all users from DB
    for user in users:
        if str(user.user_id) == str(user_id):
            # Log successful user validation
            logger.info(f"Authenticated user_id={user_id} successfully")
            return user

    # Log failed user validation
    logger.error(f"Failed to validate credentials for user_id={user_id}")
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )
