from pymongo import MongoClient
from app.config.settings import settings

client = MongoClient(settings.mongo_uri)

mongo_db = client[settings.mongo_db]

tasks_collection = mongo_db["tasks"]
logs_collection = mongo_db["logs"]
attachments_collection=mongo_db["attachments"]