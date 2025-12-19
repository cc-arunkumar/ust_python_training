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

# Remarks collection (separate from activity logs)
remarks_collection = db["remarks"]


def get_remarks_for_task(task_id: int):
    """Return a list of remark documents for a given task id, sorted by created_at ascending."""
    try:
        cursor = remarks_collection.find({"task_id": int(task_id)}).sort("created_at", 1)
        results = []
        for doc in cursor:
            results.append({
                "id": str(doc.get("_id")),
                "task_id": int(doc.get("task_id")),
                "comment": doc.get("comment"),
                "created_by": doc.get("created_by"),
                "created_at": doc.get("created_at"),
            })
        return results
    except Exception:
        return []


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


def save_remark(task_id: int, comment: str, created_by: Optional[int]):
    """Save a remark document linked to a task in the `remarks` collection.

    Returns the inserted document id or None on failure.
    """
    try:
        doc = {
            "task_id": int(task_id),
            "comment": comment,
            "created_by": created_by,
            "created_at": datetime.now(),
        }
        res = remarks_collection.insert_one(doc)
        return res.inserted_id
    except Exception:
        return None
