from fastapi import FastAPI
# from auth_jwt import jwt_router  # Assuming this handles authentication routes
from apis import employee_router  # Assuming employee_router handles employee-related operations
from login_api import jwt_router
# Create an instance of FastAPI with a custom title for the application
app = FastAPI(title="Employee Management API")

# Include the JWT authentication router for login-related operations
app.include_router(jwt_router)

# Include the employee router for CRUD operations on employee data
app.include_router(employee_router)
