from pymongo import MongoClient
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")  # MongoDB URI from .env or default to local
client = MongoClient(MONGO_URI)  # Create a MongoClient to connect to MongoDB
db = client["task_manager"]  # Select the "task_manager" database
logs_collection = db["activity_logs"]  # Select the "activity_logs" collection for logging

# Function to log user activity
def log_activity(username: str, action: str, task_id: int):
    try:
        # Create a log entry to store the activity in MongoDB
        log_entry = {
            "username": username,  # User performing the action
            "action": action,  # Type of action (e.g., CREATE, UPDATE, DELETE)
            "task_id": task_id,  # ID of the task involved in the action
            "timestamp": datetime.now(timezone.utc)  # Timestamp of the activity in UTC
        }
        
        # Insert the log entry into the MongoDB collection
        logs_collection.insert_one(log_entry)
    except Exception as e:
        print(f"Error logging activity: {e}")  # Print error if the insert fails
