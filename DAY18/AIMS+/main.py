# src/main.py
from fastapi import FastAPI
from src.api.asset_api import asset_router
from src.api.employee_api import emp_router
from src.api.maintanance_api import main_router
from src.api.vendor_api import vendor_router
from src.api.login_api import jwt_router


app = FastAPI(title="AIMS")

app.include_router(jwt_router)
app.include_router(asset_router)
app.include_router(emp_router)
app.include_router(main_router)
app.include_router(vendor_router)


