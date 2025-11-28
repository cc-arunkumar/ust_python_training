from fastapi import FastAPI
from src.api.asset_model_api.main import asset_router
from src.api.employee_directory_api.main import employee_router
from src.api.maintainence_api.main import maintain_router
from src.api.vendor_api.main import vendor_router
from src.api.login_api.main import login_router
# Initialize the FastAPI app with the title "AIMS Plus"
app = FastAPI(title="AIMS Plus")

# Include the routers for different parts of the application
# Each router corresponds to a specific resource (assets, employees, vendors, maintenance)
app.include_router(login_router)
app.include_router(asset_router)  
app.include_router( employee_router)  
app.include_router(maintain_router)  
app.include_router(vendor_router)  
