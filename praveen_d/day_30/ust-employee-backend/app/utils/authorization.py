from fastapi import Depends, HTTPException, status
from utils.auth_dependency import get_current_user
from utils.permissions import ROLE_PERMISSIONS

def require_permission(permission: str):
    def checker(user=Depends(get_current_user)):
        role = user.get("role")

        if not role or permission not in ROLE_PERMISSIONS.get(role, set()):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )
        return user
    return checker
