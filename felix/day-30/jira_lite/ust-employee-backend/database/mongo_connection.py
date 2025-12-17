from pymongo import MongoClient   # Import MongoClient to connect with MongoDB
from models.task_model import TaskCreate,TaskUpdate,Task
from datetime import datetime
client = MongoClient("mongodb://localhost:27017/")   # Create MongoDB client connected to local server

db = client["ust_jira_lite"]
# db.create_collection("tasks") 
# db.create_collection("logs") 
# print("MongoDB collections 'tasks' and 'logs' created in database 'ust_jira_lite'.")

tasks = db.tasks
logs = db.logs

