from fastapi import HTTPException,Depends
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from jose import jwt,JWTError
from typing import Optional
from datetime import datetime,timedelta,timezone
from ..models.user_model import User
from dotenv import load_dotenv
import os

load_dotenv()

SECRECT_KEY = os.getenv("SECRECT_KEY")
ALGORITHM = os.getenv("ALGORITHM")

USERNAME = os.getenv("USER_NAME")


def create_access_token(subject:str,expires_delta:Optional[timedelta]=None):
    to_encode = {"sub":subject}
    if expires_delta:
        expires = datetime.now(timezone.utc) + expires_delta
    else:
        expires = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp":expires})

    encoded = jwt.encode(to_encode,SECRECT_KEY,algorithms=ALGORITHM)
    return encoded



security = HTTPBearer()


def get_current_user(credentials : HTTPAuthorizationCredentials = Depends(security))->User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token,SECRECT_KEY,algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid or expired token")
    
    username = payload.get("sub")
    if username!=USERNAME:
        raise HTTPException(status_code=401,detail="User not found")
    
    return User(username=username)

