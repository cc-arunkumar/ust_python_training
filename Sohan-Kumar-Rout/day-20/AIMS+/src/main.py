import datetime
import pymysql
from fastapi import FastAPI, HTTPException
from config.db_connection import get_connection
from auth.jwt_auth import jwt_router,User,Depends,get_curr_user
from api.asset_api import router as asset_router
from api.vendor_api import router as vendor_router
from api.maintenance_api import router as maintenance_router
from api.employee_api import router as employee_router

app = FastAPI()

app.include_router(jwt_router)
app.include_router(asset_router)
app.include_router(vendor_router)
app.include_router(maintenance_router)
app.include_router(employee_router)

