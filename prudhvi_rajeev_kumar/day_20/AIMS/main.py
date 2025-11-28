# main.py
from fastapi import FastAPI, HTTPException, status
from datetime import timedelta
from src.authentication.auth import (
    DEMO_USERNAME, DEMO_PASSWORD,
    create_access_token, Token, LoginRequest,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from src.api.asset_api import register_asset_api
from src.api.employee_api import register_employee_api
from src.api.maintenance_api import register_maintenance_api
from src.api.vendor_api import register_vendor_api

app = FastAPI(title="AIMS API with JWT")

# --- Login endpoint ---
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password."
        )
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")

# --- Register all APIs ---
register_asset_api(app)
register_employee_api(app)
register_maintenance_api(app)
register_vendor_api(app)
