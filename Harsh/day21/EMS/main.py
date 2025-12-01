from fastapi import FastAPI
from api.employee_api import router   

app = FastAPI()

# Register the router
app.include_router(router)
