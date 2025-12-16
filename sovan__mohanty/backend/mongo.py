from pymongo import MongoClient,ASCENDING
from datetime import datetime

# Connect to MongoDB (adjust URI as needed)
client = MongoClient("mongodb://localhost:27017/")
db = client["activity_logs_db"]

# Collection for user activity
user_activity_collection = db["user_activity"]
# task_remarks_collection = db["task_remarks"]

# task_remarks_collection.create_index([("task_id", ASCENDING), ("timestamp", ASCENDING)])

def log_activity(user_id: int, action: str, details: dict | None = None):
    """Insert a log entry into MongoDB."""
    entry = {
        "user_id": user_id,
        "action": action,
        "details": details or {},
        "timestamp": datetime.utcnow()
    }
    user_activity_collection.insert_one(entry)
