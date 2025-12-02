from fastapi import FastAPI
from api.training_api import router as request_router
from api.login_api import router as login_router
app = FastAPI(title="Request Table.")

app.include_router(login_router)
app.include_router(request_router)