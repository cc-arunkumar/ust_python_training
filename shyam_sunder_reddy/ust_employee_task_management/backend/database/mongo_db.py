from pymongo import MongoClient
from typing import Optional

# Simple MongoDB connection helper. Adjust URI as needed.
MONGO_URI = "mongodb://localhost:27017"
MONGO_DB = "ust_task_logs"


def get_mongo_client() -> MongoClient:
    return MongoClient(MONGO_URI)


def get_mongo_db():
    client = get_mongo_client()
    return client[MONGO_DB]
