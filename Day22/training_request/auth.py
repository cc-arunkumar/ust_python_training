from datetime import datetime, timedelta, timezone
import os
from typing import Optional
from fastapi import HTTPException, status, Depends,APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from pydantic import BaseModel
from pathlib import Path
from dotenv import load_dotenv
from model import TrainingRequestModel

jwt_router=APIRouter(prefix="/jwt")


load_dotenv()  


DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")
SECURITY_KEY=os.getenv("SECURITY_KEY")
ALGORITHM=os.getenv("ALGORITHM")
print(DEMO_USERNAME)
print(DEMO_PASSWORD)

# print(DEMO_USERNAME)
# print(DEMO_PASSWORD)



def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}
    
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # Default 15 mins expiration
    
    to_encode.update({"exp": expire})
    
    encoded = jwt.encode(to_encode, SECURITY_KEY, algorithm=ALGORITHM)
    return encoded

security = HTTPBearer()

def get_curr_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> TrainingRequestModel:
    token = credentials.credentials
    
    try:
        payload = jwt.decode(token, SECURITY_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    username = payload.get("sub")
    
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    return TrainingRequestModel(username=username)