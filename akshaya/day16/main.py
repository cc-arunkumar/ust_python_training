from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt


# FastAPI app initialization
app = FastAPI(title="Minimal JWT Auth Demo")


# JWT configuration settings
SECRET_KEY = "change-this-secret-key-in-real-projects"  # Use a secure, randomly generated key in production
ALGORITHM = "HS256"  # Hashing algorithm for JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Expiry time for access tokens

# Demo user credentials (in-memory, should be replaced with a secure database in production)
user_name = input("Enter user name: ")  # For demo purposes, username is input during runtime
my_password = input("Enter passowrd: ")  # Password input at runtime, insecure in production
DEMO_USERNAME = user_name
DEMO_PASSWORD = my_password


# Pydantic models for request and response validation
class LoginRequest(BaseModel):
    """
    Pydantic model to represent the login request body, where users provide their credentials.
    Ensures proper validation of incoming data.
    """
    username: str
    password: str

class Token(BaseModel):
    """
    Pydantic model for the response containing the access token.
    Ensures a structured response for the token generation.
    """
    access_token: str
    token_type: str

class User(BaseModel):
    """
    Pydantic model to represent the authenticated user.
    This model is used to return user data after successful authentication.
    """
    username: str


# Helper function to create JWT access token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    """
    Creates a JWT token for the given user subject.
    If expiration is provided, it sets the expiration time, else it uses the default expiration.
    """
    to_encode = {"sub": subject}  # Subject represents the username of the user

    # Set the expiration time of the token
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # Default expiration

    to_encode.update({"exp": expire})  # Add the expiration time to the token payload
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Encode the payload using the SECRET_KEY and ALGORITHM
    return encoded


# HTTPBearer for Authorization: Bearer <token> scheme
security = HTTPBearer()


# Decode and verify the JWT token to get the current authenticated user
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Decodes and verifies the JWT token to retrieve the current user.
    This is used to protect endpoints, ensuring only authorized users can access them.
    """
    token = credentials.credentials  # Extract token from the HTTP Authorization header
    try:
        # Decode the token using the SECRET_KEY and the specified ALGORITHM
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"  # Raise an error if token is invalid or expired
        )

    # Extract the username from the payload
    username = payload.get("sub")
    
    # If the username does not match the DEMO_USERNAME, raise an unauthorized error
    if username != DEMO_USERNAME:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"  # This checks the username in the payload
        )

    # Return the User object with the decoded username
    return User(username=username)


# /login endpoint to authenticate users and return a JWT token
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Endpoint to authenticate users with their username and password.
    If successful, returns a JWT access token.
    """
    # Validate the credentials (in production, replace this with database authentication)
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",  # Return error if username/password mismatch
        )

    # Set expiration time for the token
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Generate access token for the authenticated user
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")  # Return the generated token


# Protected endpoint to retrieve user details
@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    """
    A protected endpoint that can only be accessed by authenticated users.
    It returns the user data and a message.
    """
    return {
        "message": "This is a protected endpoint using JWT TOKEN",  # Message confirming successful authentication
        "user": current_user,  # Return user object containing the username
    }


# sample output
# Response body
# Download
# {
#   "message": "This is a protected endpoint using JWT TOKEN",
#   "user": {
#     "username": "aksh"
#   }
# }