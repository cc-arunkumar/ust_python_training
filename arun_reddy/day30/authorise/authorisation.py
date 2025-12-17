from fastapi import Depends, HTTPException, status
from typing import List
from authorise.dependencies import get_current_user
from Models.user_model import UserSchema


def role_guard(allowed_roles: List[str]):
    """
    Role-based authorization dependency.
    allowed_roles: ["admin"], ["manager"], ["admin", "manager"], etc.
    """
    def _guard(current_user: UserSchema = Depends(get_current_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Role '{current_user.role}' is not authorized"
            )
        return current_user

    return _guard
