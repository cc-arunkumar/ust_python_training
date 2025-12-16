from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import decode_token

# Use HTTPBearer instead of OAuth2PasswordBearer
bearer_scheme = HTTPBearer()

class AuthUser(dict):
    """Wrapper for decoded JWT payload"""

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> AuthUser:
    """
    Extract and decode JWT from Authorization header.
    Swagger UI will now only show a simple Bearer token field.
    """
    token = credentials.credentials
    payload = decode_token(token)
    return AuthUser(payload)

def require_admin(current_user: AuthUser = Depends(get_current_user)) -> AuthUser:
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return current_user

def require_manager(current_user: AuthUser = Depends(get_current_user)) -> AuthUser:
    if current_user.get("role") not in {"admin", "manager"}:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Manager privileges required"
        )
    return current_user

def require_employee(current_user: AuthUser = Depends(get_current_user)) -> AuthUser:
    if current_user.get("role") not in {"admin", "manager", "employee"}:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Employee privileges required"
        )
    return current_user
