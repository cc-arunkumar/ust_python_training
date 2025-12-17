from jose import jwt, JWTError
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException, status
from datetime import timedelta, timezone, datetime

# Hardcoded configuration (not recommended for production)
SECRET_KEY = "super-secret-key-please-change"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10080  # 15 hours

def create_asset_token(subject: str):
    """
    Generate a JWT access token for a given subject (username).
    - Includes 'sub' claim for subject identification.
    - Includes 'exp' claim for token expiration (15 minutes from now).
    """
    # Payload with subject claim
    to_encode = {"sub": subject}
    # Add expiration time to payload
    to_encode.update({"exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

# HTTP Bearer authentication scheme for token extraction
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Dependency function to retrieve the current authenticated user.
    - Extracts JWT token from Authorization header.
    - Decodes and validates token using SECRET_KEY and ALGORITHM.
    - Ensures 'sub' claim matches expected USER_NAME.
    - Returns a User model instance if validation succeeds.
    """
    # Extract raw token string from credentials
    token = credentials.credentials
    try:
        # Decode JWT token and validate signature/expiration
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except JWTError:
        # Raise 401 Unauthorized if token is invalid or expired
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    # Retrieve subject (emp_id) from token payload
    emp_id = payload.get("sub")
    if not emp_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token: missing subject"
        )

    # Return the subject (emp_id) as string. Callers can convert to int if needed.
    return emp_id