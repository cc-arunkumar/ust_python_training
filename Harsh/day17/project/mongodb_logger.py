from pymongo import MongoClient
from datetime import datetime

# Adjust if your MongoDB DSN differs
client = MongoClient("mongodb://localhost:27017/")
db = client["ust_task_manager_logs"]
logs_collection = db["activity_logs"]

def log_activity(username: str, action: str, task_id: int):
    try:
        logs_collection.insert_one({
            "username": username,
            "action": action,            # CREATE, UPDATE, DELETE
            "task_id": task_id,
            "timestamp": datetime.utcnow()
        })
    except Exception:
        # Logging failures must NEVER break the API
        pass
