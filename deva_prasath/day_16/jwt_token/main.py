from datetime import datetime,timedelta,timezone
from typing import Optional
from fastapi import FastAPI,HTTPException,status,Depends
from pydantic import BaseModel
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from jose import JWTError,jwt

# FastAPI app
app = FastAPI(title="Minimal JWT Auth Demo")

# JWT configuration
SECRET_KEY = "-----"  # Secret key used for encoding and decoding JWT tokens
ALGORITHM = "HS256"  # Algorithm used for encoding/decoding the JWT token
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Expiration time for the access token in minutes

# Demo user (in-memory)
user_name = input("Enter user name: ")  # Takes user input for username
my_password = input("Enter passowrd: ")  # Takes user input for password
DEMO_USERNAME = user_name  # Stores the entered username for demo purposes
DEMO_PASSWORD = my_password  # Stores the entered password for demo purposes

class LoginRequest(BaseModel):
    username:str  # The username for login
    password:str  # The password for login
    
class Token(BaseModel):
    access_token:str  # The generated JWT access token
    token_type:str  # Type of the token (bearer)

class User(BaseModel):
    username:str  # The username of the user


def create_access_token(subject:str,expires_delta:Optional[timedelta]=None):
   
    to_encode={"sub":subject}  # Create payload with the subject (username)
    
    if expires_delta:
        expire=datetime.now(timezone.utc)+expires_delta  # Calculate expiration if provided
    else:
        expire=datetime.now(timezone.utc)+timedelta(minutes=15)  # Default expiration time (15 minutes)
    
    to_encode.update({'exp':expire})  # Add expiration time to the payload
    encoded=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)  # Encode the payload with the secret key and algorithm
    return encoded  # Return the encoded JWT token

security=HTTPBearer()  # Security dependency for bearer token authentication

def get_current_user(credentials:HTTPAuthorizationCredentials=Depends(security)) -> User:
    
    token=credentials.credentials  # Extract token from the credentials
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])  # Decode the token
    except JWTError:  # If there is an error decoding, raise unauthorized error
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    username=payload.get("sub")  # Get the username (subject) from the payload
    if username!=DEMO_USERNAME:  # Validate if the user exists in the demo data
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return User(username=username)  # Return the User model with the username

@app.post("/login",response_model=Token)
def login(data:LoginRequest):
  
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:  # Check if credentials match demo data
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    
    expires=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Set expiration time for the token
    token=create_access_token(subject=data.username, expires_delta=expires)  # Generate the access token

    return Token(access_token=token,token_type="bearer")  # Return the token as a response

@app.get("/me")
        
def read_me(current_user:User=Depends(get_current_user)):
    
    return {
        "message":"This is a protected endpoint using JWT TOKEN",  # Message indicating the protected status
        "user":current_user,  # The current user object (from JWT token)
    }
