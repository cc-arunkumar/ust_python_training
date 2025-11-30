from fastapi import FastAPI
from exceptions.exception_handler import add_exception_handlers
from api.asset_api import router as asset_router
from api.employee_api import router as employee_router
from api.vendor_api import router as vendor_router
from api.maintainance_api import router as maintainance_router

from api.auth_login import jwt_router as auth_router


app = FastAPI(title="AIMS+")

app.include_router(auth_router)

add_exception_handlers(app)
# app.include_router(asset_router)
app.include_router(asset_router)
app.include_router(employee_router)
app.include_router(vendor_router)
app.include_router(maintainance_router)


@app.get("/")
def home():
    return {"status": "success", "message": "AIMS+ API Running"}
