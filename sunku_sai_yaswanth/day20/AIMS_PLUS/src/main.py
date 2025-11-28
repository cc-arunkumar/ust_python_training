from api.asset_api import asset_router
from api.employee_api import employee_router
from api.maintenance_api import maintenance_router
from api.vendor_api import vendor_router
from fastapi import FastAPI
from api.login_api import jwt_router
app=FastAPI(title="AIMS Plus managment")

app.include_router(jwt_router)
app.include_router(asset_router)
app.include_router(employee_router)
app.include_router(maintenance_router)
app.include_router(vendor_router)