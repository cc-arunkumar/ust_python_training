from jose import JWTError, jwt  # For encoding, decoding, and handling JWT tokens
from fastapi import HTTPException, Security  # For HTTP exceptions and security handling
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials  # For extracting the token from headers
from datetime import datetime, timedelta  # For handling dates and times
from typing import Optional  # For type hinting (Optional)
from auth import SECRET_KEY, ALGORITHM  # Import secret key and algorithm used for encoding/decoding JWT

# HTTPBearer is used to extract the JWT token from the Authorization header
bearer_scheme = HTTPBearer()

# Function to verify the JWT token and extract the current user
def verify_token(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
    try:
        # Extract the token from the credentials
        token = credentials.credentials
        
        # Decode the JWT token and validate it using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Extract the username (subject) from the decoded payload
        username: str = payload.get("sub")
        
        # If no username (sub) in the payload, raise an error
        if username is None:
            raise HTTPException(
                status_code=401, detail="Could not validate credentials"
            )
        
        # Return the username if token is valid
        return username
    except JWTError:
        # If decoding or validation fails, raise an exception
        raise HTTPException(
            status_code=401, detail="Could not validate credentials"
        )

# Function to get the current user from the token
def get_current_user(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)) -> str:
    # Calls verify_token to check the validity of the JWT and return the username
    return verify_token(credentials)

# Helper function to check if a task exists by ID
def get_task_by_id(task_id: int, tasks: list) -> Optional[dict]:
    # Iterate through the list of tasks to find the task by its ID
    for task in tasks:
        if task["id"] == task_id:
            return task  # Return the task if found
    return None  # Return None if the task is not found
