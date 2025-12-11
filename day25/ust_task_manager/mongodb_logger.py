from pymongo import MongoClient  # Import the MongoClient to connect to MongoDB
from datetime import datetime  # Import datetime to record the timestamp of the action

# Connect to the MongoDB server running on localhost on the default port (27017)
client = MongoClient("mongodb://localhost:27017/")

# Select the 'ust_task_tracker_db' database and the 'audit_logs' collection
db = client["ust_task_tracker_db"]
audit_logs = db["audit_logs"]

def log_action(username, action, task_id):
    """
    Logs an action performed by a user on a task in the 'audit_logs' collection.
    
    Parameters:
    username (str): The name of the user performing the action.
    action (str): The action the user performed (e.g., "created", "updated", "deleted").
    task_id (str): The ID of the task being acted upon.
    """
    try:
        # Insert a new document into the 'audit_logs' collection
        audit_logs.insert_one({
            "username": username,  # Store the username performing the action
            "action": action,      # Store the action performed
            "task_id": task_id,    # Store the task ID associated with the action
            "timestamp": datetime.now()  # Store the current timestamp of the action
        })
    except:
        # If an error occurs during insertion, it is silently ignored
        pass
