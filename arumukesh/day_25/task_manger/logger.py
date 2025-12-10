# logger.py
import datetime
from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017/")
log_db = mongo_client["task_manager_logs"]
log_collection = log_db["logs"]

def log_action(user_id: int, action: str, details: dict = None):
    log_entry = {
        "user_id": user_id,
        "action": action,
        "details": details or {},
        "timestamp": datetime.datetime.now()
    }
    log_collection.insert_one(log_entry)
