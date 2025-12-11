from pymongo import MongoClient
from datetime import datetime
from typing import Dict
 
 
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update this if needed
db = client["ust_task_manager_db"]  # MongoDB database name
activity_logs = db["activity_logs"]  # MongoDB collection for activity logs
 
def log_activity(username: str, action: str, task_id: int):
    """
    Logs user activity in MongoDB
    """
    log_entry = {
        "username": username,
        "action": action,
        "task_id": task_id,
        "timestamp": datetime.utcnow()  # Log the current timestamp
    }
 
    try:
        # Insert the log entry into the collection
        activity_logs.insert_one(log_entry)
    except Exception as e:
        # If an error occurs during logging, print it
        print(f"Error logging activity to MongoDB: {e}")
 