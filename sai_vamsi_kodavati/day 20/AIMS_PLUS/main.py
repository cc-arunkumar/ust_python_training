from src.api.asset_api import asset_router
from src.api.employee_api import employee_router
from src.api.maintenance_api import maintenance_router
from src.api.vendor_api import vendor_router
from fastapi import FastAPI
from src.auth.demo_jwt.main import jwt_router

app=FastAPI(title="Aims Plus Management")

app.include_router(jwt_router)
app.include_router(asset_router)
app.include_router(employee_router)
app.include_router(vendor_router)
app.include_router(maintenance_router)





