from fastapi import APIRouter, Depends
from utils.auth_dependency import get_current_user
from database.mongodb import log_collection
from datetime import datetime

log_router = APIRouter(
    prefix="/logs",
    tags=["Logs"]
)


@log_router.get("/")
def get_logs(user=Depends(get_current_user)):
    return list(log_collection.find({}, {"_id": 0}))
