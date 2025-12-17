from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from authorise.authorisation import role_guard
from authorise.dependencies import get_current_user
from database.mysql_connection import SessionLocal, User, StatusEnum
from database.mongodb_connection import tasks as task_collection
from Models.task_model import AssignTaskRequest

assigntask_router = APIRouter(prefix="/assigntasks", tags=["AssignTasks"])


@assigntask_router.post(
    "/assign",
    dependencies=[Depends(role_guard(["admin", "manager"]))]
)
def assign_task(
    data: AssignTaskRequest,
    current_user=Depends(get_current_user)
):
   
    try:
        task = task_collection.find_one({"_id": ObjectId(data.task_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid task id format")

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")


    if current_user.role == "manager" and task.get("manager_id") != current_user.emp_id:
        raise HTTPException(status_code=403, detail="Not your task")


    task_collection.update_one(
        {"_id": ObjectId(data.task_id)},
        {
            "$set": {
                "assigned_to": data.employee_id,
                "status": "in-progress"
            }
        }
    )


    db = SessionLocal()
    try:
        user = db.query(User).filter(User.emp_id == data.employee_id).first()

        if not user:
            user = User(
                emp_id=data.employee_id,
                password="password",   
                role="developer",
                status=StatusEnum.active
            )
            db.add(user)
            db.commit()

    finally:
        db.close()

    return {
        "message": "Task assigned successfully",
        "task_id": data.task_id,
        "employee_id": data.employee_id,
        "status": "in-progress"
    }
