import logging
import datetime
from pymongo import MongoClient, errors

# --- Database Setup ---
client = MongoClient("mongodb://localhost:27017/")
db = client["ust_mongo_db"]
conn = db["loggers"]

# --- Custom Logging Handler ---
class MongoHandler(logging.Handler):
    def __init__(self, collection):
        logging.Handler.__init__(self)
        self.collection = collection

    def emit(self, record):
        try:
            log_entry = {
                "level": record.levelname,
                "message": record.getMessage(),
                "timestamp": datetime.datetime.now(),
                "module": record.module,
                "funcName": record.funcName,
                "lineNo": record.lineno
            }
            self.collection.insert_one(log_entry)
        except errors.PyMongoError as e:
            # Fallback: print error if MongoDB insert fails
            print(f"Failed to write log to MongoDB: {e}")

# --- Configure Logger ---
logger = logging.getLogger("mongoLogger")
logger.setLevel(logging.INFO)

mongo_handler = MongoHandler(conn)
logger.addHandler(mongo_handler)

# --- Usage Example ---
# logger.info("Application started successfully")
# logger.warning("This is a warning message")
# logger.error("Something went wrong in the database operation")
