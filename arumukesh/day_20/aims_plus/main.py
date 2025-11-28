from fastapi import FastAPI

# Importing routers from different modules
from src.api.employee_api import router as employee_router
from src.api.maintenance_api import router as maintenance_router
from src.api.asset_api import router as asset_router
from src.api.vendor_api import router as vendor_router
from src.auth.jwt_authentication import jwt_router 

# Create FastAPI application instance
app = FastAPI(title="AIMS+")

# -------------------- Registering Routers --------------------
# Authentication router must be registered first
app.include_router(jwt_router)

# Routers for functional modules
app.include_router(employee_router)
app.include_router(maintenance_router)
app.include_router(asset_router)
app.include_router(vendor_router)

