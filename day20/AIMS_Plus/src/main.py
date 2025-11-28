from fastapi import FastAPI
from src.api.asset_api import asset_router
from src.api.employee_api import emp_router
from src.api.maintenance_api import log_router
from src.api.vendor_api import vendor_router
from src.api.login_api import login_router

app = FastAPI(title="AIMS Plus")  # Initialize FastAPI application with title

app.include_router(login_router)
app.include_router(asset_router)   # Register asset routes
app.include_router(emp_router)     # Register employee routes
app.include_router(log_router)     # Register maintenance log routes
app.include_router(vendor_router)  # Register vendor routes
