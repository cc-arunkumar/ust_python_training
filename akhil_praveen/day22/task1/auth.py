from dotenv import load_dotenv
from typing import Optional
from datetime import datetime,timedelta,timezone
import os
from fastapi import HTTPException,Depends
from jose import jwt,JWTError
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from pydantic import BaseModel
class User(BaseModel):
    username : str
    
class LoginRequest(BaseModel):
    username : str
    password : str
    
class Token(BaseModel):
    access_token : str
    token_type : str

load_dotenv()

DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def create_access_token(subject:str,expire_delta : Optional[timedelta] = None):
    to_encode = {"sub":subject}
    
    if expire_delta:
        expires = datetime.now(timezone.utc) + expire_delta
    else:
        expires = datetime.now(timezone.utc) + timedelta(minutes=60) 
    
    to_encode.update({"exp":expires})
    
    encode = jwt.encode(to_encode,SECRET_KEY,algorithm = ALGORITHM)
    
    return encode

security = HTTPBearer()

def get_current_user(credentials : HTTPAuthorizationCredentials = Depends(security)) -> User:
    
    token = credentials.credentials
    
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid or expired token")
    
    username = payload.get("sub")
    
    if username!=DEMO_USERNAME:
        raise HTTPException(status_code=401,detail="Username not found")
    
    return User(username=username)
