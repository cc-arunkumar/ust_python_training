from jose import jwt, JWTError  # Import jwt module from 'jose' to encode and decode JWT tokens
from fastapi import HTTPException, status, Depends  # Import FastAPI tools for error handling and dependency injection
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials  # Import HTTPBearer for token-based auth
from sqlalchemy.orm import Session  # Import Session for working with the database
from datetime import datetime, timedelta, timezone  # Import date/time tools for managing token expiration
from database import get_db  # Import database session dependency
from models import UserDB, User  # Import database models for User

# Define the secret key used for encoding and decoding JWT tokens
SECRET_KEY = "UST-TaskTracker-Secret"

# Define the algorithm used for JWT signing (HS256 is a common symmetric encryption algorithm)
ALGORITHM = "HS256"

# Define how long the access token is valid for (in minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Instantiate HTTPBearer for bearer token authentication in FastAPI
security = HTTPBearer()

# Function to create a new JWT access token
def create_access_token(subject: str, expires_delta=None):
    """
    Generates an access token with a specified expiration time.
    
    Parameters:
    - subject (str): The username or subject for the token.
    - expires_delta (timedelta, optional): The time duration for token expiration, default is 30 minutes.
    
    Returns:
    - str: The encoded JWT token.
    """
    # Create a dictionary to hold the token's claims
    to_encode = {"sub": subject}
    
    # Set the expiration time (either default 30 minutes or a custom duration)
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=30))
    
    # Add expiration claim to the token data
    to_encode.update({"exp": expire})
    
    # Return the encoded token using the secret key and algorithm
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Function to extract the current user from the JWT token
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),  # Dependency to get authorization credentials
    db: Session = Depends(get_db)  # Dependency to get a database session
) -> User:
    """
    Decodes the JWT token and fetches the user from the database.

    Parameters:
    - credentials (HTTPAuthorizationCredentials): Authorization data extracted from the request headers.
    - db (Session): The current database session.

    Returns:
    - User: The current user object.

    Raises:
    - HTTPException: If the token is invalid, expired, or the user is not found in the database.
    """
    # Extract the token from the authorization credentials
    token = credentials.credentials
    
    try:
        # Decode the JWT token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # If decoding fails, raise an HTTPException with 401 status code
        raise HTTPException(401, "Invalid or expired token")

    # Extract the username (subject) from the decoded token payload
    username = payload.get("sub")
    
    # Query the database to find the user associated with the username
    user = db.query(UserDB).filter(UserDB.username == username).first()

    # If no user is found, raise an HTTPException with 401 status code
    if not user:
        raise HTTPException(401, "User not found")

    # Return the user object
    return User(username=user.username)
