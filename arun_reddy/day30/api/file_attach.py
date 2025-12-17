from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from bson import ObjectId
import os
import shutil
from datetime import datetime
from authorise.authorisation import role_guard
from authorise.dependencies import get_current_user
from database.mongodb_connection import tasks as task_collection

task_router = APIRouter(prefix="/tasks", tags=["Tasks"])


@task_router.post(
    "/{task_id}/attach",
    dependencies=[Depends(role_guard(["developer", "manager"]))]
)
def attach_file_to_task(
    task_id: str,
    file: UploadFile = File(...),
    current_user=Depends(get_current_user)
):
    # ---------- VALIDATE TASK ----------
    try:
        task = task_collection.find_one({"_id": ObjectId(task_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid task id")

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # ---------- OPTIONAL: OWNERSHIP CHECK ----------
    if current_user.role == "developer":
        if task.get("assigned_to") != current_user.emp_id:
            raise HTTPException(status_code=403, detail="Not your task")

    if current_user.role == "manager":
        if task.get("manager_id") != current_user.emp_id:
            raise HTTPException(status_code=403, detail="Not your task")

    # ---------- SAVE FILE ----------
    upload_dir = f"uploads/tasks/{task_id}"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # ---------- UPDATE TASK DOCUMENT ----------
    attachment_info = {
        "filename": file.filename,
        "path": file_path,
        "uploaded_by": current_user.emp_id,
        "uploaded_at": datetime.utcnow()
    }

    task_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$push": {"attachments": attachment_info}}
    )

    return {
        "message": "File attached successfully",
        "task_id": task_id,
        "filename": file.filename
    }
