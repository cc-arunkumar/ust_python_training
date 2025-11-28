from fastapi import FastAPI
from src.api.asset_api import asset_router
from src.api.maintainence_api import maintainence_router
from src.api.vendor_api import vendor_router
from src.api.employee_api import employee_router
from src.auth.jwt_auth import jwt_router
from src.api.login_api import login_router

# Create FastAPI application instance with a custom title
app = FastAPI(title="AIMS PLUS")

app.include_router(login_router)
app.include_router(jwt_router)
# Include router for asset-related APIs
app.include_router(asset_router)

# Include router for maintenance-related APIs
app.include_router(maintainence_router)

# Include router for vendor-related APIs
app.include_router(vendor_router)

# Include router for employee-related APIs
app.include_router(employee_router)
