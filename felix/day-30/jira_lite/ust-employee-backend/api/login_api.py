from fastapi import APIRouter, HTTPException, status
from models.user_model import LoginModel
from models.user_model import Token
from auth.jwt_auth import create_asset_token
from services.user_services import authenticate_user


# Create a router instance for login-related endpoints
login_router = APIRouter()


@login_router.post("", response_model=Token)
def login(user: LoginModel):
    """Login endpoint that validates user credentials against MySQL users table and returns a JWT token.

    - Accepts a UserModel containing emp_id and password.
    - Verifies credentials using services.authenticate_user.
    - Returns a bearer token if authentication succeeds.
    """
    print("Login attempt received")
    emp_id = user.emp_id
    password = user.password
    print(f"Attempting login for emp_id: {emp_id}")

    # Authenticate against the database
    auth_user = authenticate_user(emp_id, password)
    if not auth_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid emp_id or password"
        )

    # create token with emp_id as string
    token = create_asset_token(str(emp_id))
    return Token(token=token, token_type="bearer")