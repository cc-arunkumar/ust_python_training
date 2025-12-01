from fastapi import FastAPI
from auth import auth
from crud import crud

# Initialize FastAPI app
app = FastAPI(
    title="UST Employee Training Request Management API",
    version="1.0.0"
)

# Include routers
app.include_router(auth.router)                 # /auth/login
app.include_router(crud.router)     # /api/v1/training-requests

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to UST Training Request Management API"}
