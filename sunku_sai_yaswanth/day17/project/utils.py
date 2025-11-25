from jose import JWTError, jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from typing import Optional
from auth import SECRET_KEY, ALGORITHM

# HTTPBearer helps to extract the token from the Authorization header
bearer_scheme = HTTPBearer()

# Function to verify the JWT and extract the current user
def verify_token(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
    try:
        token = credentials.credentials  # Get the token from the credentials
        # Decode the JWT token and validate it
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401, detail="Could not validate credentials"
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=401, detail="Could not validate credentials"
        )

# Function to get the current user from the token
def get_current_user(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)) -> str:
    return verify_token(credentials)

# Helper function to check if a task exists
def get_task_by_id(task_id: int, tasks: list) -> Optional[dict]:
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None
