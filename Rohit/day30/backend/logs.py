from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["jira_logs"]
logs_collection = db["activity_logs"]

def insert_log(entity: str, entity_id: int, action: str, performed_by: int, role: str, details: dict = None):
    log_entry = {
        "entity": entity,
        "entity_id": entity_id,
        "action": action,
        "performed_by": performed_by,
        "role": role,
        "timestamp": datetime.utcnow(),
        "details": details or {}
    }
    logs_collection.insert_one(log_entry)
