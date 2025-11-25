from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
from jose import JWTError, jwt

# Initialize FastAPI app
app = FastAPI(title="Minimal jwt demo")

# Secret key and algorithm for JWT token generation
SECRET_KEY = "hi-hello-how-are-you"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time in minutes

# User credentials for demo
user_name = input("Enter username: ")
password = input("Enter password: ")

DEMO_USERNAME = user_name  # User-provided username
DEMO_PASSWORD = password  # User-provided password

# Pydantic model for login request (username and password)
class LoginRequest(BaseModel):
    username: str
    password: str

# Pydantic model for JWT token response (access_token and token_type)
class Token(BaseModel):
    access_token: str
    token_type: str

# Pydantic model for the user (username)
class User(BaseModel):
    username: str

# Function to create a JWT token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    # Prepare the token payload with user subject
    to_encode = {"sub": subject}
    
    # Set expiration time
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # Default expiration time
    
    to_encode.update({"exp": expire})  # Add expiration to the payload
    
    # Encode the JWT token
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

# HTTPBearer security scheme to handle authorization headers
security = HTTPBearer()

# Dependency to get the current user from the JWT token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        # Decode and verify the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # If decoding fails, raise an unauthorized error
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    # Get the username from the token payload
    username = payload.get("sub")
    
    # Check if the username matches the demo user
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    # Return the current user object
    return User(username=username)

# Login endpoint to authenticate and return a JWT token
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    # Check if the provided username and password match the demo credentials
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Username or Password")
    
    # Generate the access token with expiration time
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    
    # Return the JWT token
    return Token(access_token=token, token_type="bearer")

# Protected endpoint to access user information
@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    # This is a protected endpoint, only accessible with a valid JWT token
    return {
        "message": "This is a protected endpoint using JWT TOKEN",
        "user": current_user
    }

# Sample Output

"""
Sample Output for /login (POST):
Input:
{
    "username": "demo_user",
    "password": "demo_password"
}
Output:
{
    "access_token": "some_jwt_token",
    "token_type": "bearer"
}

Sample Output for /me (GET) with valid token:
Input: 
Authorization: Bearer <some_jwt_token>
Output:
{
    "message": "This is a protected endpoint using JWT TOKEN",
    "user": {
        "username": "demo_user"
    }
}

Sample Output for /me (GET) with invalid token:
Input:
Authorization: Bearer <invalid_jwt_token>
Output:
{
    "detail": "Invalid or expired token"
}

Sample Output for /me (GET) without token:
Output:
{
    "detail": "Not authenticated"
}
"""
