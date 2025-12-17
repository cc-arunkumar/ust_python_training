from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.mysql import engine, Base
from models.employees import Employee
from models.user import User
from models.task import Task
from routers.employees import emp_router
from routers.task import task_router
from routers.login import login_router
from routers.user import router as user_router

app = FastAPI(title="Jira Lite")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_router)
app.include_router(emp_router)
app.include_router(task_router)
app.include_router(user_router)