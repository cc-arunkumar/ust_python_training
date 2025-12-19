from fastapi import APIRouter, Depends, HTTPException, status, Request, UploadFile, File, Form
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime
from typing import List, Optional
import os
from uuid import uuid4

from src.services.auth import get_current_user, get_db
from src.database.db_creation import Tasks, User
from sqlalchemy.orm import Session

router = APIRouter()

# MongoDB client (local)
MONGO_URI = "mongodb://localhost:27017/"
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client['task_manager_db']
remarks_coll = mongo_db['task_remarks']


class RemarkPayload(BaseModel):
    message: str


def _is_authorized_for_task(db: Session, user: User, task_id: int) -> bool:
    task = db.query(Tasks).filter(Tasks.t_id == task_id).first()
    if not task:
        return False

    uid = str(user.emp_id)
    # Admins allowed
    roles = []
    if hasattr(user, "roles") and isinstance(user.roles, (list, tuple)):
        roles = [r.lower() for r in user.roles if isinstance(r, str)]
    elif hasattr(user, "role") and isinstance(user.role, str):
        roles = [r.strip().lower() for r in user.role.split(",") if r.strip()]

    if "admin" in roles or "manager" in roles:
        return True

    # Developer/other: must be assigned_to, reviewer or creator
    if task.assigned_to == uid or task.reviewer == uid or task.created_by == uid:
        return True

    return False


@router.get(
    "/api/v1/tasks/{t_id}/remarks",
    status_code=status.HTTP_200_OK,
)
async def get_remarks(
    t_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Authorization
    task = db.query(Tasks).filter(Tasks.t_id == t_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if not _is_authorized_for_task(db, current_user, t_id):
        raise HTTPException(status_code=403, detail="Not authorized to view remarks")

    docs = list(remarks_coll.find({"task_id": t_id}).sort("timestamp", 1))
    # sanitize ObjectId and datetime
    results = []
    for d in docs:
        results.append({
            "id": str(d.get("_id")),
            "task_id": d.get("task_id"),
            "message": d.get("message"),
            "from_emp_id": d.get("from_emp_id"),
            "timestamp": d.get("timestamp"),
            "attachments": d.get("attachments", []),
        })

    return results


@router.post(
    "/api/v1/tasks/{t_id}/remarks",
    status_code=status.HTTP_201_CREATED,
)
async def post_remark(
    t_id: int,
    message: Optional[str] = Form(None),
    files: Optional[List[UploadFile]] = File(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    request: Request = None,
):
    # Validate task exists
    task = db.query(Tasks).filter(Tasks.t_id == t_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Only participants (assignee/reviewer/creator) or admin/manager can post
    if not _is_authorized_for_task(db, current_user, t_id):
        raise HTTPException(status_code=403, detail="Not authorized to post remarks")

    # If message wasn't provided via form (e.g. client sent JSON), try to read JSON body
    if (not message or not message.strip()):
        try:
            if request is not None and request.headers.get('content-type', '').lower().startswith('application/json'):
                body = await request.json()
                if isinstance(body, dict) and 'message' in body:
                    message = body.get('message')
        except Exception:
            # ignore json parse errors
            pass

    if (not message or not (isinstance(message, str) and message.strip())) and not files:
        raise HTTPException(status_code=400, detail="Either message or file is required")

    attachments = []
    # prepare upload directory relative to backend folder
    upload_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
    upload_dir = os.path.join(upload_root, 'remarks')
    os.makedirs(upload_dir, exist_ok=True)

    if files:
        for upload in files:
            try:
                contents = await upload.read()
                ext = os.path.splitext(upload.filename)[1]
                stored_name = f"{uuid4().hex}{ext}"
                dest_path = os.path.join(upload_dir, stored_name)
                with open(dest_path, 'wb') as f:
                    f.write(contents)

                base = str(request.base_url).rstrip('/')
                url = f"{base}/uploads/remarks/{stored_name}"
                attachments.append({
                    "filename": upload.filename,
                    "stored_filename": stored_name,
                    "content_type": upload.content_type,
                    "size": len(contents),
                    "url": url,
                })
            except Exception:
                # if any file fails to save, continue with others
                continue

    doc = {
        "task_id": t_id,
        "message": (message.strip() if message else ""),
        "from_emp_id": str(current_user.emp_id),
        "timestamp": datetime.utcnow().isoformat(),
        "attachments": attachments,
    }

    result = remarks_coll.insert_one(doc)
    doc["id"] = str(result.inserted_id)

    return doc
