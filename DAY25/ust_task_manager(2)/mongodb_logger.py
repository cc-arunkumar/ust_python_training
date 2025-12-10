from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
collection = client.ust_mongo_db.activity_log

def log_activity(username: str, action: str, task_id: int):
    try:
        collection.insert_one({
            "username": username,
            "action": action,
            "task_id": task_id,
            "timestamp": datetime.utcnow()
        })
    except Exception as e:
        print(f"log failed: {e}")