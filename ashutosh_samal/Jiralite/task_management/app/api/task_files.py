# app/api/task_files.py
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from bson import ObjectId

from app.core.database import get_db
from app.core.mongo import fs, files_collection
from app.api.task import task_exists
from app.core.security import get_current_user

router = APIRouter(prefix="/tasks", tags=["Task Files"])

@router.post("/{task_id}/files")
async def upload_file(
    task_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    # ✅ Validate task in MySQL
    if not task_exists(db, task_id):
        raise HTTPException(404, "Task not found")

    file_id = await fs.upload_from_stream(
        file.filename,
        file.file,
        metadata={"content_type": file.content_type},
    )

    await files_collection.insert_one({
        "task_id": task_id,
        "file_id": file_id,
        "filename": file.filename,
        "content_type": file.content_type,
        "uploaded_by": user["emp_id"],
        "uploaded_at": datetime.utcnow(),
    })

    return {"message": "File uploaded"}

@router.get("/{task_id}/files")
async def list_files(
    task_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    if not task_exists(db, task_id):
        raise HTTPException(404, "Task not found")

    cursor = files_collection.find({"task_id": task_id})
    files = []

    async for f in cursor:
        files.append({
            "file_id": str(f["file_id"]),
            "filename": f["filename"],
            "content_type": f["content_type"],
            "uploaded_by": f["uploaded_by"],
            "uploaded_at": f["uploaded_at"],
        })

    return files

from fastapi.responses import StreamingResponse

@router.get("/{task_id}/files/{file_id}")
async def download_file(
    task_id: int,
    file_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    if not task_exists(db, task_id):
        raise HTTPException(404, "Task not found")

    meta = await files_collection.find_one({
        "task_id": task_id,
        "file_id": ObjectId(file_id)
    })
    if not meta:
        raise HTTPException(404, "File not found")

    grid_out = await fs.open_download_stream(ObjectId(file_id))

    return StreamingResponse(
        grid_out,
        media_type=meta["content_type"],
        headers={
            "Content-Disposition": f'attachment; filename="{meta["filename"]}"'
        },
    )
