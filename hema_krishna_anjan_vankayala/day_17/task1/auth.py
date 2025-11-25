from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from jose import JWTError,jwt
from datetime import datetime, timezone, timedelta
from models import User

users = {
 "rahul": {
 "username": "rahul",
 "password": "password123" # store as plain text for this assignment only
}
}

DEMO_USER_NAME  = users['rahul']['username']
DEMO_PASSWORD = users['rahul']['password']

SECRET_KEY = 'UST-TaskTracker-Secret'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30                        # Token expiry duration

def get_access_token(subject : str):
    expiry = datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    toencode = {"sub":subject,'exp':expiry}
    token = jwt.encode(toencode,SECRET_KEY,algorithm=ALGORITHM)
    return token
    
security = HTTPBearer() 
def get_curr_user(credentials : HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials 
    try:
        decoded = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token Expired or Invalid")
    
    username = decoded.get('sub')                       # Extract subject (username) from payload
    if username != DEMO_USER_NAME:                       # Check if username matches demo user
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,   # Raise 401 if user not found
            detail="Invalid username or password"
        )
    return User(username=username)                      # Return authenticated user object


        