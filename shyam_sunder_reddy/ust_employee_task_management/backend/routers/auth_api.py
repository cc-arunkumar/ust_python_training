from fastapi import APIRouter, HTTPException, Depends
from models.auth import LoginRequest, Token
from utils.auth import authenticate_user, create_access_token, get_current_user
from datetime import timedelta

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/login", response_model=Token)
def login(credentials: LoginRequest):
	user = authenticate_user(credentials.e_id, credentials.password)
	if not user:
		raise HTTPException(status_code=401, detail="Invalid e_id or password")
	access_token_expires = timedelta(minutes=30)
	token = create_access_token(subject=str(user.e_id), expires_delta=access_token_expires)
	return {"access_token": token, "token_type": "bearer"}

@auth_router.get("/me")
def me(current_user=Depends(get_current_user)):
	return current_user
