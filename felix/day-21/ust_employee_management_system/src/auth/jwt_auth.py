from jose import jwt,JWTError
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from fastapi import Depends,HTTPException,status
import os
from dotenv import load_dotenv
from datetime import timedelta,timezone,datetime
from ..model.user_model import User

load_dotenv()
USER_NAME = os.getenv("USER_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
def create_asset_token(subject:str):
    to_encode = {"sub":subject}
    to_encode.update({"exp":datetime.now(timezone.utc)+timedelta(minutes=15)})
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

security = HTTPBearer()
def get_current_user(credentials:HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid or expired token")

    username = payload.get("sub")
    
    if username != USER_NAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid or expired token")
    return User(username=username)