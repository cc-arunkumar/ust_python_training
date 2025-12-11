from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from models import UserName  # Assuming this is the schema/model for the user
from sqlalchemy.orm import Session
from database import SessionLocal, User  # Assuming 'User' is the SQLAlchemy model

# Dependency to get a session from the database
def get_db():
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Yield the session to be used by other functions
    finally:
        db.close()  # Close the session after it's no longer needed

# Constants for JWT creation
SECRET_KEY = "UST-TaskTracker-Secret"  # Secret key for JWT signing
ALGORITHM = "HS256"  # Algorithm for signing the JWT token

# Function to create an access token (JWT)
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    """
    Create a JWT access token for the given subject (user).
    :param subject: The username or identifier of the user (sub).
    :param expires_delta: The expiration time for the token, if provided.
    :return: Encoded JWT token.
    """
    to_encode = {"sub": subject}  # Payload with the subject (username)
    
    # Set the expiration time (either passed in or default 15 minutes)
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta  # Custom expiration
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # Default expiration (15 minutes)
    
    to_encode.update({"exp": expire})  # Add the expiration time to the payload
    
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Encode the JWT with the secret key and algorithm
    return encoded  # Return the encoded JWT token

# HTTPBearer security dependency for extracting the token from the request
security = HTTPBearer()

# Dependency to get the current user from the token
def get_curr_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)) -> User:
    """
    Get the current authenticated user based on the JWT token in the request.
    :param credentials: The HTTP authorization credentials (JWT token).
    :param db: The database session.
    :return: The User object if the token is valid and the user exists.
    """
    token = credentials.credentials  # Extract the token from the credentials
    
    try:
        # Decode the JWT token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # If the token is invalid or expired, raise an exception
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    # Get the username (subject) from the decoded token payload
    username = payload.get("sub")
    
    if username is None:
        # If the username is not found in the payload, raise an exception
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    # Fetch the user from the database by username
    user = db.query(User).filter(User.username == username).first()
    
    if user is None:
        # If the user does not exist in the database, raise an exception
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    return user  # Return the user object

# Function to authenticate the user based on username and password
def authenticate_user(username: str, password: str, db: Session) -> User:
    """
    Authenticate a user by their username and password.
    :param username: The username provided by the user.
    :param password: The password provided by the user.
    :param db: The database session.
    :return: The authenticated User object.
    """
    # Query the user from the database by username
    user = db.query(User).filter(User.username == username).first()
    
    # If the user is not found or the password is incorrect, raise an exception
    if user is None or user.password != password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    
    return user  # Return the authenticated user
