# from pymongo import MongoClient
# from datetime import datetime

# # MongoDB connection for activity logging
# MONGO_CLIENT = MongoClient("mongodb://localhost:27017")
# mongo_db = MONGO_CLIENT["task_manager_logs"]
# activity_log_collection = mongo_db["activity_log"]

# # MySQL connection string for SQLAlchemy (ensure the credentials are correct for your setup)
# DATABASE_URL = "mysql+pymysql://username:password1@localhost:3306/ust_task_manager_db"  # Replace 'username' and 'password' with actual values

# def log_user_activity(username: str, action: str, task_id: int):
#     """
#     Logs user activity in MongoDB.
#     """
#     log_entry = {
#         "username": username,
#         "action": action,
#         "task_id": task_id,
#         "timestamp": datetime.utcnow()  # Use UTC timestamp
#     }
    
#     # Insert the log entry into the MongoDB collection
#     try:
#         activity_log_collection.insert_one(log_entry)
#         print(f"Activity logged: {action} on Task {task_id} by {username}")
#     except Exception as e:
#         print(f"Error logging activity: {e}")

# # Example usage (feel free to replace with actual data when calling this)
# # log_user_activity("rahul", "CREATE", 101)  # Example of logging activity
