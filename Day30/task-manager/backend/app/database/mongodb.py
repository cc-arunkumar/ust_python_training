"""from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_URI)

mongo_db = client["task_manager_logs"]
api_logs_collection = mongo_db["api_logs"]
"""

from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
mongo_db = client["task_manager_logs"]
api_logs_collection = mongo_db["api_logs"]