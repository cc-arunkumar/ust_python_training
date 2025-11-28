from fastapi import HTTPException, status, Depends, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from dotenv import load_dotenv
import os
from src.model.model_login import User,LoginRequest

# Creating a router with prefix "/jwt"
jwt_router = APIRouter(prefix="/jwt")

# Load environment variables from `.env` file
load_dotenv(os.path.join(os.path.dirname(__file__)))

# Security environment variables
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")  # Secret key used to sign JWT tokens
ALGORITHM = os.getenv("ALGORITHM")                      # Encryption algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

# Demo user credentials from env
DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")

print("Loaded DEMO_USERNAME:", DEMO_USERNAME)
print("Loaded DEMO_PASSWORD:", DEMO_PASSWORD)

# ----------------------------- TOKEN GENERATION -----------------------------

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    """
    Creates a JWT token with expiration time.

    Args:
        subject (str): The username or identifier to embed in the token.
        expires_delta (Optional[timedelta]): Custom expiration duration.

    Returns:
        str: Encoded JWT token.
    """
    to_encode = {"sub": subject}
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    
    # Add expiration info into token body
    to_encode.update({"exp": expire})

    # Encode token using secret key
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# ----------------------------- AUTH VALIDATION -----------------------------

security = HTTPBearer()  # Token reader middleware

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Validates and decodes the JWT token and returns authenticated user.

    Args:
        credentials (HTTPAuthorizationCredentials): The extracted bearer token.

    Returns:
        User: The authenticated user object.

    Raises:
        HTTPException: If token is missing, invalid, or user not found.
    """
    token = credentials.credentials
    try:
        # Decode token with stored secret key
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid or expired token"
        )

    # Extract username from the token
    username = payload.get("sub")

    # Validate if token user exists
    if username != DEMO_USERNAME:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="User not found"
        )

    return User(username=username)


# ----------------------------- OPTIONAL PROTECTED ENDPOINT -----------------------------
# Uncomment if needed

# @jwt_router.get("/me")
# def read_me(current_user: User = Depends(get_current_user)):
#     """
#     A protected route that returns the logged-in user's data.
#     """
#     return {
#         "message": "This is a protected endpoint using JWT TOKEN",
#         "user": current_user,
#     }
