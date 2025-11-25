# auth.py
from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from models import User


users = {
 "rahul": {
 "username": "rahul",
 "password": "password123"   # store as plain text for this assignment onl

}
 }

DEMO_USERNAME = users["rahul"]["username"]
DEMO_PASSWORD = users["rahul"]["password"]

SECRET_KEY = "UST-TaskTracker-Secret"
ALGORITHM="HS256"




    
def create_access_token(subject:str,expires_delta:Optional[timedelta]=None):
    to_encode={"sub":subject}
    
    if expires_delta:
        expire=datetime.now(timezone.utc)+expires_delta
    else:
        expire=datetime.now(timezone.utc)+timedelta(minutes=15)
        
    to_encode.update({"exp":expire})
    
    encoded=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

security = HTTPBearer()
def get_curr_user(credentials:HTTPAuthorizationCredentials=Depends(security))->User:
    token=credentials.credentials
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    username = payload.get("sub")
    
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    return User(username=username)
