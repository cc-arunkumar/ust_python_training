
from fastapi import FastAPI, Depends, HTTPException,status

from src.services.login_api import router as login_router
from src.services.employee_api import router as employee_router
from src.services.task_api import router as task_router
app = FastAPI(title="Task Manager API", version="1.0.0")
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(login_router)
app.include_router(employee_router)
app.include_router(task_router)
