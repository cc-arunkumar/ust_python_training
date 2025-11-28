# Importing the routers for different modules of the AIMS Plus management system
from src.api.asset_api import asset_router        # Router for asset-related operations
from src.api.employee_api import employee_router  # Router for employee-related operations
from src.api.maintenance_api import maintenance_router  # Router for maintenance-related operations
from src.api.vendor_api import vendor_router      # Router for vendor-related operations
from fastapi import FastAPI                       # FastAPI class for creating the application
from src.api.login_api import jwt_router          # Router for JWT-based authentication

# Create an instance of FastAPI with a custom title for the application
app = FastAPI(title="AIMS Plus management")

# Include the JWT authentication router for login-related operations
app.include_router(jwt_router)

# Include the asset router for CRUD operations on asset inventory
app.include_router(asset_router)

# Include the employee router for managing employee-related data
app.include_router(employee_router)

# Include the maintenance router for handling maintenance records
app.include_router(maintenance_router)

# Include the vendor router for managing vendor information and operations
app.include_router(vendor_router)
