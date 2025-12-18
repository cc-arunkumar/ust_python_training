# Import necessary modules for MongoDB connection and handling timestamps
from pymongo import MongoClient
import gridfs
from datetime import datetime
from typing import Optional
from bson import ObjectId

# Create a MongoClient instance to connect to the local MongoDB instance
client = MongoClient("mongodb://localhost:27017/")

# Define the database and collections to store activity logs and files
db = client["ust_employee_db"]
collection = db["logs"]
fs = gridfs.GridFS(db, collection="files")


def log_activity(emp_id: Optional[int], action: str, task_id: int):
    """Insert a simple activity log document into MongoDB.

    This is best-effort; failures are swallowed to avoid breaking the main
    SQL-backed API.
    """
    try:
        collection.insert_one({
            "emp_id": emp_id,
            "action": action,
            "task_id": task_id,
            "timestamp": datetime.now(),
        })
    except Exception:
        pass


def save_task_file_bytes(task_id: int, filename: str, content: bytes, content_type: Optional[str] = None):
    """Save a file (bytes) into GridFS with metadata linking it to a task_id.

    Returns the inserted file ObjectId.
    """
    try:
        file_id = fs.put(
            content,
            filename=filename,
            contentType=content_type,
            metadata={
                "task_id": int(task_id),
                "uploaded_at": datetime.now(),
            },
        )
        return file_id
    except Exception:
        return None


def get_file_by_id(file_id: str):
    """Retrieve a GridFS file by id (string or ObjectId). Returns a dict with
    stream and metadata or None if not found.
    """
    try:
        oid = ObjectId(file_id)
        grid_out = fs.get(oid)
        return {
            "filename": grid_out.filename,
            "content_type": grid_out.content_type if hasattr(grid_out, "content_type") else None,
            "length": grid_out.length,
            "stream": grid_out,
            "metadata": grid_out.metadata,
        }
    except Exception:
        return None
