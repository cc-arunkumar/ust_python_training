# mongodb_logger.py
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["ust_task_tracker_db"]
audit_logs = db["audit_logs"]

def log_action(username, action, task_id):
    try:
        audit_logs.insert_one({
            "username": username,
            "action": action,
            "task_id": task_id,
            "timestamp": datetime.utcnow()
        })
    except:
        pass  # Logging must NOT break API
