from fastapi import FastAPI
from api.employee_api import emp_router
from api.login_api import login_router
from auth_jwt import jwt_router
app=FastAPI(title="Employee INFO")
app.include_router(login_router)
app.include_router(jwt_router)
app.include_router(emp_router)