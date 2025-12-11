from pymongo import MongoClient

def get_mongo_connection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["ust_mongo_db"]
    return db