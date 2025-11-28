from fastapi import FastAPI
from src.api import asset_api, employee_api, vendor_api, maintainance_api
from src.auth import jwt_auth   # <-- import your JWT router

# Initialize FastAPI app
app = FastAPI(title="AIMS Plus")

# Include routers for each module
app.include_router(asset_api.router, prefix="/assets", tags=["Assets"])
app.include_router(employee_api.router, prefix="/employees", tags=["Employees"])
app.include_router(vendor_api.router, prefix="/vendors", tags=["Vendors"])
app.include_router(maintainance_api.router, prefix="/maintenance", tags=["Maintenance"])

# Include JWT authentication router
app.include_router(jwt_auth.jwt_router, tags=["Auth"])

# Register global exception handlers

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to AIMS+ Asset & Employee Management System"}
