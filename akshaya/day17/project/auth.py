# auth.py
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from models import User
from main import SECRET_KEY, ALGORITHM


# Helper to create JWT
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}
    
    # Set the expiration time (default is 15 minutes if no expires_delta is provided)
    expire = datetime.now(timezone.utc) + (expires_delta if expires_delta else timedelta(minutes=15))
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Decode + verify token
def get_current_user(token: str) -> User:
    try:
        # Decode the JWT token and check its validity
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        
        if username is None:
            raise JWTError("Token doesn't contain user information.")
        
    except JWTError:
        raise Exception("Invalid or expired token")
    
    return User(username=username)
