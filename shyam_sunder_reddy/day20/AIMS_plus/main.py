from fastapi import FastAPI
from src.api.asset_api import asset_router
from src.api.employee_api import employee_router
from src.api.maintenance_api import maintenance_router
from src.api.vendor_api import vendor_router
from src.api.login_api import jwt_router
# Initialize FastAPI application with a project title
app = FastAPI(title="AIMS Plus")

# -------------------------------
# Register API routers
# -------------------------------

app.include_router(jwt_router)

# Asset management endpoints (CRUD operations for assets)
app.include_router(asset_router)

# Employee management endpoints (CRUD operations for employees)
app.include_router(employee_router)

# Maintenance log endpoints (CRUD operations for maintenance records)
app.include_router(maintenance_router)

# Vendor management endpoints (CRUD operations for vendors)
app.include_router(vendor_router)
