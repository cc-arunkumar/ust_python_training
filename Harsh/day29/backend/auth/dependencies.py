from fastapi import Depends, HTTPException, status
from auth.auth import get_current_user
from schemas.user import CurrentUser
 
def admin_only(current_user: CurrentUser = Depends(get_current_user)):
    if "ADMIN" not in current_user.role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access only"
        )
    return current_user
 
 