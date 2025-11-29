from employee_api import router as employee_router
from fastapi import FastAPI

# Create a FastAPI application instance with a title
app = FastAPI(title="Employee Management")

# Include the employee API router so all employee-related routes
# (POST, GET, PUT, DELETE) will be available under `/employees`
app.include_router(employee_router)
