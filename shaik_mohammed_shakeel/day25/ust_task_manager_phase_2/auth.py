from datetime import datetime, timedelta, timezone
from typing import Optional, Dict
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from passlib.context import CryptContext  # Password hashing library
from passlib.exc import UnknownHashError
import logging
from mongodb_logger import log_activity  # Import MongoDB logging function
 
import models  # Ensure your user model is imported here
from db_connection_sql import get_db  # DB session dependency
 
# Constants for JWT
SECRET_KEY = "UST-TaskTracker-Secret"  # Change for production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Expiration time for the JWT token
 
# Initialize the bearer security
security = HTTPBearer()
 
# Initialize CryptContext for hashing passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # Password hashing algorithm
 
# -------------------- Authenticate User --------------------
 
# Authenticate the user by verifying username and password from the database
def authenticate_user(username: str, password: str, db: Session) -> Optional[Dict[str, str]]:
    # Query user from the database
    user = db.query(models.User).filter(models.User.username == username).first()
 
    # Check if the user exists and if the password is valid
    if user is None or not verify_password(password, user.password):  # verify_password function is defined below
        return None
   
    # Log the successful login activity in MongoDB
    log_activity(username, "LOGIN", None)  # No task_id for login, so passing `None`
   
    return {"username": user.username}  # Return user data (username) if valid
 
# -------------------- Password Verification --------------------
 
# Verify the hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against a hashed password.
    """
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except UnknownHashError:
        # Stored password isn't recognized as a passlib hash (maybe plaintext)
        logging.warning("Stored password for user is not a recognized hash; falling back to direct compare")
        return plain_password == hashed_password
 
# -------------------- JWT Creation --------------------
 
# Create JWT token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Creates an access token with an expiration time.
    """
    to_encode = data.copy()
    if expires_delta is None:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Default expiration time
 
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
   
    # Encode the JWT token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
 
# -------------------- Get Current User --------------------
 
# Extract current user from the JWT token (this function is used as a dependency in FastAPI endpoints)
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)) -> Dict[str, str]:
    """
    Extracts the user information from the JWT token.
    """
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
 
    try:
        # Decode the JWT token to extract user information (sub -> username)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception  # If no username found in the token, raise exception
    except JWTError:
        raise credentials_exception  # If the token is invalid or expired, raise exception
 
    # Query the user from the database
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception  # If user is not found in DB, raise exception
 
    return {"username": user.username}  # Return the username of the authenticated user
 
# -------------------- Hash Password --------------------
 
# Function to hash the password
def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)
 
 