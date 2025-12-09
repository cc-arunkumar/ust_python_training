from fastapi import FastAPI
from empl_api import training_router
from auth import jwt_router
app=FastAPI(
    title="UST Employee Training Request Management "
)
app.include_router(jwt_router)
app.include_router(training_router)