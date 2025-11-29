from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

SECRET_KEY = "AIMSPLUSSECRET"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30

security = HTTPBearer()


# Create token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


# Verify token & authentication dependency
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload     # returning user info
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


# Router for testing authentication
from fastapi import APIRouter
jwt_router = APIRouter(prefix="/auth", tags=["Auth"])

@jwt_router.get("/verify")
def verify_user(user: dict = Depends(verify_token)):
    return {"message": "Token verified", "user": user}
