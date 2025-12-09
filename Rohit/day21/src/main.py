from fastapi import FastAPI,APIRouter
from src.api.employee_api import employee_router


app = FastAPI()

app.include_router(employee_router)
