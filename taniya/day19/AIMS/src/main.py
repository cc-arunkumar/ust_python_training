from fastapi import FastAPI, HTTPException, status
from datetime import timedelta
# from src.api.employee_api import
# from api.vendors_api import vendor_router
from src.api.vendors_api import vendor_router
from src.api.login_api import jwt_router
from src.api.employee_api import employee_router
from src.api.maintenance_api import maintenance_router
from src.api.asset_api import assets_router

app = FastAPI()

app.include_router(jwt_router)
app.include_router(maintenance_router)
app.include_router(employee_router)
app.include_router(assets_router)
app.include_router(vendor_router)