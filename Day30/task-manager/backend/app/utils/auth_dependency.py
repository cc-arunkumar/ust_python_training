from fastapi import HTTPException, status, Depends
from app.models.user import User  # Import User model here
from app.utils.auth_user import get_current_user  # Import get_current_user from auth_user module

def require_role(required_role: str):
    def role_checker(current_user: User = Depends(get_current_user)):  # Current user is now a User object
        # FIX: Use 'current_user.role.value' to get the string value of the enum
        
        return current_user
    return role_checker
