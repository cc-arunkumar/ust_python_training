from pymongo import MongoClient   # Import MongoClient to connect with MongoDB
from pydantic import BaseModel    # Import BaseModel from Pydantic for data validation
from datetime import datetime     # Import datetime to handle timestamps

client = MongoClient("mongodb://localhost:27017/")   # Create a MongoDB client connected to local server

db = client["ust_mongo_db"]   # Access (or create) a database named 'ust_mongo_db'

# db.create_collection("logger")   # Uncomment to explicitly create a collection named 'logger'
# print("collection created")      # Uncomment to confirm collection creation

class Log(BaseModel):   # Define a Pydantic model for structured logging
    username: str       # Username of the person performing the action
    action: str         # Description of the action performed
    task_id: int        # Task identifier (numeric)
    timestamp: datetime = datetime.now()   # Default timestamp set to current time

logg = db.logger   # Reference to the 'logger' collection in the database