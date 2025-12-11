from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["ust_task_manager"]  # Database name
logs_collection = db["activity_logs"]  # Collection for logs

# Function to log user activity
def log_activity(username: str, action: str, task_id: int):
    try:
        log_entry = {
            "username": username,
            "action": action,
            "task_id": task_id,
            "timestamp": datetime.timezone.utc()
        }
        logs_collection.insert_one(log_entry)
    except Exception as e:
        print(f"Error logging activity: {e}")
