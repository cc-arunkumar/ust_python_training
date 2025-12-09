from fastapi import Depends, FastAPI
from src.api.login_api import jwt_router
from src.api.training_api import training_router   # <-- import router, not service
from src.auth.jwt_auth import get_current_user
from src.models.login_model import User

app = FastAPI()

app.include_router(jwt_router)
app.include_router(training_router)

# @app.get("/")
# def get_user(current_user: User = Depends(get_current_user)):
#     return "Hello from the server side"
