
from fastapi import FastAPI, Depends, HTTPException, status
import os
from fastapi.staticfiles import StaticFiles

from src.services.login_api import router as login_router
from src.services.employee_api import router as employee_router
from src.services.task_api import router as task_router
from src.services.remarks_api import router as remarks_router

app = FastAPI(title="Task Manager API", version="1.0.0")
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ensure uploads directory exists and serve it at /up  loads
uploads_path = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(uploads_path, exist_ok=True)
app.mount('/uploads', StaticFiles(directory=uploads_path), name='uploads')

app.include_router(login_router)
app.include_router(employee_router)
app.include_router(task_router)
app.include_router(remarks_router)
