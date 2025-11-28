from fastapi import FastAPI, HTTPException
from src.api.asset_api import asset_router
from src.api.vendor_api import vendor_router
from src.api.maintenence_api import maintenance_router
from src.api.employee_api import employee_router
from src.auth.jwt_auth import jwt_router
from src.api.login_api import login_router

app = FastAPI(title="UST  ")

app.include_router(login_router)
app.include_router(jwt_router)
app.include_router(asset_router)
app.include_router(vendor_router)
app.include_router(maintenance_router)
app.include_router(employee_router)