from fastapi import FastAPI
from api.training_api import router as router_model
from api.login_api import jwt_router as jwt_model

app=FastAPI(title="Training Requests")
app.include_router(jwt_model)
app.include_router(router_model)
