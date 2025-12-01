from fastapi import FastAPI
from api.emp_api import employee_router
app=FastAPI(
    title="Employee Management"
)

app.include_router(employee_router)