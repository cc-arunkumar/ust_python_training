from fastapi import HTTPException, status, Depends, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from dotenv import load_dotenv
import os
from src.models.login_model import User,Token,LoginRequest
 
 
# Load environment variables
load_dotenv()
 
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
DEMO_USERNAME = os.getenv("DEMO_USER")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")
 
print("Loaded DEMO_USERNAME:", DEMO_USERNAME)
print("Loaded DEMO_PASSWORD:", DEMO_PASSWORD)
 

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
 
security = HTTPBearer()
 
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
 
    username = payload.get("sub")
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
 
    return User(username=username)
 

 
# @jwt_router.get("/me")
# def read_me(current_user: User = Depends(get_current_user)):
#     return {
#         "message": "This is a protected endpoint using JWT TOKEN",
#         "user": current_user,
#     }
 