from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from typing import Optional

from app.db.mongodb import tasks_collection
from app.schemas.task_schema import TaskCreate, TaskUpdate
from app.api.deps import get_current_user
from app.utils.logger import create_log

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

ALLOWED_STATUSES = ["TO_DO", "IN_PROGRESS", "REVIEW", "COMPLETED"]

# ---------------------------------------------------
# CREATE TASK (MANAGER / ADMIN)
# ---------------------------------------------------
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, current_user: dict = Depends(get_current_user)):
    if "manager" not in current_user["roles"] and "admin" not in current_user["roles"]:
        create_log(
            emp_id=current_user["emp_id"],
            roles=current_user["roles"],
            module="TASKS",
            action="CREATE_TASK",
            description="Unauthorized create attempt",
            status="FAILED"
        )
        raise HTTPException(status_code=403, detail="Not allowed")

    if tasks_collection.find_one({"task_id": task.task_id}):
        raise HTTPException(status_code=400, detail="Task ID already exists")

    doc = {
        "task_id": task.task_id,
        "title": task.title,
        "description": task.description,
        "status": "TO_DO",
        "priority": task.priority,
        "assigned_to": task.assigned_to,
        "assigned_by": current_user["emp_id"],
        "created_by": current_user["emp_id"],
        "created_at": datetime.now(),
        "expected_closure": task.expected_closure,
        "remarks": None,
        "reviewer": task.reviewer,
        "actual_closure": None,
        "updated_at": None,
        "updated_by": None
    }

    tasks_collection.insert_one(doc)

    create_log(
        emp_id=current_user["emp_id"],
        roles=current_user["roles"],
        module="TASKS",
        action="CREATE_TASK",
        resource_id=task.task_id,
        description="Task created",
        status="SUCCESS",
        new_value=doc
    )

    return {"message": "Task created successfully"}


# ---------------------------------------------------
# GET ALL TASKS
# ---------------------------------------------------
@router.get("/")
def get_all_tasks(current_user: dict = Depends(get_current_user)):
    roles = current_user["roles"]
    emp_id = current_user["emp_id"]

    if "admin" in roles:
        return list(tasks_collection.find({}, {"_id": 0}))

    if "manager" in roles:
        return list(tasks_collection.find({"created_by": emp_id}, {"_id": 0}))

    return list(tasks_collection.find({"assigned_to": emp_id}, {"_id": 0}))


# ---------------------------------------------------
# GET TASK BY ID
# ---------------------------------------------------
@router.get("/{task_id}")
def get_task(task_id: str, current_user: dict = Depends(get_current_user)):
    task = tasks_collection.find_one({"task_id": task_id}, {"_id": 0})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    roles = current_user["roles"]
    emp_id = current_user["emp_id"]

    if "admin" in roles:
        return task
    if "manager" in roles and task["created_by"] == emp_id:
        return task
    if "developer" in roles and task["assigned_to"] == emp_id:
        return task

    raise HTTPException(status_code=403, detail="Access denied")


# ---------------------------------------------------
# PATCH TASK STATUS
# ---------------------------------------------------
@router.patch("/{task_id}/status")
def patch_status(task_id: str, status: str, current_user: dict = Depends(get_current_user)):
    if status not in ALLOWED_STATUSES:
        raise HTTPException(status_code=400, detail="Invalid status value")

    task = tasks_collection.find_one({"task_id": task_id})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    roles = current_user["roles"]
    emp_id = current_user["emp_id"]
    current_status = task["status"]

    if "admin" in roles:
        raise HTTPException(status_code=403, detail="Admin cannot change task status")

    # Developer rule
    if "developer" in roles:
        if task["assigned_to"] != emp_id:
            raise HTTPException(status_code=403, detail="Developer can update only assigned tasks")
        if current_status != "IN_PROGRESS" or status != "REVIEW":
            raise HTTPException(status_code=400, detail="Developer can move status only from IN_PROGRESS to REVIEW")

    # Manager rule
    if "manager" in roles:
        if task["created_by"] != emp_id:
            raise HTTPException(status_code=403, detail="Manager can update only tasks created by him")
        allowed_transitions = {"TO_DO": "IN_PROGRESS", "REVIEW": "COMPLETED"}
        if current_status not in allowed_transitions or allowed_transitions[current_status] != status:
            raise HTTPException(status_code=400, detail="Invalid status transition for manager")

    tasks_collection.update_one(
        {"task_id": task_id},
        {"$set": {
            "status": status,
            "updated_at": datetime.now(),
            "updated_by": emp_id,
            "actual_closure": datetime.now() if status == "COMPLETED" else None
        }}
    )

    create_log(
        emp_id=emp_id,
        roles=roles,
        module="TASKS",
        action="PATCH_STATUS",
        resource_id=task_id,
        description=f"Status changed from {current_status} to {status}",
        status="SUCCESS",
        old_value={"status": current_status},
        new_value={"status": status}
    )

    return {"message": f"Task status updated to {status}"}


# ---------------------------------------------------
# PATCH REVIEWER (MANAGER ONLY)
# ---------------------------------------------------
@router.patch("/{task_id}/reviewer")
def patch_reviewer(task_id: str, reviewer: str, current_user: dict = Depends(get_current_user)):
    if "manager" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only manager allowed")

    task = tasks_collection.find_one({"task_id": task_id})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks_collection.update_one(
        {"task_id": task_id},
        {"$set": {"reviewer": reviewer, "updated_at": datetime.now(), "updated_by": current_user["emp_id"]}}
    )

    create_log(
        emp_id=current_user["emp_id"],
        roles=current_user["roles"],
        module="TASKS",
        action="PATCH_REVIEWER",
        resource_id=task_id,
        description="Reviewer assigned",
        status="SUCCESS"
    )

    return {"message": "Reviewer updated"}


# ---------------------------------------------------
# PATCH PRIORITY (MANAGER ONLY)
# ---------------------------------------------------
@router.patch("/{task_id}/priority")
def patch_priority(task_id: str, priority: str, current_user: dict = Depends(get_current_user)):
    task = tasks_collection.find_one({"task_id": task_id})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    roles = current_user["roles"]
    emp_id = current_user["emp_id"]

    if "admin" in roles or "developer" in roles:
        raise HTTPException(status_code=403, detail="Not allowed to update priority")
    if "manager" in roles and task["created_by"] != emp_id:
        raise HTTPException(status_code=403, detail="Manager can update only own tasks")

    tasks_collection.update_one(
        {"task_id": task_id},
        {"$set": {"priority": priority, "updated_at": datetime.now(), "updated_by": emp_id}}
    )

    create_log(
        emp_id=emp_id,
        roles=roles,
        module="TASKS",
        action="PATCH_PRIORITY",
        resource_id=task_id,
        description=f"Priority changed to {priority}",
        status="SUCCESS",
        old_value={"priority": task.get("priority")},
        new_value={"priority": priority}
    )

    return {"message": "Task priority updated successfully"}


# ---------------------------------------------------
# PUT TASK (ADMIN ONLY - FULL UPDATE)
# ---------------------------------------------------
@router.put("/{task_id}")
def put_task(task_id: str, task: TaskCreate, current_user: dict = Depends(get_current_user)):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Admin only")

    old = tasks_collection.find_one({"task_id": task_id}, {"_id": 0})
    if not old:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks_collection.update_one({"task_id": task_id}, {"$set": task.dict()})

    create_log(
        emp_id=current_user["emp_id"],
        roles=current_user["roles"],
        module="TASKS",
        action="PUT_TASK",
        resource_id=task_id,
        description="Task fully updated",
        status="SUCCESS",
        old_value=old,
        new_value=task.dict()
    )

    return {"message": "Task fully updated"}


# ---------------------------------------------------
# DELETE TASK (ADMIN ONLY)
# ---------------------------------------------------
@router.delete("/{task_id}")
def delete_task(task_id: str, current_user: dict = Depends(get_current_user)):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Admin only")

    task = tasks_collection.find_one({"task_id": task_id}, {"_id": 0})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks_collection.delete_one({"task_id": task_id})

    create_log(
        emp_id=current_user["emp_id"],
        roles=current_user["roles"],
        module="TASKS",
        action="DELETE_TASK",
        resource_id=task_id,
        description="Task deleted",
        status="SUCCESS",
        old_value=task
    )

    return {"message": "Task deleted"}


# from fastapi import APIRouter, Depends, HTTPException, status
# from datetime import datetime

# from app.db.mongodb import tasks_collection
# from app.schemas.task_schema import TaskCreate
# from app.api.deps import get_current_user
# from app.utils.logger import create_log

# router = APIRouter(
#     prefix="/tasks",
#     tags=["Tasks"]
# )

# # ---------------------------------------------------
# # CREATE TASK (MANAGER / ADMIN)
# # ---------------------------------------------------
# @router.post("/", status_code=status.HTTP_201_CREATED)
# def create_task(
#     task: TaskCreate,
#     current_user: dict = Depends(get_current_user)
# ):
#     # Only manager or admin can create task
#     if "manager" not in current_user["roles"] and "admin" not in current_user["roles"]:
#         create_log(
#             emp_id=current_user["emp_id"],
#             roles=current_user["roles"],
#             module="TASKS",
#             action="CREATE_TASK",
#             description="Unauthorized create attempt",
#             status="FAILED"
#         )
#         raise HTTPException(status_code=403, detail="Not allowed")

#     # Check for duplicate task_id
#     if tasks_collection.find_one({"task_id": task.task_id}):
#         raise HTTPException(status_code=400, detail="Task ID already exists")

#     # Auto-generate system fields
#     doc = {
#         "task_id": task.task_id,
#         "title": task.title,
#         "description": task.description,
#         "status": "TO_DO",  # initial status
#         "priority": task.priority,
#         "assigned_to": task.assigned_to,
#         "assigned_by": current_user["emp_id"],  # auto from logged-in user
#         "created_by": current_user["emp_id"],   # auto from logged-in user
#         "created_at": datetime.utcnow(),
#         "expected_closure": task.expected_closure,
#         "remarks": None,          # system-managed
#         "reviewer": task.reviewer,
#         "actual_closure": None,   # system-managed
#         "updated_at": None,       # system-managed
#         "updated_by": None        # system-managed
#     }

#     # Insert into MongoDB
#     tasks_collection.insert_one(doc)

#     # Create a log entry
#     create_log(
#         emp_id=current_user["emp_id"],
#         roles=current_user["roles"],
#         module="TASKS",
#         action="CREATE_TASK",
#         resource_id=task.task_id,
#         description="Task created",
#         status="SUCCESS",
#         new_value=doc
#     )

#     return {"message": "Task created successfully"}
