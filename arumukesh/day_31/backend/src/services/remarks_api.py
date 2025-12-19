from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime

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
        })

    return results


@router.post(
    "/api/v1/tasks/{t_id}/remarks",
    status_code=status.HTTP_201_CREATED,
)
async def post_remark(
    t_id: int,
    payload: RemarkPayload,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Validate task exists
    task = db.query(Tasks).filter(Tasks.t_id == t_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Only participants (assignee/reviewer/creator) or admin/manager can post
    if not _is_authorized_for_task(db, current_user, t_id):
        raise HTTPException(status_code=403, detail="Not authorized to post remarks")

    if not payload.message or not payload.message.strip():
        raise HTTPException(status_code=400, detail="Message is required")

    doc = {
        "task_id": t_id,
        "message": payload.message.strip(),
        "from_emp_id": str(current_user.emp_id),
        "timestamp": datetime.utcnow().isoformat(),
    }

    result = remarks_coll.insert_one(doc)
    doc["id"] = str(result.inserted_id)

    return doc
