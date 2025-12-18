from fastapi import FastAPI
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
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Add this import if missing

app = FastAPI()


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


# ... rest of your code (imports, routers, middleware, startup event)
app.include_router(emp_router)
app.include_router(user_router)
app.include_router(task_router)


app.include_router(auth_router)
app.include_router(file_router)
app.include_router(log_router)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)



