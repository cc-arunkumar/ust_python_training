from fastapi import HTTPException, Depends,APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from typing import Optional
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
import os

from pydantic import BaseModel

login_router = APIRouter(prefix="/auth")

# Model representing a user with a username
class User(BaseModel):
    username: str

# Model representing an authentication token and its type
class Token(BaseModel):
    token: str
    token_type: str

# Model representing login request payload with username and password
class LoginRequest(BaseModel):
    username: str
    password: str

# Load environment variables from .env file
load_dotenv()

# Secret key and algorithm used for JWT encoding/decoding
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# Expected username for validation
USERNAME = os.getenv("USER_NAME")

expire = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


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
    encoded = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
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
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    # Extract username from token payload
    username = payload.get("sub")
    if username != USERNAME:
        raise HTTPException(status_code=401, detail="User not found")

    # Return validated user object
    return User(username=username)


@login_router.post("/login", response_model=Token)
def login(user: LoginRequest):
    """
    Authenticate user with username and password.
    If valid, generate and return a JWT access token.
    """
    try:
        # Validate credentials against environment variables
        if (user.username != os.getenv("USER_NAME") or user.password != os.getenv("PASSWORD")):
            raise HTTPException(status_code=404, detail="Invalid username or password")

        # Set token expiration time
        expires = timedelta(minutes=int(expire))

        # Generate JWT token
        token = create_access_token(user.username, expires)

        # Return token response
        return Token(token=token, token_type="bearer")

    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=404, detail=str(e))