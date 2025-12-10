from pymongo import MongoClient
from datetime import datetime,timezone

# Function: Establish and return a connection to MongoDB 
client = MongoClient("mongodb://localhost:27017")
db = client.ust_task_manager_logs

#function to log activity in mongodb
def log_activity(username: str, action: str, task_id: int):
    log = {
        "username": username,
        "action": action,
        "task_id": task_id,
        "timestamp": datetime.now(timezone.utc)
    }
    db.activity_logs.insert_one(log)
