from fastapi import FastAPI
from employee_api import emp_router
from jwt_auth import jwt_router

app=FastAPI()

app.include_router(jwt_router)
app.include_router(emp_router)