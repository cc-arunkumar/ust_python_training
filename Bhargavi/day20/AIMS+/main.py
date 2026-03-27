
from fastapi import FastAPI

# Importing routers for different modules
from src.api.asset_api import asset_router
from src.api.maintenance_api import maintenance_router
from src.api.vendor_api import vendor_router
from src.api.employee_api import employee_router
from src.api.login_api import login_router
from src.auth.jwt_auth import jwt_router

# Create FastAPI application instance with a custom title
app = FastAPI(title="AIMS PLUS")

# Include the routers for different modules
app.include_router(login_router)
app.include_router(jwt_router)
app.include_router(asset_router)
app.include_router(maintenance_router)
app.include_router(vendor_router)
app.include_router(employee_router)

#output
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [7948] using WatchFiles
# INFO:     Started server process [9048]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
