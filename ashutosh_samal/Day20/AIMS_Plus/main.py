from fastapi import FastAPI  # Import FastAPI for creating the API app
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware for Cross-Origin Resource Sharing
from src.api.asset_api import asset_router  # Import the asset router
from src.api.maintenance_api import maintenance_router  # Import the maintenance router
from src.api.employee_api import employee_router  # Import the employee router
from src.api.vendor_api import vendor_router  # Import the vendor router
from src.auth.jwt_auth import jwt_router,get_current_user,User
# Create FastAPI app instance
app = FastAPI(
    title="AIMS Plus - Asset Inventory Management System"  # Set the API title
)
app.include_router(jwt_router)

# Include routers for asset, maintenance, employee, and vendor
app.include_router(asset_router)  # Asset router to handle asset-related requests
app.include_router(employee_router)  # Employee router to handle employee-related requests
app.include_router(vendor_router)  # Vendor router to handle vendor-related requests
app.include_router(maintenance_router)  # Maintenance router to handle maintenance-related requests


