from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from database import SessionLocal, User 


# Dependency to get a database session
def get_db():
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Yield the session so it can be used in route functions
    finally:
        db.close()  # Ensure the session is closed after use


# Constants for JWT creation
SECRET_KEY = "UST-TaskTracker-Secret"  # Secret key used to sign the JWT token
ALGORITHM = "HS256"  # Algorithm used to sign the token (HS256)


# Function to create a JWT access token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    # Define the payload of the token
    to_encode = {"sub": subject}  # The subject is the username (subject of the token)

    # Set the expiration time of the token
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta  # Expiration time if provided
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # Default expiration time (15 minutes)

    to_encode.update({"exp": expire})  # Add the expiration time to the payload

    # Encode the token using the secret key and algorithm
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded  # Return the encoded JWT token


# Security scheme for handling the JWT token in requests
security = HTTPBearer()


# Dependency to get the current user from the token
def get_curr_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)) -> User:
    token = credentials.credentials  # Get the token from the Authorization header

    try:
        # Decode the token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # If decoding fails, raise an HTTP 401 error
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    username = payload.get("sub")  # Get the 'sub' (subject) field from the payload (username)
    if username is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    # Fetch the user from the MySQL database using the username
    user = db.query(User).filter(User.username == username).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return user  # Return the user object


# Function to authenticate a user based on username and password
def authenticate_user(username: str, password: str, db: Session) -> User:
    # Query the database for the user with the specified username
    user = db.query(User).filter(User.username == username).first()

    # If the user doesn't exist or the password doesn't match, raise an HTTP 401 error
    if user is None or user.password != password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    
    return user  # Return the user object if authentication is successful
