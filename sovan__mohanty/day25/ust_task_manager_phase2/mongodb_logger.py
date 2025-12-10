from pymongo import MongoClient
from datetime import datetime,timezone

client = MongoClient("mongodb://localhost:27017/")
mongo_db = client["ust_task_manager_logs"]
logs = mongo_db["activity"]

def log_activity(username: str, action: str, task_id: int):
    try:
        logs.insert_one({
            "username": username,
            "action": action,
            "task_id": task_id,
            "timestamp": datetime.now(timezone.utc)
        })
    except Exception as e:
        print("Logging failed:", e) 
