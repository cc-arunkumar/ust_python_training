from pymongo import MongoClient
from app.core.config import MONGO_URL

client = MongoClient(MONGO_URL)
mongo_db = client["task_management_logs"]
log_collection = mongo_db["logs"]