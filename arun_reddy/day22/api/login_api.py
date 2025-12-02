from models.auth_model import LoginRequest, Token
from auth_jwt import DEMO_PASSWORD, DEMO_USERNAME, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from fastapi import HTTPException, status, APIRouter
from datetime import timedelta

# Router for login
login_router = APIRouter(prefix="/login")

# POST /login → check credentials and return JWT token
@login_router.post("", response_model=Token)
def login(data: LoginRequest):
    # Check username and password
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Set token expiry time
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Create JWT token
    token = create_access_token(subject=data.username, expires_delta=expires)
    
    # Return token response
    return Token(access_token=token, token_type="bearer")
