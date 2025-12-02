from fastapi import FastAPI
from api.login_api import router as login_router
from api.training_api import router 

app = FastAPI(title="ETM")


app.include_router(login_router)
app.include_router(router)