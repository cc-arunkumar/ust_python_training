from api.employee_api import router as emp_router
from fastapi import FastAPI

app=FastAPI()

app.include_router(emp_router)

