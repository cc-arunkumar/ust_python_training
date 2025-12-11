from pymongo import MongoClient   
from datetime import datetime    

# Create a connection to the local MongoDB server running on default port 27017
mongo_client = MongoClient("mongodb://localhost:27017/")

# Access (or create if not exists) the database named 'ust_task_tracker'
db = mongo_client["ust_task_tracker"]

# Access (or create if not exists) the collection named 'logs' inside the database
collection = db["logs"]

def mongodb_logs(username: str, action: str, task_id: int):
    try:
        # Create a log entry document with user details, action performed, task ID, and current timestamp
        log_entry = {
            "username": username,       
            "action": action,           
            "task_id": task_id,         
            "timestamp": datetime.now() 
        }

        # Insert the log entry into the 'logs' collection
        collection.insert_one(log_entry)

    except Exception as e:
        # Print an error message if logging fails for any reason
        print("Logging failed:", e)