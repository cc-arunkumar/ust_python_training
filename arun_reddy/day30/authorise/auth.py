from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt, JWTError
import os

# ================= CONFIG =================

SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME_IMMEDIATELY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# ================= TOKEN CREATION =================

def create_access_token(
    subject: str,
    role: str,
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Creates a JWT access token.

    subject -> emp_id (string)
    role    -> admin / manager / developer
    """

    payload = {
        "sub": subject,
        "role": role
    }

    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    payload.update({"exp": expire})

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# ================= TOKEN DECODING =================

def decode_access_token(token: str):
    """
    Decodes JWT token.
    Returns payload if valid, else None.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
