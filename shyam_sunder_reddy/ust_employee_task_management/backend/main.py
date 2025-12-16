from fastapi import FastAPI
from routers.employee_api import employee_router
from routers.users_api import users_router
from routers.task_api import task_router
from routers.remark_api import remark_router
from routers.auth_api import auth_router

app = FastAPI(title="UST Employee Task Management")

app.include_router(auth_router)

app.include_router(employee_router)
app.include_router(users_router)
app.include_router(task_router)
app.include_router(remark_router)