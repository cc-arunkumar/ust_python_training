from datetime import datetime, timedelta, timezone  # For handling time and dates
from jose import JWTError, jwt  # For encoding and decoding JWT tokens
from typing import Optional  # For Optional type hinting

# Secret key used for encoding the JWT token
SECRET_KEY = "UST-TaskTracker-Secret"
# Algorithm for encoding the JWT
ALGORITHM = "HS256"
# Default expiration time for the access token (in minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Function to create a JWT access token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    # Create the payload with the subject (user info)
    to_encode = {"sub": subject}
    
    # If an expiration time is provided, use it
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # Otherwise, use the default expiration time
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Add expiration time (exp) to the payload
    to_encode.update({"exp": expire})

    # Encode the JWT token with the secret key and algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    # Return the encoded JWT token
    return encoded_jwt
