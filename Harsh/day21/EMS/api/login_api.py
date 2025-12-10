# auth_router.py
from fastapi import APIRouter, Form,HTTPException
from auth.employee_auth import create_access_token

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    # Replace with DB user validation
    if username == "admin" and password == "secret":
        token = create_access_token({"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
