from datetime import datetime
from database import audit_logs


def log_action(username, action, task_id):
    try:
        audit_logs.insert_one({
            "username": username,
            "action": action,
            "task_id": task_id,
            "timestamp": datetime.now()
        })
    except:
        pass