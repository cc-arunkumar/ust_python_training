from fastapi import FastAPI  # Importing FastAPI to create the web application
from src.api.asset_api import asset_router  # Import the asset API router to handle asset-related routes
from src.api.employee_api import employee_router  # Import the employee API router to handle employee-related routes
from src.api.vendor_api import vendor_router  # Import the vendor API router to handle vendor-related routes
from src.api.maintenance_api import maintenance_router  # Import the maintenance API router to handle maintenance-related routes
from src.auth.auth_jwt_token import jwt_router  # Import the JWT authentication router for user authentication

# Initialize FastAPI app with the title "AIMS Plus"
app = FastAPI(title="AIMS Plus")

# Include the API routers to connect the routes to the application

# Add the JWT authentication routes to the app for managing authentication and token generation
app.include_router(jwt_router)

# Add the asset-related routes to the app by including the asset API router
app.include_router(asset_router)  # Handles routes related to asset operations like creating, updating, deleting assets

# Add the employee-related routes to the app by including the employee API router
app.include_router(employee_router)  # Handles routes related to employee operations like creating, updating, deleting employees

# Add the vendor-related routes to the app by including the vendor API router
app.include_router(vendor_router)  # Handles routes related to vendor operations like adding, updating vendor details

# Add the maintenance-related routes to the app by including the maintenance API router
app.include_router(maintenance_router)  # Handles routes related to maintenance log operations like adding maintenance records

