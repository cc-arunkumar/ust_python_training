from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
from datetime import datetime
import uuid
import io

from app.db.mongodb import attachments_collection, tasks_collection
from app.api.deps import get_current_user
from app.utils.logger import create_log

router = APIRouter(
    prefix="/attachments",
    tags=["Attachments"]
)

# ---------------------------------------------------
# UPLOAD ATTACHMENT (ONLY REVIEWER)
# ---------------------------------------------------
@router.post("/{task_id}", status_code=201)
def upload_attachment(
    task_id: str,
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_user)
):
    task = tasks_collection.find_one({"task_id": task_id})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Only reviewer can upload
    if task.get("reviewer") != current_user["emp_id"]:
        raise HTTPException(
            status_code=403,
            detail="Only reviewer can upload attachments"
        )

    file_bytes = file.file.read()

    attachment_doc = {
        "attachment_id": str(uuid.uuid4()),
        "task_id": task_id,
        "filename": file.filename,
        "content_type": file.content_type,
        "file_data": file_bytes,
        "uploaded_by": current_user["emp_id"],
        "uploaded_at": datetime.now(),
        "is_active": True
    }

    attachments_collection.insert_one(attachment_doc)

    create_log(
        emp_id=current_user["emp_id"],
        roles=current_user["roles"],
        module="ATTACHMENTS",
        action="UPLOAD",
        resource_id=attachment_doc["attachment_id"],
        description="Attachment uploaded",
        status="SUCCESS"
    )

    return {
        "message": "Attachment uploaded successfully",
        "attachment_id": attachment_doc["attachment_id"]
    }


# ---------------------------------------------------
# DOWNLOAD ATTACHMENT (STREAMING)
# ---------------------------------------------------
@router.get("/{attachment_id}/download")
def download_attachment(
    attachment_id: str,
    current_user: dict = Depends(get_current_user)
):
    attachment = attachments_collection.find_one({
        "attachment_id": attachment_id,
        "is_active": True
    })

    if not attachment:
        raise HTTPException(status_code=404, detail="Attachment not found")

    task = tasks_collection.find_one({"task_id": attachment["task_id"]})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    roles = current_user["roles"]
    emp_id = current_user["emp_id"]

    # Role-based access
    if "admin" in roles:
        pass
    elif "manager" in roles and task["created_by"] == emp_id:
        pass
    elif "developer" in roles and task["assigned_to"] == emp_id:
        pass
    elif emp_id == attachment["uploaded_by"]:
        pass
    else:
        raise HTTPException(status_code=403, detail="Access denied")

    return StreamingResponse(
        io.BytesIO(attachment["file_data"]),
        media_type=attachment["content_type"],
        headers={
            "Content-Disposition": f'attachment; filename="{attachment["filename"]}"'
        }
    )


# ---------------------------------------------------
# SOFT DELETE ATTACHMENT
# ---------------------------------------------------
@router.delete("/{attachment_id}")
def delete_attachment(
    attachment_id: str,
    current_user: dict = Depends(get_current_user)
):
    attachment = attachments_collection.find_one({
        "attachment_id": attachment_id,
        "is_active": True
    })

    if not attachment:
        raise HTTPException(status_code=404, detail="Attachment not found")

    # Only admin or uploader can delete
    if (
        "admin" not in current_user["roles"]
        and attachment["uploaded_by"] != current_user["emp_id"]
    ):
        raise HTTPException(status_code=403, detail="Not allowed")

    attachments_collection.update_one(
        {"attachment_id": attachment_id},
        {"$set": {"is_active": False}}
    )

    create_log(
        emp_id=current_user["emp_id"],
        roles=current_user["roles"],
        module="ATTACHMENTS",
        action="DELETE",
        resource_id=attachment_id,
        description="Attachment soft deleted",
        status="SUCCESS"
    )

    return {"message": "Attachment deleted successfully"}
