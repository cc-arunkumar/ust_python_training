from datetime import datetime
from pymongo.database import Database

class LogService:
    def __init__(self, db: Database):
        self.col = db["logs"]

    def log_event(self, level: str, message: str, actor_id: str | None = None, context: str | None = None):
        entry = {
            "level": level,
            "message": message,
            "actor_id": actor_id,
            "timestamp": datetime.utcnow(),
            "context": context,
        }
        self.col.insert_one(entry)
