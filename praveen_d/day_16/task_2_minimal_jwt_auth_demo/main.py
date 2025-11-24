from datetime import datetime,timedelta,timezone
from typing import Optional
from fastapi import FastAPI,HTTPException,status,Depends
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError,jwt

app=FastAPI(description="Minimal JWT Auth Demo")

# JWT configuration

SECRET_KEY="change-this secret-key-in-real-projects"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Demo user(in-memory)
user_name=input("Enter the username:")
password=input("Enter the password:")
DEMO_USERNAME=user_name
DEMO_PASSWORD=password

# pydantic models
class LoginRequest(BaseModel):
    username:str
    password:str
class Token(BaseModel):
    access_token:str
    token_type:str
class User(BaseModel):
    username:str

# Helper to create JWT
# subject:str,expires_delta:Optional[timedelta]=None
def create_access_token(subject:str,expires_delta:Optional[timedelta]=None):
    to_encode={"sub":subject}
    
    if expires_delta:
        expire=datetime.now(timezone.utc)+expires_delta
    else:
        expire=datetime.now(timezone.utc)+timedelta(minutes=15)
    
    to_encode.update({"exp":expire})
    encoded=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

# HTTPBearer or Authorization:Bearer <token>
security=HTTPBearer()

# Decode +verify token
def get_current_user(credientials:HTTPAuthorizationCredentials=Depends(security))->User:
    token=credientials.credentials
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid or expired token")
    
    user_name=payload.get("sub")
    if user_name!= DEMO_USERNAME:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return User(username=user_name)
        



# login endpoint->returns JWT token
@app.post("/login",response_model=Token)
def login(data:LoginRequest):
    if data.username!=DEMO_USERNAME or data.password!=DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect username or password")
    
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token=create_access_token(subject=data.username,expires_delta=expires)
    
    return Token(access_token=token,token_type="bearer")

@app.get("/me")
def read_me(current_user:User= Depends(get_current_user)):
    return {
        "message":"This is a protected endpoint using JWT TOKEN",
        "user":current_user,
    }



    
    
