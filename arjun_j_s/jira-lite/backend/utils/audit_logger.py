from datetime import datetime
from pymongo.errors import PyMongoError
from database.mongo import audit_logs_collection
 
def log_audit(action: str, emp_id: int | None = None, ref_id: int | None = None):
    try:
        audit_logs_collection.insert_one({
            "action": action,
            "emp_id": emp_id,
            "ref_id": ref_id,   # task_id / user_id / employee_id
            "timestamp": datetime.utcnow()
        })
    except PyMongoError as e:
        print(f"Failed to log audit: {str(e)}")
 