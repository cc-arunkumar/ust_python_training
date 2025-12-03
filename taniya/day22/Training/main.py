from fastapi import FastAPI
from practice.api.training_api import employee_router

app=FastAPI()
app.include_router(employee_router)
