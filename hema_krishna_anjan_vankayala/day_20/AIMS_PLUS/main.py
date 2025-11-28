from fastapi import FastAPI
from src.api.asset_api import asset_router
from src.api.maintenance_api import maintenance_router
from src.api.employee_api import employee_router
from src.api.vendor_api import vendors_router
from src.auth.jwt_auth import jwt_router
# Initialize FastAPI app with a title
app = FastAPI(title="AIMS Plus")

# Register routers for different modules
app.include_router(jwt_router)
# Asset management endpoints
app.include_router(asset_router)     

# Maintenance log endpoints   
app.include_router(maintenance_router)  

# Employee directory endpoints
app.include_router(employee_router)    

# Vendor master endpoints 
app.include_router(vendors_router)     
