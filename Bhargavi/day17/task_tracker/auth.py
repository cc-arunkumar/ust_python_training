from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt  # 'jose' library is used to create and verify JWT tokens
from typing import Optional

# The secret key used to encode and decode the JWT token. It's important to keep this key secure.
SECRET_KEY = "UST-TaskTracker-Secret"
# The algorithm used for encoding the JWT token (HS256 is a commonly used algorithm).
ALGORITHM = "HS256"
# The default expiration time for the JWT token (30 minutes).
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):


    # Define the payload (data) that will be stored in the JWT token.
    to_encode = {"sub": subject}  # 'sub' is a standard claim representing the subject of the token.

    # Set the expiration time for the token.
    if expires_delta:
        # If a custom expiration is provided, use it.
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # If no custom expiration is provided, use the default expiration time.
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Add the expiration time ('exp' is a standard JWT claim representing expiration time).
    to_encode.update({"exp": expire})

    # Encode the payload with the secret key using the specified algorithm (HS256).
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
