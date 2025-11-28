from src.models.assetsinventory import AssetInventory
from src.models.employeedirectory import EmployeeDirectory
from src.models.maintenancelog import MaintenanceLog
from src.models.vendormaster import VendorMaster
from fastapi import FastAPI, HTTPException
from src.auth.jwt_auth import jwt_router
from src.api.asset_api import asset_router
from src.api.employee_api import employee_router
from src.api.maintenance_api import maintenance_router
from src.api.vendor_api import vendor_router

import csv


# Initialize FastAPI application with a custom title
app = FastAPI(title="UST AIMS PLUS")

# Register routers for different modules
# Each router handles CRUD operations for its respective entity
app.include_router(jwt_router)
app.include_router(asset_router)        # Asset Inventory APIs
app.include_router(employee_router)     # Employee Directory APIs
app.include_router(maintenance_router)  # Maintenance Log APIs
app.include_router(vendor_router)       # Vendor Master APIs