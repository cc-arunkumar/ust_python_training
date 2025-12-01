from fastapi import FastAPI
from api import router as employee_router

app = FastAPI(title="Employees Table.")

# Include router from api.py
app.include_router(employee_router)
