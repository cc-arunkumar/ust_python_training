from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from utils.auth_dependency import get_current_user
from utils.authorization import require_permission
from database.mongodb import file_collection
from datetime import datetime
import os
import uuid

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

file_router = APIRouter(
    prefix="/files",
    tags=["File Upload"]
)


@file_router.post(
    "/upload",
    dependencies=[Depends(require_permission("file:upload"))]
)
def upload_file(
    file: UploadFile = File(...),
    user=Depends(get_current_user)
):
    file_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{file_id}_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    metadata = {
        "file_id": file_id,
        "filename": file.filename,
        "path": file_path,
        "uploaded_by": user["emp_id"],
        "uploaded_at": datetime.utcnow()
    }

    file_collection.insert_one(metadata)

    return {
        "message": "File uploaded successfully",
        "file_id": file_id
    }
