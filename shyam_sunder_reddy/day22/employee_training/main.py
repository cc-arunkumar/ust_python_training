from employee_api import emp_router
from fastapi import FastAPI
from jwt_auth import jwt_router

app=FastAPI(title="Employee Training management system")

app.include_router(jwt_router)
app.include_router(emp_router)