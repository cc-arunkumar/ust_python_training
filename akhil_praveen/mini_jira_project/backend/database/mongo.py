from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket
from config.config import Config

# Async Mongo Client
client = AsyncIOMotorClient(Config.MONGODB_URL)

# Motor database (IMPORTANT)
db = client[Config.MONGODB_DATABASE]

# Collections
reviews_collection = db["reviews"]
audit_logs_collection = db["audit_logs"]

# GridFS (now correct)
fs = AsyncIOMotorGridFSBucket(db)
