from fastapi import Depends, HTTPException, status
from utils.auth_dependency import get_current_user
from utils.permissions import ROLE_PERMISSIONS

def require_permission(permission: str):
    def checker(user=Depends(get_current_user)):
        role = user.get("role")

        # role may be a string or a list of strings
        allowed = set()
        if isinstance(role, list):
            for r in role:
                allowed.update(ROLE_PERMISSIONS.get(r, set()))
        else:
            allowed = ROLE_PERMISSIONS.get(role, set())

        if permission not in allowed:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )
        return user
    return checker
