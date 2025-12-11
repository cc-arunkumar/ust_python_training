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
SECRET_KEY = os.getenv("SECRET_KEY", "UST-TaskTracker-Secret")  # Use environment variable for secret key
ALGORITHM = "HS256"  # JWT algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiry time in minutes

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to create access token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}  # Payload contains subject (username)
    
    # Set expiration time for the token (if not provided, use default)
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Add expiration time to the payload
    to_encode.update({"exp": expire})
    
    # Encode the JWT token with the secret key and algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to verify password (check against the DB)
def verify_password(db: Session, username: str, password: str):
    # Query the user from the database
    user = db.query(User).filter(User.username == username).first()
    if not user or not pwd_context.verify(password, user.password):  # Verify password hash
        return False  # Return False if user doesn't exist or password mismatch
    return True  # Return True if password matches

# Function to authenticate a user
def authenticate_user(db: Session, username: str, password: str):
    # Check if the username and password are correct
    if not verify_password(db, username, password):
        raise HTTPException(status_code=401, detail="Invalid username or password")  # Raise error if invalid
    
    # If authentication is successful, generate and return JWT token
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
        # Decode the JWT token using the secret key
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")  # Extract username (subject) from the token
        if username is None:
            raise credentials_exception  # Raise error if subject is not found in token
        
        # Query the user from the database
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise credentials_exception  # Raise error if user does not exist in the database
        
        return user  # Return the user object if valid
    except JWTError:
        raise credentials_exception  # Raise error if JWT decoding fails

# Function to hash password (for user registration)
def hash_password(password: str):
    # Hash the plain text password
    return pwd_context.hash(password)
