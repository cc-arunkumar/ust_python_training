from fastapi import FastAPI
from api.employee_api import router as employee_router
from api.login_api import auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(employee_router)
