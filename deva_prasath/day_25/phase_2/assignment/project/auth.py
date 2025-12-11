# Import necessary modules for handling dates, JWTs, FastAPI, and security
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from database import get_db, UserDB
from sqlalchemy.orm import Session

# Initialize HTTPBearer for managing authorization headers
security = HTTPBearer()

# Function to create an access token
def create_access_token(subject: str):
    # Set the expiration time of the token
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Prepare the payload with subject (username) and expiration time
    to_encode = {"sub": subject, "exp": expire}
    # Return the encoded JWT token
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Function to get the user from the token
def get_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    # Extract the token from the HTTPAuthorizationCredentials object
    token = credentials.credentials
    try:
        # Decode the token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Extract the username (subject) from the token payload
        username: str = payload.get("sub")
        # If the username is missing, raise an unauthorized exception
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
        
        # Query the database to find the user with the extracted username
        user = db.query(UserDB).filter(UserDB.username == username).first()
        # If the user is not found, raise an unauthorized exception
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
        
        # Return the user object if found
        return user 
    except JWTError:
        # If there's any error decoding the token, raise an unauthorized exception
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
