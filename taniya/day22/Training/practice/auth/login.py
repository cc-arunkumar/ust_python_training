from fastapi import HTTPException,status,Depends
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from typing import Optional
from datetime import datetime,date,timedelta,timezone
from jose import JWTError,jwt
from dotenv import load_dotenv
import os
from practice.models.login_model import Token,LoginRequest,user

load_dotenv(os.path.join(os.path.dirname(__file__),"user_credential.enc"))
SECRET_KEY=os.getenv("SECRET_KEY","fallback-street")
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES= 60

DEMO_USERNAME=os.getenv("DEMO_USERNAME")
DEMO_PASSWORD=os.getenv("DEMO_PASSWORD")

print("DEMO_USERNAME:",DEMO_USERNAME)
print("DEMO_PASSWORD:",DEMO_PASSWORD)

def create_access_token(subject:str,expires_delta:Optional[timedelta]=None):
    to_encode={"sub":subject}
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))

    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
security=HTTPBearer()

def get_username(credentials:HTTPAuthorizationCredentials = Depends(security)) -> user:
    token=credentials.credentials
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    username=payload.get("sub")
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
 
    return user(username=username)
