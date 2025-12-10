from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from models import User
from database import get_db

# Constants for JWT encoding
SECRET_KEY = "UST-TaskTracker-Secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

security = HTTPBearer()

# Generate a JWT token with an expiration time
def create_access_token(subject: str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": subject, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Decode + verify token
def get_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")  
        if username is None:
            raise HTTPException(status_code=403, detail="Could not validate credentials")
        # Ensure that the user exists in the database
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise HTTPException(status_code=403, detail="User not found")
        return username 
    except JWTError:
        raise HTTPException(status_code=403, detail="Could not validate credentials")