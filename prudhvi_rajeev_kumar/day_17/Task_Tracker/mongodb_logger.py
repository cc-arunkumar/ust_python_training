from datetime import datetime
from typing import Optional
from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "ust_task_manager_logs"
COLLECTION = "activity"

_client: Optional[MongoClient] = None

def _get_client() -> MongoClient:
    global _client
    if _client is None:
        _client = MongoClient(MONGO_URL)
    return _client

def log_activity(username: str, action: str, task_id: int) -> None:
    try:
        doc = {
            "username": username,
            "action": action, 
            "task_id": task_id,
            "timestamp": datetime.utcnow(),
        }
        client = _get_client()
        client[DB_NAME][COLLECTION].insert_one(doc)
    except Exception:
        pass
