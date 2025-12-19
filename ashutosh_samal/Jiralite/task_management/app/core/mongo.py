from pymongo import MongoClient
from app.core.config import MONGO_URL

client = MongoClient(MONGO_URL)
mongo_db = client["task_management_logs"]
log_collection = mongo_db["logs"]

# app/core/mongo.py
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket

client = AsyncIOMotorClient("mongodb://localhost:27017")
mongo_db = client.task_files
fs = AsyncIOMotorGridFSBucket(mongo_db)
files_collection = mongo_db.files
