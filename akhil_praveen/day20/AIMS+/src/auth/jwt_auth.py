from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from ..models.login_model import User
import os
from dotenv import load_dotenv

SECRET_KEY = os.getenv("SECRET_KEY") 
ALGORITHM = os.getenv("ALGORITHM")
DEMO_USERNAME = os.getenv("DEMO_USERNAME")

def create_access_token(subject:str,expires_delta : Optional[timedelta] = None):
    to_encode = {"sub":subject}
    
    if expires_delta:
        expires_delta = datetime.now(timezone.utc) + expires_delta
    else:
        expires_delta = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    to_encode.update({"exp":expires_delta})
    encoded = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    
    return encoded

security = HTTPBearer()

def get_current_user(credentials : HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    username = payload.get("sub")
    
    if username!=DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    return User(username=username)
    