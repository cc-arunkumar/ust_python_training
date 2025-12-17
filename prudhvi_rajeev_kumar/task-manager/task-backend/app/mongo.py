from pymongo import MongoClient

# Hardcode MongoDB URI and Database Name
MONGO_URI = "mongodb://localhost:27017"
MONGO_DB_NAME = "ust_auth_db"

# Connect to MongoDB using the URI
client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

# Specify the collection
activity_collection = db["activity_logs"]

def log_activity(data: dict):
    """
    Insert a single activity document into MongoDB.
    `data` should already be JSON-serializable.
    """
    activity_collection.insert_one(data)
