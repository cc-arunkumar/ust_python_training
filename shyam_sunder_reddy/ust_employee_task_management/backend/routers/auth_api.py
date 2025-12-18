from fastapi import APIRouter, HTTPException, Depends
from models.auth import LoginRequest, AuthResponse
from utils.auth import create_access_token, get_current_user
from crud.users_crud import get_user_by_id
from datetime import timedelta

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login", response_model=AuthResponse)
def login(credentials: LoginRequest):
	# Explicitly fetch user and compare password so we can surface clearer failures
	try:
		user = get_user_by_id(credentials.e_id)
	except HTTPException:
		# Do not reveal which part failed to the client; return generic message
		raise HTTPException(status_code=401, detail="Invalid e_id or password")

	if not user or user.password != credentials.password:
		raise HTTPException(status_code=401, detail="Invalid e_id or password")

	access_token_expires = timedelta(minutes=30)
	token = create_access_token(subject=str(user.e_id), expires_delta=access_token_expires)

	# Return token and the user object so frontend can store roles/status
	user_data = user if hasattr(user, '__iter__') else user
	# ensure password not returned by pydantic model
	user_dict = user.dict() if hasattr(user, 'dict') else {}
	user_dict.pop('password', None)
	return {"access_token": token, "token_type": "bearer", "user": user_dict}


@auth_router.get("/me")
def me(current_user=Depends(get_current_user)):
	return current_user
