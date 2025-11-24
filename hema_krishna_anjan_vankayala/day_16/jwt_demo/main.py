from typing import Optional, List
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, HTTPException, status, Depends
from jose import jwt, JWTError
from pydantic import BaseModel

# Initialize FastAPI app with title
app = FastAPI(title="JWT Demo")

# JWT Configuration 
SECRET_KEY = "change-this-secret-key-in-real-projects"   # Secret key for signing JWTs
ALGORITHM = "HS256"                                     # Algorithm used for JWT encoding/decoding
ACCESS_TOKEN_EXPIRE_MINUTES = 30                        # Token expiry duration

#  Demo User (in-memory) 
user_name = input("Enter user name: ")                  # Prompt for demo username
my_password = input("Enter passowrd: ")                 # Prompt for demo password
DEMO_USERNAME = user_name                               # Store demo username
DEMO_PASSWORD = my_password                             # Store demo password

#  Pydantic Models 
class LoginRequest(BaseModel):
    username: str                                      
    password: str                                     

class Token(BaseModel):
    access_token: str                                   
    token_type: str                                    

class User(BaseModel):
    username: str    # Represents the authenticated user

#  JWT Utility Function 
def create_access_token(subject: str, expiry: Optional[timedelta] = None):
    to_encode = {"sub": subject}   # Payload includes subject (username)
    if expiry:
        expire = datetime.now(timezone.utc) + expiry    # Use provided expiry
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # Default 15 minutes expiry
    to_encode.update({'exp': expire})   # Add expiry to payload
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Encode JWT
    return encoded    # Return encoded token

#  Security Dependency 
security = HTTPBearer()                                 # HTTP Bearer scheme for token extraction

def get_curr_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials   # Extract token string from Authorization header
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)  # Decode JWT
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,   # Raise 401 if token invalid/expired
            detail="Invalid or expired token"
        )
    username = decoded.get('sub')                       # Extract subject (username) from payload
    if username != DEMO_USERNAME:                       # Check if username matches demo user
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,   # Raise 401 if user not found
            detail="User not found"
        )
    return User(username=username)                      # Return authenticated user object

# Login Endpoint 
@app.post('/login', response_model=Token)
def login(user_cred: LoginRequest):
    if user_cred.username != DEMO_USERNAME and user_cred.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User Not Found")  # Invalid credentials
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Set token expiry
    token = create_access_token(subject=user_cred.username, expiry=expires)  # Generate JWT
    return Token(access_token=token, token_type="bearer")    # Return token response
