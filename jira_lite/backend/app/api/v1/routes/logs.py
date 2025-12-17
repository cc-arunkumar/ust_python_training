from fastapi import APIRouter
from app.db.mongodb import logs_collection

router = APIRouter(
    prefix="/logs",
    tags=["Logs"]
)


@router.get("/")
def get_logs():
    logs = []
    for log in logs_collection.find().sort("timestamp", -1):
        log["_id"] = str(log["_id"])
        logs.append(log)
    return logs
