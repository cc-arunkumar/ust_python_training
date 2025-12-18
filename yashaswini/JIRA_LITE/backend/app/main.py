from fastapi import FastAPI

from app.api.v1.routes.auth import router as auth_router
from app.api.v1.routes.users import router as user_router
from app.api.v1.routes.employees import router as employee_router
from app.api.v1.routes.tasks import router as task_router
from app.api.v1.routes.attachments import router as attachment_router

app = FastAPI(title="UST Employee Management")


app.include_router(auth_router)


app.include_router(user_router)
app.include_router(employee_router)
app.include_router(task_router)
app.include_router(attachment_router)
