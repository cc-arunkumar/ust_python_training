from app.routers.auth_router import router as auth_router
from app.routers.employee_router import router as employee_router
from app.routers.task_router import router as task_router
from app.routers.task_file_router import router as task_file_router
from app.routers.user_router import router as user_router

__all__ = [
    "auth_router",
    "employee_router",
    "task_router",
    "task_file_router",
    "user_router"
]