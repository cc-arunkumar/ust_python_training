# Import FastAPI framework for building APIs
from fastapi import FastAPI

# Import the employee API router from the application's API module
from src.api.employee_api import employee_router
from src.api.login_api import login_router

# Initialize the FastAPI application instance
# The 'title' parameter sets the name of the API in the interactive docs (Swagger UI / ReDoc)
app = FastAPI(title="Employee Management System")

# Include the employee API router into the main application
# This allows all endpoints defined in 'employee_api' to be registered under the app
app.include_router(login_router)
app.include_router(employee_router)