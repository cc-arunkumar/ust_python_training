from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.employee_api import employee_router
from routers.users_api import users_router
from routers.task_api import task_router
from routers.remark_api import remark_router
from routers.auth_api import auth_router
from middleware.error_handler import error_handler_middleware
from middleware.logging_middleware import logging_middleware
from dotenv import load_dotenv
import os

load_dotenv()
 
app = FastAPI(
    title="UST Employee Task Management",
    description="JIRA-lite Employee Management System with role-based access control",
    version="1.0.0"
)
 
# CORS Configuration for Frontend Integration
# Allow all localhost origins for development
origins = [
    "http://localhost:5173",  # Vite default port
    "http://localhost:3000",  # Alternative React port
    "http://localhost:8080",  # Current frontend port
    "http://localhost:5174",  # Vite fallback when 5173 is in use
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:5174",
]
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
)
 
# Add custom middleware
app.middleware("http")(error_handler_middleware)
app.middleware("http")(logging_middleware)

app.include_router(auth_router)
app.include_router(employee_router)
app.include_router(users_router)
app.include_router(task_router)
app.include_router(remark_router)


@app.get("/health", tags=["health"])
def health_check():
    """Simple health-check for debugging and automated tests."""
    return {"status": "ok"}