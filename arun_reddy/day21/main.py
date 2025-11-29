from api import emp_router
from fastapi import FastAPI

# Create a FastAPI application instance
# The 'title' parameter sets the name shown in the interactive docs (Swagger UI)
app = FastAPI(title="Employee Management System")

# Include the employee router
# This attaches all endpoints defined in emp_router (CRUD operations for employees)
# under the prefix "/employees"
app.include_router(emp_router)
