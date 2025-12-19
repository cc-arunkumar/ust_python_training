from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from services.database import engine, Base
from services.employee_service import Employee
from services.task_service import Task
from routers.employee_routers import emp_router
from routers.user_router import user_router
from routers.task_routers import task_router
from routers.log_router import log_router
from middleware.logging_middleware import LoggingMiddleware
from routers.auth_routers import auth_router
from routers.file_upload import file_router
from routers.task_remarks import task_remarks_router

# Create FastAPI app (only once!)
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add logging middleware
app.add_middleware(LoggingMiddleware)

# Create uploads directory if it doesn't exist
UPLOAD_DIR = "uploads/task-files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Mount static files for serving uploaded files
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Register routers
app.include_router(auth_router)      # Auth should be first
app.include_router(emp_router)
app.include_router(user_router)
app.include_router(task_router)
app.include_router(task_remarks_router)  # Task remarks
app.include_router(file_router)
app.include_router(log_router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Task Management API", "status": "running"}

# Startup event
@app.on_event("startup")
def startup():
    print("🚀 Starting application...")
    print("📦 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully")
    print(f"📁 Upload directory: {UPLOAD_DIR}")
    print("🌐 API running at: http://127.0.0.1:8000")
    print("📚 Docs available at: http://127.0.0.1:8000/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=800)