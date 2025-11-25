# ---------------- IMPORTS ----------------
from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from models import LoginRequest, Token, User

# ---------------- CONFIGURATION ----------------
SECRET_KEY = "UST-TaskTracker-Secret"   # Secret key for JWT signing
ALGORITHM = "HS256"                     # Algorithm used for JWT encoding/decoding
ACCESS_TOKEN_EXPIRE_MINUTES = 30        # Token expiration time in minutes

# ---------------- DEMO USERS ----------------
# In-memory user list (replace with database in production)
users = [
    User(username="rahul", password="password123")
]

# ---------------- TOKEN CREATION ----------------
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    """
    Create a JWT access token for a given subject (username).
    - subject: username of the authenticated user
    - expires_delta: optional expiration time (default: 15 minutes)
    """
    to_encode = {"sub": subject}   # Payload with subject (username)
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})   # Add expiration claim
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# ✅ Example Output:
# "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." (JWT token string)

# ---------------- SECURITY SCHEME ----------------
# HTTP Bearer authentication (expects "Authorization: Bearer <token>")
security = HTTPBearer()

# ---------------- CURRENT USER VALIDATION ----------------
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Validate JWT token and return the current authenticated user.
    - credentials: Authorization header containing Bearer token
    """
    token = credentials.credentials
    try:
        # Decode JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # Raise error if token is invalid or expired
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    # Extract username from payload
    username = payload.get("sub")
    for user in users:
        if user.username == username:
            return user

    # Raise error if user not found
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )

# ✅ Example Output (Valid Token):
# {
#   "username": "rahul",
#   "password": "password123"
# }
#
# ❌ Example Output (Invalid/Expired Token):
# {
#   "detail": "Invalid or expired token"
# }
#
# ❌ Example Output (User Not Found):
# {
#   "detail": "Could not validate credentials"
# }
