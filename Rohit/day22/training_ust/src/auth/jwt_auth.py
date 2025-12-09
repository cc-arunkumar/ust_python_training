from fastapi import FastAPI,HTTPException,Depends,status,APIRouter
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from datetime import date,datetime,timedelta,timezone
from pydantic import BaseModel
from typing import Optional
from jose import JWTError,jwt
from dotenv import load_dotenv
import os

class LoginRequest(BaseModel):
    username: str
    password: str
 
class Token(BaseModel):
    access_token: str
    token_type: str
 
class User(BaseModel):
    username: str

load_dotenv(os.path.join(os.path.dirname(__file__),"user_credentials.env" ))
SECRET_KEY = os.getenv("SECRET_KEY","fallback_secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30


DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")
print("Loaded DEMO_USERNAME:", DEMO_USERNAME)
print("Loaded DEMO_PASSWORD:", DEMO_PASSWORD)


def create_acces_token(subject:str , expires_delta :Optional[timedelta]=None):
    to_encode = {"sub":subject}
    print(to_encode)
    expire = datetime.now(timezone.utc)+(expires_delta or timedelta(minutes=15))
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

security =HTTPBearer()


 

def get_current_user(credentials:HTTPAuthorizationCredentials = Depends(security))-> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
 
    username = payload.get("sub")
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
 
    return User(username=username)
    
    
 

