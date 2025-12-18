from bson import ObjectId
from fastapi import HTTPException
from datetime import datetime, timezone
from database.sql_db import get_connection
from database.mongo_db import remarks_collection
from sqlalchemy.orm import Session
from schema.task_schema import TaskSchema
from utils.file_upload import save_file, delete_file
from utils.mongo_serializer import serialize_mongo


def _is_manager(user) -> bool:
    return hasattr(user, "role") and ("Manager" in user.role if isinstance(user.role, list) else "Manager" in str(user.role))


def _is_developer(user) -> bool:
    return hasattr(user, "role") and ("Developer" in user.role if isinstance(user.role, list) else "Developer" in str(user.role))


def add_remark(task_id: int, comment: str, e_id: int, file=None, role: str = None, user=None):
    """Add a remark for a task with authorization checks based on task status and user role."""
    session: Session = get_connection()

    try:
        task = session.query(TaskSchema).filter(TaskSchema.t_id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        task_status = (task.status or "").upper()

        # Authorization based on task status
        if task_status == "REVIEW":
            if not _is_manager(user):
                raise HTTPException(status_code=403, detail="Only managers can add remarks in the REVIEW phase.")
        elif task_status == "IN_PROGRESS":
            if not _is_developer(user):
                raise HTTPException(status_code=403, detail="Only developers can add remarks in the IN_PROGRESS phase.")
        else:
            raise HTTPException(status_code=400, detail="Task phase does not allow adding remarks.")

        # Handle file upload
        file_id = None
        file_name = None
        if file:
            file_id = save_file(file)
            file_name = file.filename

        # Create the remark element with its own ObjectId so it can be addressed later
        remark = {
            "_id": ObjectId(),
            "comment": comment,
            "created_by": e_id,
            "file_id": file_id,
            "file_name": file_name,
            "created_at": datetime.now(timezone.utc),
        }

        # Upsert a single document per task and push the remark into the remarks array
        resp = remarks_collection.update_one(
            {"task_id": task_id},
            {
                "$setOnInsert": {"task_id": task_id},
                "$push": {"remarks": remark},
            },
            upsert=True,
        )

        # Return the serialized remark element
        return serialize_mongo(remark)
    except Exception as e:
        raise HTTPException(e)
    finally:
        session.close()


# def get_remarks_by_task(task_id: int):
#     # Support two storage formats for backward compatibility:
#     # 1) New format: a single document per task with an embedded `remarks` array
#     # 2) Legacy format: one Mongo document per remark with a top-level task_id

#     # Try the new in-place format first
#     doc = remarks_collection.find_one({"task_id": task_id, "remarks": {"$exists": True}})
#     if doc and doc.get("remarks"):
#         remarks = doc.get("remarks", [])
#         serialized = []
#         for r in remarks:
#             if isinstance(r.get("_id"), ObjectId):
#                 r["_id"] = str(r["_id"])
#             serialized.append(r)
#         return serialized

#     # Fallback to legacy format: multiple remark documents with top-level fields
#     docs = list(remarks_collection.find({"task_id": task_id, "remarks": {"$exists": False}}))
#     if not docs:
#         return []
#     return [serialize_mongo(d) for d in docs]

def get_remarks_by_task(task_id: int):
    """
    Returns ONE task document with embedded remarks
    """
    return remarks_collection.find_one({"task_id": task_id})

def update_remark(remark_id: str, comment: str | None, file, e_id: int, role: str):
    # Find the document that contains the remark element
    # First try to update an embedded remark (new format)
    parent = remarks_collection.find_one({"remarks._id": ObjectId(remark_id)})
    if not parent:
        # Fallback: maybe this is a legacy top-level remark document
        legacy = remarks_collection.find_one({"_id": ObjectId(remark_id)})
        if legacy:
            # Only admin or owner can update
            if not (role and role.upper() == "ADMIN") and legacy.get("created_by") != e_id:
                raise HTTPException(status_code=403, detail="Not allowed to update this remark")

            update_data = {}
            if comment:
                update_data["comment"] = comment
            if file:
                if legacy.get("file_id"):
                    try:
                        delete_file(legacy["file_id"])
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
        raise HTTPException(status_code=404, detail="Remark not found")

    # locate remark element
    remark_elem = None
    for r in parent.get("remarks", []):
        if str(r.get("_id")) == str(remark_id) or (isinstance(r.get("_id"), ObjectId) and r.get("_id") == ObjectId(remark_id)):
            remark_elem = r
            break

    if not remark_elem:
        raise HTTPException(status_code=404, detail="Remark not found")

    # Only admin or owner can update
    if not (role and role.upper() == "ADMIN") and remark_elem.get("created_by") != e_id:
        raise HTTPException(status_code=403, detail="Not allowed to update this remark")

    update_fields = {}
    if comment:
        update_fields["remarks.$.comment"] = comment

    if file:
        # delete old file if present
        if remark_elem.get("file_id"):
            try:
                delete_file(remark_elem["file_id"])
            except Exception:
                pass

        file_id = save_file(file)
        update_fields["remarks.$.file_id"] = file_id
        update_fields["remarks.$.file_name"] = file.filename

    if not update_fields:
        raise HTTPException(status_code=400, detail="Nothing to update")

    update_fields["remarks.$.updated_at"] = datetime.now(timezone.utc)

    # Update the remark element in-place using positional operator
    remarks_collection.update_one({"remarks._id": ObjectId(remark_id)}, {"$set": update_fields})

    # Return the updated remark element
    updated_parent = remarks_collection.find_one({"remarks._id": ObjectId(remark_id)}, {"remarks": {"$elemMatch": {"_id": ObjectId(remark_id)}}})
    updated_remark = None
    if updated_parent and updated_parent.get("remarks"):
        updated_remark = updated_parent["remarks"][0]
        if isinstance(updated_remark.get("_id"), ObjectId):
            updated_remark["_id"] = str(updated_remark["_id"])
    return updated_remark


def delete_remark_by_id(remark_id: str, role: str, user):
    # Try to remove from embedded array first
    parent = remarks_collection.find_one({"remarks._id": ObjectId(remark_id)})
    if not parent:
        # Fallback to legacy top-level document
        legacy = remarks_collection.find_one({"_id": ObjectId(remark_id)})
        if not legacy:
            raise HTTPException(status_code=404, detail="Remark not found")

        # Only ADMIN or owner can delete
        if not (role and role.upper() == "ADMIN") and legacy.get("created_by") != getattr(user, "e_id", None):
            raise HTTPException(status_code=403, detail="Not allowed to delete this remark")

        if legacy.get("file_id"):
            try:
                delete_file(str(legacy["file_id"]))
            except Exception:
                pass

        remarks_collection.delete_one({"_id": ObjectId(remark_id)})
        return {"message": "Remark deleted successfully", "remark_id": remark_id}

    # find remark element
    remark_elem = None
    for r in parent.get("remarks", []):
        if str(r.get("_id")) == str(remark_id) or (isinstance(r.get("_id"), ObjectId) and r.get("_id") == ObjectId(remark_id)):
            remark_elem = r
            break

    if not remark_elem:
        raise HTTPException(status_code=404, detail="Remark not found")

    # Only ADMIN or owner can delete
    if not (role and role.upper() == "ADMIN") and remark_elem.get("created_by") != getattr(user, "e_id", None):
        raise HTTPException(status_code=403, detail="Not allowed to delete this remark")

    if remark_elem.get("file_id"):
        try:
            delete_file(str(remark_elem["file_id"]))
        except Exception:
            pass

    # Pull the remark from the array
    remarks_collection.update_one({"remarks._id": ObjectId(remark_id)}, {"$pull": {"remarks": {"_id": ObjectId(remark_id)}}})

    # Optionally remove the parent doc if no remarks remain
    parent_after = remarks_collection.find_one({"task_id": parent.get("task_id")})
    if parent_after and not parent_after.get("remarks"):
        remarks_collection.delete_one({"task_id": parent.get("task_id")})

    return {"message": "Remark deleted successfully", "remark_id": remark_id}