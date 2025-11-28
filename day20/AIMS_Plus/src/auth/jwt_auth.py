from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

# -----------------------------
# JWT Configuration
# -----------------------------
SECRET_KEY = "AIMSPLUSSECRET"   # Secret key used to sign JWT tokens (keep safe in production!)
ALGORITHM = "HS256"             # Algorithm used for encoding/decoding JWT
TOKEN_EXPIRE_MINUTES = 30       # Token validity duration (in minutes)

# Security scheme: HTTP Bearer (Authorization header with "Bearer <token>")
security = HTTPBearer()


# -----------------------------
# Function: Create JWT token
# -----------------------------
def create_token(data: dict):
    """
    Create a JWT token with payload data.
    - Copies the provided data (e.g., {"username": "admin"}).
    - Adds an expiration time (exp claim).
    - Encodes the token using SECRET_KEY and ALGORITHM.
    Returns the signed JWT token string.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)  # Expiration time
    to_encode.update({"exp": expire})  # Add expiry claim
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Encode JWT
    return token


# -----------------------------
# Function: Verify JWT token
# -----------------------------
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Verify the JWT token provided in the Authorization header.
    - Extracts token from HTTP Bearer credentials.
    - Decodes token using SECRET_KEY and ALGORITHM.
    - Returns payload (user info) if valid.
    - Raises HTTP 401 if token is expired or invalid.
    """
    token = credentials.credentials  # Extract raw token string
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # Decode JWT
        return payload  # Return decoded payload (e.g., {"username": "admin", "exp": ...})
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")  # Expired token
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")  # Invalid token


# -----------------------------
# Router for testing authentication
# -----------------------------
from fastapi import APIRouter

# Create a router for authentication endpoints
jwt_router = APIRouter(prefix="/auth", tags=["Auth"])

@jwt_router.get("/verify")
def verify_user(user: dict = Depends(verify_token)):
    """
    Test endpoint to verify JWT authentication.
    - Depends on verify_token() to validate token.
    - Returns success message and decoded user payload if token is valid.
    Example:
      GET /auth/verify with header Authorization: Bearer <token>
    """
    return {"message": "Token verified", "user": user}
