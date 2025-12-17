from fastapi import FastAPI
from api.emp_api import emp_router
from api.task_api import task_router
from api.login_api import login_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Jira Lite")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_router, prefix="/api/v1/login")
app.include_router(task_router, prefix="/api/v1")
app.include_router(emp_router, prefix="/api/v1")