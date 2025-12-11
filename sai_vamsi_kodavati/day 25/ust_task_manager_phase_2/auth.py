from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import HTTPException
from passlib.context import CryptContext
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from database import User
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
SECRET_KEY = os.getenv("SECRET_KEY", "UST-TaskTracker-Secret")  # Use environment variable
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Initialize password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to create access token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}
    
    # Set expiration time for the token
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Add expiration time to the payload
    to_encode.update({"exp": expire})
    
    # Encode the JWT
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to verify password (check against the DB)
def verify_password(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not pwd_context.verify(password, user.password):  # Hash passwords in real-world use
        return False
    return True

# Function to authenticate a user
def authenticate_user(db: Session, username: str, password: str):
    # Check if the username and password are correct
    if not verify_password(db, username, password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    # If authenticated, generate and return JWT token
    access_token = create_access_token(subject=username)
    return {"access_token": access_token, "token_type": "bearer"}

# Function to get the current user from the JWT token
def get_current_user(token: str, db: Session):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        
        # Query the user from the database
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise credentials_exception
        
        return user
    except JWTError:
        raise credentials_exception

# Function to hash password (for user registration)
def hash_password(password: str):
    return pwd_context.hash(password)
