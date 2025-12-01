from fastapi import FastAPI
from src.api.training_request_api import training_request_router
from src.api.login_api import login_router

# Initialize FastAPI application with a custom title
app = FastAPI(title="UST Employee Training Request Management")

# Include the login router for authentication endpoints
app.include_router(login_router)

# Include the training request router for CRUD operations on training requests
app.include_router(training_request_router)