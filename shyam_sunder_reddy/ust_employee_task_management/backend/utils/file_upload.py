from gridfs import GridFS
from database.mongo_db import mongodb
 
from bson import ObjectId
from database.mongo_db import fs
 
fs = GridFS(mongodb)
 
 
def save_file(file):
    content = file.file.read()
    file_id = fs.put(
        content,
        filename=file.filename,
        content_type=file.content_type
    )
    return str(file_id)
 
 
 
 
def delete_file(file_id: str):
    try:
        fs.delete(ObjectId(file_id))
    except Exception:
        pass  # safe delete (file may already be gone)