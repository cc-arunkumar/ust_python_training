from datetime import datetime
from database.mongo_db import get_mongo_db


def log_action(action: str, details: dict):
	"""Insert a log document into MongoDB 'logs' collection."""
	try:
		db = get_mongo_db()
		entry = {
			"action": action,
			"details": details,
			"timestamp": datetime.now()
		}
		db.logs.insert_one(entry)
	except Exception:
		# Do not raise further to avoid breaking API flow if logging fails
		pass
