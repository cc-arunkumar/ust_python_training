# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from jwt import create_access_token
from routes import router as training_router

app = FastAPI(title="Training Request API")

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/auth/login")
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "password123":
        token = create_access_token(request.username)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

app.include_router(training_router)
