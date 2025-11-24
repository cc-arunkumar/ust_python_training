from datetime import datetime,timedelta,timezone
from typing import Optional
from fastapi import FastAPI,HTTPException,status,Depends
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from pydantic import BaseModel
from jose import JWTError,jwt

app = FastAPI(title="Minimal jwt demo")


SECRET_KEY = "hi-hello-how-are-you"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

user_name = input("Enter username: ")
password = input("Enter password: ")

DEMO_USERNAME = user_name
DEMO_PASSWORD = password

class LoginRequest(BaseModel):
    username : str
    password : str
    
class Token(BaseModel):
    access_token : str
    token_type : str
    
class User(BaseModel):
    username : str
    
 
def create_access_token(subject:str,expires_delta:Optional[timedelta]=None):
    to_encode = {"sub":subject}    
    if expires_delta:
        expire = datetime.now(timezone.utc)+expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    to_encode.update({"exp":expire})
    encoded = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid or expired token")
    
    username = payload.get("sub")
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User not found")
        
    return User(username=username)

@app.post("/login",response_model=Token)
def login(data: LoginRequest):
    if data.username!=DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect Username or Password")
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username,expires_delta=expires)
    return Token(access_token=token,token_type="bearer")

@app.get("/me")
def read_me(current_user:User = Depends(get_current_user)):
    return {
        "message":"This is a protected endpoint using JWT TOKEN",
        "user" : current_user
    }