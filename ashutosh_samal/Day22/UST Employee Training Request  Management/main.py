from fastapi import FastAPI  # Import FastAPI for creating the API app
from fastapi.middleware.cors import CORSMiddleware 
from api import emp_router
from auth import jwt_router,get_current_user,User

app = FastAPI(
    title="Employee Training System"  # Set the API title
)
app.include_router(jwt_router)
# Include routers for asset, maintenance, employee, and vendor
app.include_router(emp_router)  # Employee router to handle employee-related requests
