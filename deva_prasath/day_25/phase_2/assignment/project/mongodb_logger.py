# Import necessary modules for MongoDB connection and handling timestamps
from pymongo import MongoClient
from datetime import datetime

# Create a MongoClient instance to connect to the local MongoDB instance
client = MongoClient("mongodb://localhost:27017/")

# Define the database and collection to store activity logs
db = client["ust_mongo_db"]
collection = db["activity_logs"]

# Function to log user activity to the MongoDB collection
def log_activity(username: str, action: str, task_id: int):
    try:
        # Insert a document with the activity details into the collection
        collection.insert_one({
            "username": username,  # User performing the action
            "action": action,      # Action taken 
            "task_id": task_id,    # Associated task ID
            "timestamp": datetime.now()  # Timestamp of when the action occurred
        })
    except Exception:
        # If any exception occurs, silently pass (could be improved by logging the exception)
        pass
