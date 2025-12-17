# app/mongo.py
from pymongo import MongoClient
import os

# You can move this to environment variables if you prefer
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://msovan928_db_user:sovan@clusterfastapi.yrq0el1.mongodb.net/")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "task_audit_db")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

activity_collection = db["activity_logs"]


def log_activity(data: dict):
    """
    Insert a single activity document into MongoDB.
    `data` should already be JSON-serializable.
    """
    activity_collection.insert_one(data)
