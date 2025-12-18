from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["ust_mongo_db"]
collection = db["activity_log"]

def log_activity(username: str, action: str, task_id: int):
    log_entry = {
        "username": username,
        "action": action,
        "task_id": task_id,
        "timestamp": datetime.utcnow()
    }
    collection.insert_one(log_entry)
