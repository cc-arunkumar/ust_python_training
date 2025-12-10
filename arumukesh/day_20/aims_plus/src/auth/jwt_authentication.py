from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
import os
from typing import Optional
from src.model.model_login import User

jwt_router = APIRouter(prefix="/jwt")

load_dotenv()

# Environment Variables
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))

# Demo User
DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")  # <-- stored plain for demo

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


# ------------------ Helper Methods ------------------

def verify_password(raw_password: str, hashed_password: str):
    """Compare plain text password with hashed value."""
    return pwd_context.verify(raw_password, hashed_password)


def hash_password(password: str):
    """Hash password for secure storage."""
    return pwd_context.hash(password)


def get_user(username: str):
    """Mock DB lookup."""
    if username == DEMO_USERNAME:
        return User(username=username)
    return None


def authenticate_user(username: str, password: str):
    """Validate credentials."""
    if username == DEMO_USERNAME and password == DEMO_PASSWORD:
        return get_user(username)
    return None


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Generate JWT token."""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)):
    """Extract current user from JWT."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Token missing username")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = get_user(username)

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user
