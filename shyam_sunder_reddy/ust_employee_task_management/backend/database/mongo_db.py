from pymongo import MongoClient
from typing import Optional
from gridfs import GridFS
# Simple MongoDB connection helper. Adjust URI as needed.
MONGO_URI = "mongodb://localhost:27017"
MONGO_DB = "ust_task_logs"
 
 
client = MongoClient(MONGO_URI)
 
mongodb = client[MONGO_DB]
 
# Collections
remarks_collection = mongodb["remarks"]
logs_collection = mongodb["logs"]
# GridFS for file upload / download
fs = GridFS(mongodb)
# client = MongoClient(MONGO_URI)