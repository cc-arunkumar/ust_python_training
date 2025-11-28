from fastapi import FastAPI
from src.api.asset_api import asset_router
from src.api.employee_api import employee_router
from src.api.maintenance_api import maintenance_router
from src.api.vendor_api import vendor_router
from src.api.login_api import jwt_router

# Initialize the FastAPI app with the title "AIMS Plus"
app = FastAPI(title="AIMS+ (AssetInventory Management System - Advanced Edition)")

# Include the routers for different parts of the application
# Each router corresponds to a specific resource (assets, employees, vendors, maintenance)
app.include_router(jwt_router)
app.include_router(asset_router)  
app.include_router(employee_router)  
app.include_router(vendor_router)  
app.include_router(maintenance_router)  
