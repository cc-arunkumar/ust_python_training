from fastapi import FastAPI  # Import FastAPI for creating the API app
from fastapi.middleware.cors import CORSMiddleware 
from api import employee_router

app = FastAPI(
    title="Employee Management System"  # Set the API title
)

# Include routers for asset, maintenance, employee, and vendor
app.include_router(employee_router)  # Employee router to handle employee-related requests
