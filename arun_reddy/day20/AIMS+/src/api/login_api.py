from fastapi import HTTPException, status,APIRouter
from datetime import timedelta
from ..auth.jwt_auth import jwt_router,DEMO_PASSWORD,DEMO_USERNAME,ACCESS_TOKEN_EXPIRE_MINUTES,create_access_token
from ..models.user_model import Token,LoginRequest
login_router=APIRouter(prefix="/login")

@login_router.post("", response_model=Token)
def login(data: LoginRequest):
    # Check if the provided username and password are correct
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        # If incorrect, raise an HTTPException with 401 Unauthorized status
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    # Set expiration time for the token (using the global constant defined earlier)
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Create the access token
    token = create_access_token(subject=data.username, expires_delta=expires)
    # Return the token in the response
    return Token(access_token=token, token_type="bearer")
