from src.api.login_api import jwt_router  # Import the router for JWT-based authentication
from src.api.employee_api import employee_router  # Import the router for employee-related routes
from fastapi import FastAPI  # Import FastAPI for creating the application

# Initialize the FastAPI application instance
app = FastAPI()

# Include the JWT router for handling login and authentication-related routes
app.include_router(jwt_router)

# Include the employee router for handling employee-related API routes
app.include_router(employee_router)
