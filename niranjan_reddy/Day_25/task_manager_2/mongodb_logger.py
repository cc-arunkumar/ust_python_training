from pymongo import MongoClient
from datetime import datetime

# Connect to the MongoDB server at the specified URI
mongo_client = MongoClient("mongodb://localhost:27017/")  # MongoDB connection URI
db = mongo_client["ust_task_tracker"]  # Access the "ust_task_tracker" database
collection = db["logs"]  # Access the "logs" collection within the database

# Function to log actions performed on tasks in MongoDB
def mongodb_logs(username: str, action: str, task_id: int):
    try:
        # Create a log entry with relevant details
        log_entry = {
            "username": username,  # Username of the person performing the action
            "action": action,  # Action performed (e.g., CREATE, UPDATE, DELETE)
            "task_id": task_id,  # ID of the task being affected
            "timestamp": datetime.now()  # Timestamp of the action (current time)
        }
        
        # Insert the log entry into the "logs" collection
        collection.insert_one(log_entry)
    
    except Exception as e:
        print("Logging failed:", e)  # Print an error message if logging fails
