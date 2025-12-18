from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = MongoClient(MONGO_URL)
mongo_db = client["ust_employee_db"]

user_collection = mongo_db["users"]
log_collection = mongo_db["logs"]
file_collection = mongo_db["files"]
