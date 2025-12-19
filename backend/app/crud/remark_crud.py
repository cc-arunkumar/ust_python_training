from bson import ObjectId
from fastapi import HTTPException
from datetime import datetime, timezone
from app.database.mysql_connection import get_connection
from app.database.mongodb_connection import remarks_collection
from sqlalchemy.orm import Session
from app.schemas.schemas import TaskSchema
from app.utils.file_upload import save_file, delete_file
from app.utils.mongo_serializer import serialize_mongo
from app.database.mongodb_connection import notifications_collection


def _has_role(user, role_name: str) -> bool:
    """Return True if user has role_name. Checks both `roles` (list) and `role` (string) attributes."""
    if not user:
        return False
    roles = getattr(user, "roles", None)
    if roles and isinstance(roles, (list, tuple)):
        return any(str(r).strip().lower() == role_name.strip().lower() for r in roles)
    # fallback to single attribute `role` or `role` string inside object
    single = getattr(user, "role", None)
    if single:
        return str(single).strip().lower() == role_name.strip().lower() or (
            isinstance(single, str) and role_name.strip().lower() in str(single).strip().lower()
        )
    return False


def add_remark(task_id: int, comment: str, e_id: int, file=None, role: str = None, user=None):
    """Add a remark for a task.

    Authorization rules (implemented):
    - Admin: can add remarks to any task.
    - Manager: can add remarks for tasks they created or tasks they are reviewer for or tasks assigned to them.
    - Developer: can add remarks for tasks assigned to them.

    This relaxes phase-only restrictions and bases permissions on relationship to the task.
    """
    session: Session = get_connection()

    try:
        task = session.query(TaskSchema).filter(TaskSchema.t_id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        user_eid = getattr(user, "e_id", None)

        # Admins can always add remarks
        if _has_role(user, "Admin"):
            allowed = True
        # Managers may add remarks if they created the task, are reviewer, or are assigned
        elif _has_role(user, "Manager"):
            allowed = (
                (task.created_by is not None and task.created_by == user_eid)
                or (task.reviewer is not None and task.reviewer == user_eid)
                or (task.assigned_to is not None and task.assigned_to == user_eid)
            )
        # Developers may add remarks if they are assigned to the task
        elif _has_role(user, "Developer"):
            allowed = task.assigned_to is not None and task.assigned_to == user_eid
        else:
            allowed = False

        if not allowed:
            raise HTTPException(status_code=403, detail="Not allowed to add remark for this task")

        # Handle file upload
        file_id = None
        file_name = None
        if file:
            file_id = save_file(file)
            file_name = file.filename

        remark = {
            "task_id": task_id,
            "comment": comment,
            "created_by": e_id,
            "file_id": file_id,
            "file_name": file_name,
            "created_at": datetime.now(timezone.utc),
        }

        result = remarks_collection.insert_one(remark)
        remark["_id"] = result.inserted_id
        # Create notifications for other participants (assigned user and reviewer)
        try:
            notif_targets = []
            if getattr(task, "assigned_to", None) and task.assigned_to != user_eid:
                notif_targets.append(int(task.assigned_to))
            if getattr(task, "reviewer", None) and task.reviewer != user_eid:
                # ensure reviewer is included (if different from assignee)
                if int(task.reviewer) not in notif_targets and task.reviewer != user_eid:
                    notif_targets.append(int(task.reviewer))

            for to_eid in notif_targets:
                notifications_collection.insert_one(
                    {
                        "type": "remark",
                        "task_id": int(task_id),
                        "remark_id": str(result.inserted_id),
                        "to_eid": int(to_eid),
                        "from_eid": int(user_eid) if user_eid else None,
                        "message": f"New remark on task {task_id}",
                        "read": False,
                        "created_at": datetime.now(timezone.utc),
                    }
                )
        except Exception:
            # non-fatal: notifications should not block remark creation
            pass
        return serialize_mongo(remark)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()


def get_remarks_by_task(task_id: int):
    docs = list(remarks_collection.find({"task_id": task_id}))
    return [serialize_mongo(d) for d in docs]


def get_all_remarks_for_user(user):
    """Return remarks visible to the given user.

    - Admin and Manager: see all remarks
    - Developer: see remarks they created or remarks on tasks assigned to them
    """
    try:
        if _has_role(user, "Admin") or _has_role(user, "Manager"):
            docs = list(remarks_collection.find({}).sort("created_at", -1).limit(1000))
            return [serialize_mongo(d) for d in docs]

        # Developer: fetch remarks created by them or on tasks assigned to them
        user_eid = getattr(user, "e_id", None)
        if _has_role(user, "Developer") and user_eid is not None:
            # remarks created by this user
            own = list(remarks_collection.find({"created_by": int(user_eid)}))

            # remarks whose task is assigned to this user
            # find unique task_ids from remarks, then query mysql for assignments
            task_ids = list({d.get("task_id") for d in list(remarks_collection.find({})) if d.get("task_id")})

            assigned_task_ids = []
            if task_ids:
                session: Session = get_connection()
                try:
                    tasks = (
                        session.query(TaskSchema.t_id)
                        .filter(TaskSchema.t_id.in_(task_ids), TaskSchema.assigned_to == int(user_eid))
                        .all()
                    )
                    assigned_task_ids = [t[0] for t in tasks]
                finally:
                    session.close()

            assigned = []
            if assigned_task_ids:
                assigned = list(remarks_collection.find({"task_id": {"$in": assigned_task_ids}}))

            # merge unique remarks
            combined = {str(r.get("_id")): r for r in (own + assigned)}
            docs = list(combined.values())
            # sort by created_at desc
            docs.sort(key=lambda x: x.get("created_at") or 0, reverse=True)
            return [serialize_mongo(d) for d in docs]

        # default: no remarks
        return []
    except Exception:
        return []


def update_remark(remark_id: str, comment: str | None, file, e_id: int, role: str):
    remark = remarks_collection.find_one({"_id": ObjectId(remark_id)})
    if not remark:
        raise HTTPException(status_code=404, detail="Remark not found")

    # Only admin or owner can update
    if not (role and role.upper() == "ADMIN") and remark.get("created_by") != e_id:
        raise HTTPException(status_code=403, detail="Not allowed to update this remark")

    update_data = {}
    if comment:
        update_data["comment"] = comment

    if file:
        if remark.get("file_id"):
            try:
                delete_file(remark["file_id"])
            except Exception:
                pass

        file_id = save_file(file)
        update_data["file_id"] = file_id
        update_data["file_name"] = file.filename

    if not update_data:
        raise HTTPException(status_code=400, detail="Nothing to update")

    update_data["updated_at"] = datetime.now(timezone.utc)
    remarks_collection.update_one({"_id": ObjectId(remark_id)}, {"$set": update_data})
    updated = remarks_collection.find_one({"_id": ObjectId(remark_id)})
    return serialize_mongo(updated)


def delete_remark_by_id(remark_id: str, role: str, user):
    remark = remarks_collection.find_one({"_id": ObjectId(remark_id)})
    if not remark:
        raise HTTPException(status_code=404, detail="Remark not found")

    # Only ADMIN or owner can delete
    if not (role and role.upper() == "ADMIN") and remark.get("created_by") != getattr(user, "e_id", None):
        raise HTTPException(status_code=403, detail="Not allowed to delete this remark")

    if remark.get("file_id"):
        try:
            delete_file(str(remark["file_id"]))
        except Exception:
            pass

    remarks_collection.delete_one({"_id": ObjectId(remark_id)})
    return {"message": "Remark and file deleted successfully", "remark_id": remark_id}