from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any
from jose import jwt, JWTError
from argon2 import PasswordHasher
from fastapi import HTTPException, status
from app.core.config import settings

ph = PasswordHasher()

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    try:
        return ph.verify(hashed, password)
    except Exception:
        return False

def create_access_token(
    subject: str,
    role: str,
    status: str,
    employee_id: Optional[int] = None,
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Create a JWT access token embedding user_id (sub), role, status, and employee_id.
    """
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.access_token_expire_minutes)
    )
    to_encode: Dict[str, Any] = {
        "sub": subject,
        "role": role,
        "status": status,
        "employee_id": employee_id,   # ✅ include employee_id
        "exp": expire
    }
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def decode_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
