from fastapi import APIRouter, Depends, HTTPException
from app.core.security import get_current_user
from app.database.mongodb_connection import notifications_collection
from bson import ObjectId
from datetime import datetime

notification_router = APIRouter(prefix="/notifications", tags=["notifications"])


def _serialize_notification(doc: dict) -> dict:
    if not doc:
        return doc
    return {
        "id": str(doc.get("_id")),
        "type": doc.get("type"),
        "task_id": doc.get("task_id"),
        "to_eid": doc.get("to_eid"),
        "from_eid": doc.get("from_eid"),
        "message": doc.get("message"),
        "read": bool(doc.get("read", False)),
        "created_at": doc.get("created_at").isoformat() if doc.get("created_at") else None,
    }


@notification_router.get("/list")
def list_notifications(unread: bool = False, current_user=Depends(get_current_user)):
    query = {"to_eid": int(current_user.e_id)}
    if unread:
        query["read"] = False
    docs = notifications_collection.find(query).sort("created_at", -1).limit(100)
    return [ _serialize_notification(d) for d in docs ]


@notification_router.put("/{notif_id}/read")
def mark_notification_read(notif_id: str, current_user=Depends(get_current_user)):
    try:
        oid = ObjectId(notif_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid notification id")

    doc = notifications_collection.find_one({"_id": oid})
    if not doc:
        raise HTTPException(status_code=404, detail="Notification not found")
    if int(doc.get("to_eid")) != int(current_user.e_id):
        raise HTTPException(status_code=403, detail="Not allowed")

    notifications_collection.update_one({"_id": oid}, {"$set": {"read": True}})
    updated = notifications_collection.find_one({"_id": oid})
    return _serialize_notification(updated)


@notification_router.put("/mark_all_read")
def mark_all_read(current_user=Depends(get_current_user)):
    res = notifications_collection.update_many({"to_eid": int(current_user.e_id), "read": False}, {"$set": {"read": True}})
    return {"matched": res.matched_count, "modified": res.modified_count}
