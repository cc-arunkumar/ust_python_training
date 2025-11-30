from fastapi import FastAPI
from practice.config.db_connection import get_connection
from practice.api.orders_api import order_router
app=FastAPI()
app.include_router(order_router)