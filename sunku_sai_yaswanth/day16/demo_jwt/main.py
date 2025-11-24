from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt

# Initialize the FastAPI app
app = FastAPI(title="JWT Auth Demo")

# Secret key used to encode/decode JWTs (make sure to change this in real projects)
SECRECT_KEY = "change-this-secret-key-in-real-projects"
ALGORITHM = "HS256"  # The algorithm used to sign the JWT (HS256 is a commonly used symmetric key algorithm)
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Expiration time for the token (30 minutes)

# Input the demo username and password (not secure for production use)
user_name = input("enter the user name: ")
password = input("enter the password: ")
DEMO_USERNAME = user_name
DEMO_PASSWORD = password


# Pydantic model for the login request
class LoginRequest(BaseModel):
    username: str
    password: str


# Pydantic model for the token response
class Token(BaseModel):
    access_token: str
    token_type: str


# Pydantic model for the current logged-in user
class User(BaseModel):
    username: str


# Function to create an access token for a user
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    # JWT payload includes the 'sub' (subject) which is the username
    to_encode = {"sub": subject}
    
    # Set the expiration time (default is 15 minutes, but can be overridden)
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    # Add the expiration time to the payload
    to_encode.update({"exp": expire})
    
    # Encode the payload into a JWT token using the secret key and algorithm
    encoded = jwt.encode(to_encode, SECRECT_KEY, algorithm=ALGORITHM)
    return encoded


# HTTPBearer used to extract and validate the token from requests
security = HTTPBearer()

# Function to get the current user based on the JWT token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials  # Extract the token from the Authorization header
    
    try:
        # Decode the JWT token to get the payload
        payload = jwt.decode(token, SECRECT_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # If token is invalid or expired, raise an HTTPException
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    # Get the 'sub' (username) from the payload
    username = payload.get("sub")
    
    # Check if the username matches the expected one (for demo purposes)
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    # Return the current user information
    return User(username=username)


# Route to handle user login and generate JWT token
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    # Check if the provided username and password are correct
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        # If incorrect, raise an HTTPException with 401 Unauthorized status
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    
    # Set expiration time for the token (using the global constant defined earlier)
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Create the access token
    token = create_access_token(subject=data.username, expires_delta=expires)
    
    # Return the token in the response
    return Token(access_token=token, token_type="bearer")


# Protected route that requires a valid JWT token to access
@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    # This endpoint is protected; the user must be authenticated with a valid JWT token
    return {
        "message": "This is a protected endpoint using JWT TOKEN",
        "user": current_user,
    }
