from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import engine, Base
from app.middleware.logging_middleware import MongoLoggingMiddleware
from fastapi.middleware.cors import CORSMiddleware

# Correct imports — directly import the router instances
from app.routers.auth_router import router as auth_router
from app.routers.employee_router import router as employee_router
from app.routers.task_router import router as task_router
from app.routers.task_file_router import router as task_file_router
from app.routers.user_router import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="UST Employee Task Manager")

app.add_middleware(MongoLoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    # Allow both common Vite dev ports (5173, 5174) and local hostnames during development
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Correct way: include the router directly
app.include_router(auth_router)
app.include_router(employee_router)
app.include_router(task_router)
app.include_router(task_file_router)
app.include_router(user_router)

@app.get("/")
def health_check():
    return {"status": "Backend running"}