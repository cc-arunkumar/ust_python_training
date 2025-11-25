# auth.py
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt

# import demo credentials
try:
    from .model import DEMO_USERNAME, DEMO_PASSWORD
except Exception:
    # fallback if direct import fails (when run as single file)
    from model import DEMO_USERNAME, DEMO_PASSWORD

SECRET_KEY = "change-this-secret-key-in-real-projects"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

security = HTTPBearer()


class User(BaseModel):
    username: str


def auth_user(username: str, password: str) -> bool:
    return username == DEMO_USERNAME and password == DEMO_PASSWORD


def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:

    now = datetime.now(timezone.utc)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {
        "sub": subject,
        "iat": now,
        "exp": expire,
    }
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),) -> User:

    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    username = payload.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing subject (username)",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if username != DEMO_USERNAME:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return User(username=username)
