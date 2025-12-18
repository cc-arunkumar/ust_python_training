from bson.binary import Binary
import base64
from typing import Optional, Dict, Any
from database.mongo_connection import tasks, files
from bson.objectid import ObjectId
from datetime import datetime

def bson_to_json(data):
    """Convert MongoDB types to JSON-safe format"""
    if isinstance(data, dict):
        return {k: bson_to_json(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [bson_to_json(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    elif isinstance(data, Binary):
        return base64.b64encode(data).decode('utf-8')
    return data

def upload_file_to_task(task_id: str, file_data: Dict[str, Any], uploaded_by: int):
    """Upload file to MongoDB and link to task"""
    try:
        oid = ObjectId(task_id)
        
        # Store file in files collection
        file_doc = {
            "task_id": oid,
            "file_name": file_data["file_name"],
            "file_type": file_data["file_type"],
            "file_size": file_data["file_size"],
            "file_data": Binary(file_data["file_data"]),
            "uploaded_by": uploaded_by,
            "uploaded_at": datetime.now()
        }
        file_result = files.insert_one(file_doc)
        file_id = str(file_result.inserted_id)
        
        # Link file to task
        task_update = {
            "$push": {
                "files": {
                    "file_id": file_id,
                    "file_name": file_data["file_name"],
                    "file_type": file_data["file_type"],
                    "file_size": file_data["file_size"],
                    "uploaded_by": uploaded_by,
                    "uploaded_at": datetime.now()
                }
            }
        }
        task_result = tasks.update_one({"_id": oid}, task_update)
        
        return {
            "file_id": file_id,
            "task_id": task_id,
            "modified_count": task_result.modified_count
        }
    except Exception as e:
        raise Exception(f"File upload failed: {str(e)}")

def get_task_files(task_id: str):
    """Get all files for a task"""
    try:
        oid = ObjectId(task_id)
        task = tasks.find_one(
            {"_id": oid}, 
            {"files": 1, "_id": 0}
        )
        if not task:
            raise ValueError("Task not found")
        return task.get("files", [])
    except Exception as e:
        raise Exception(str(e))

def get_file_by_id(file_id: str):
    """Get specific file by ID"""
    try:
        oid = ObjectId(file_id)
        file_doc = files.find_one({"_id": oid})
        if not file_doc:
            raise ValueError("File not found")
        
        # Convert Binary back to base64 for frontend
        file_doc["file_data"] = base64.b64encode(file_doc["file_data"]).decode('utf-8')
        return file_doc
    except Exception as e:
        raise Exception(str(e))
