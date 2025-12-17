from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.core.config import SECRET_KEY, ALGORITHM
from app.core.database import get_db
from app.models.user import User

# 🔐 Bearer token extractor
security = HTTPBearer()


# -------------------------------------------------
# JWT CREATION
# -------------------------------------------------
def create_access_token(data: dict, expires_minutes: int = 60):
    """
    Creates JWT token.
    `data` should contain:
      - emp_id
      - roles
      - (optional) active_role
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# -------------------------------------------------
# CURRENT USER (WITH ACTIVE ROLE HANDLING)
# -------------------------------------------------
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        emp_id = payload.get("emp_id")
        roles = payload.get("roles", [])
        active_role = payload.get("active_role")

        if not emp_id or not roles:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload"
            )

        # 🔎 Validate user exists & active
        user = db.query(User).filter(User.e_id == emp_id).first()
        if not user or user.status != "ACTIVE":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not active or not found"
            )

        # -------------------------------------------------
        # DEFAULT ACTIVE ROLE LOGIC (VERY IMPORTANT)
        # -------------------------------------------------
        # If active_role is NOT present in token:
        #   - Prefer DEVELOPER (so user sees own tasks)
        #   - Else pick first role
        if not active_role:
            if "DEVELOPER" in roles:
                active_role = "DEVELOPER"
            else:
                active_role = roles[0]

        # 🔐 Validate active_role belongs to user
        if active_role not in roles:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid active role"
            )

        # ✅ Return a normalized user context
        return {
            "emp_id": emp_id,
            "roles": roles,
            "active_role": active_role
        }

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
