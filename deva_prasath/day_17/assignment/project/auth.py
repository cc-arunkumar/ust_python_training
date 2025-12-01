from fastapi import HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from typing import Optional
from utils import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, users

# Function to create access token
def create_access_token(subject:str,expires_delta:Optional[timedelta]=None):
    to_encode={"sub":subject}
    #setting expire time
    expire=datetime.now(timezone.utc)+(expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp":expire})
    #encoding using jwt
    encoded=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded

# Function to verify token
def verify_token(token: str):
    try:
        #decoding
        payload=jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
        return payload.get("sub")  # Return the subject (username)``
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials")
