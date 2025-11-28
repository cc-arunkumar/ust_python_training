


# Importing FastAPI and HTTPException for building the API and error handling
from fastapi import FastAPI, HTTPException

# Importing the routers for each API endpoint
from src.api.asset_api import asset_router
from src.api.employee_api import employee_router
from src.api.maintenance_api import maintenance_router
from src.api.vendor_api import vendor_router
from src.api.login_api import login_router 


# Initializing FastAPI application with a custom title
app = FastAPI(title="UST AIMS+")

app.include_router(login_router)
# Including the asset API router which will handle routes for asset operations
app.include_router(asset_router)

# Including the employee API router for employee-related operations
app.include_router(employee_router)

# Including the maintenance API router for maintenance-related operations
app.include_router(maintenance_router)

# Including the vendor API router to handle vendor-related operations
app.include_router(vendor_router)


