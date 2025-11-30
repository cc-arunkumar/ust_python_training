from fastapi import FastAPI
from src.api.employee_api import employee_router
from src.config.db_connection import get_connection
app=FastAPI()
app.include_router(employee_router)