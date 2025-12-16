from pymongo import MongoClient
from app.core.config import settings

_client = MongoClient(settings.mongo_uri)
_db = _client[settings.mongo_db]

def get_mongo_db():
    return _db
