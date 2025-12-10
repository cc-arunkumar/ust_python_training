from pymongo import MongoClient
from datetime import datetime, timezone

# Connect to MongoDB Atlas or local instance
mongo_client = MongoClient("mongodb+srv://msovan928_db_user:sovan@clusterfastapi.yrq0el1.mongodb.net/")
mongo_db = mongo_client["ust_mongo_db"]
activity_log = mongo_db["activity_log"]

def log_activity(action: str, task_id: int, username: str):
    activity_log.insert_one({
        "action": action,          
        "task_id": task_id,
        "user": username,
        "timestamp": datetime.now(timezone.utc).isoformat()
    })
