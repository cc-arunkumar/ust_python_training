from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from jose import JWTError,jwt
from datetime import datetime, timezone, timedelta
from models import UserID
from database import fetch_user_by_id
from mongodb_logger import logger


SECRET_KEY = 'UST-TaskTracker-Secret'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30                        # Token expiry duration

#Get Access Token
def get_access_token(subject : str):
    expiry = datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    toencode = {"sub":subject,'exp':expiry}
    token = jwt.encode(toencode,SECRET_KEY,algorithm=ALGORITHM)
    return token
    
security = HTTPBearer() 
#Get Current User
def get_curr_user(credentials : HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials 
    try:
        decoded = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        logger.info("Token decoded successfully")
    except JWTError:
        logger.warning("Invalid or expired token")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token Expired or Invalid")
    
    user_id = decoded.get('sub') # Extract subject (username) from payload
    db_user_id = fetch_user_by_id(int(user_id))
    if db_user_id is None: 
        logger.error(f"User not found for id {user_id}") # Check if username matches demo user
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,   # Raise 401 if user not found
            detail="Invalid username or password"
        )
    logger.info(f"Authenticated user {user_id}")
    return UserID(user_id=user_id)                      # Return authenticated user object


        