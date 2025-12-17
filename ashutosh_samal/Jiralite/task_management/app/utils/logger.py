from datetime import datetime
from app.core.mongo import log_collection

def log_action(emp_id: int, action: str, details: str):
    log_collection.insert_one({
        "emp_id": emp_id,
        "action": action,
        "details": details,
        "timestamp": datetime.utcnow()
    })