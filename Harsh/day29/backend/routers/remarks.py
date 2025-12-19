from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from bson import ObjectId
from database.mongo import remarks_collection, fs
from database.mysql import get_db
from auth.auth import get_current_user
from models.task import Task
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional
from pymongo.errors import PyMongoError
from io import BytesIO

router = APIRouter(prefix="/tasks", tags=["Remarks"])


@router.post("/{task_id}/remarks")
async def create_remark(
    task_id: int,
    text: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    # Validate task exists
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    file_id = None
    filename = None
    try:
        if file:
            filename = file.filename
            # upload to GridFS
            file_id = await fs.upload_from_stream(filename, file.file, metadata={
                "task_id": task_id,
                "uploaded_by": user.user_id,
                "uploaded_at": datetime.utcnow()
            })
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")

    remark_doc = {
        "task_id": task_id,
        "text": text or "",
        "file_id": str(file_id) if file_id else None,
        "filename": filename if filename else None,
        "created_by": user.user_id,
        "created_at": datetime.utcnow(),
    }

    try:
        res = await remarks_collection.insert_one(remark_doc)
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Failed to save remark: {str(e)}")

    remark_doc["_id"] = str(res.inserted_id)
    return remark_doc


@router.get("/{task_id}/remarks")
async def list_remarks(task_id: int):
    cursor = remarks_collection.find({"task_id": task_id}).sort("created_at", 1)
    items = []
    async for doc in cursor:
        items.append({
            "id": str(doc.get("_id")),
            "text": doc.get("text"),
            "file_id": doc.get("file_id"),
            "filename": doc.get("filename"),
            "created_by": doc.get("created_by"),
            "created_at": doc.get("created_at"),
        })
    return items


@router.get("/remarks/attachments/{file_id}")
async def download_attachment(file_id: str):
    try:
        oid = ObjectId(file_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid file id")

    try:
        grid_out = await fs.open_download_stream(oid)
    except Exception:
        raise HTTPException(status_code=404, detail="File not found")

    headers = {"Content-Disposition": f"attachment; filename=\"{grid_out.filename}\""}

    async def file_iterator():
        while True:
            chunk = await grid_out.readchunk()
            if not chunk:
                break
            yield chunk

    return StreamingResponse(file_iterator(), media_type="application/octet-stream", headers=headers)


@router.delete("/remarks/attachments/{file_id}")
async def delete_attachment(file_id: str, user=Depends(get_current_user)):
    """Delete a GridFS file by id and remove or update any remark documents that reference it.

    Behavior:
    - Delete the file from GridFS.
    - For remarks that reference this file_id: if the remark has no text, delete the remark document; otherwise unset file_id and filename so the remark remains as text-only.
    """
    try:
        oid = ObjectId(file_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid file id")

    # Delete file from GridFS
    try:
        await fs.delete(oid)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File not found or could not be deleted: {str(e)}")

    # Update/remove remarks referencing this file
    try:
        cursor = remarks_collection.find({"file_id": file_id})
        async for doc in cursor:
            text = doc.get("text") or ""
            if not text.strip():
                # no text, remove the remark doc entirely
                await remarks_collection.delete_one({"_id": doc["_id"]})
            else:
                # keep remark but remove file refs
                await remarks_collection.update_one({"_id": doc["_id"]}, {"$unset": {"file_id": "", "filename": ""}})
    except Exception:
        # best effort; file has been deleted, but remarks update failed
        raise HTTPException(status_code=500, detail="Failed to update remark records after deleting file")

    return {"detail": "Attachment deleted"}
