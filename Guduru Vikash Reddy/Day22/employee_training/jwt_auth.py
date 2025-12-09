from fastapi import APIRouter,HTTPException,Depends,status
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from datetime import timedelta,datetime,timezone
from pydantic import BaseModel
from typing import Optional
from jose import jwt,JWTError

jwt_router=APIRouter()

class LoginRequest(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_Token:str
    token_type:str

class User(BaseModel):
    username:str

SECRET_KEY="THIS-IS-THE-SECRET-KEY"
ALGORITHM="HS256"
USER_NAME="admin"
PASSWORD="password@123"

def create_access_token (subject:str,expires_delta:Optional[timedelta]=None):
    to_encode={"sub":subject}
    expire=datetime.now(timezone.utc)+(expires_delta or timedelta(minutes=15))
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,ALGORITHM)


security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    username = payload.get("sub")
    if username != USER_NAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return User(username=username)

    
@jwt_router.post("/login",response_model=Token)
def login(data:LoginRequest):
    if USER_NAME==data.username and PASSWORD==data.password:
        expires=timedelta(minutes=30)
        token= create_access_token(subject=data.username,expires_delta=expires)
        return Token(access_Token=token,token_type="bearer")
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="INcorrect credntials")