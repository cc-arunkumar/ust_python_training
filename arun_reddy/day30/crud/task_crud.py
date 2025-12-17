from bson import ObjectId
from fastapi import HTTPException, status
from database.mongodb_connection import tasks
from Models.task_model import Task, TaskCreate, TaskStatus, Remark
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from database.mysql_connection import Employee, User,StatusEnum

# Insert a new task
def insert_task(task: TaskCreate):
    try:
        item = Task(
            title=task.title,
            description=task.description,
            assigned_to=task.assigned_to,
            assigned_at=task.assigned_at,
            assigned_by=task.assigned_by,
            priority=task.priority,
            status=task.status,
            remarks=task.remarks,
            expected_closure=task.expected_closure,
            actual_closure=task.actual_closure,
            updated_by=task.updated_by,
            updated_at=datetime.now()
        )
        tasks.insert_one(item.__dict__)
        return {"message": "Task created successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inserting task: {str(e)}"
        )


# Get all tasks
def get_all_tasks():
    try:
        all_tasks = []
        for task in tasks.find():
            all_tasks.append(Task(**task))
        return all_tasks
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching tasks: {str(e)}"
        )


# Get task by ID
def get_task_by_id(task_id: str):
    try:
        task_data = tasks.find_one({"_id": ObjectId(task_id)})
        if task_data:
            return Task(**task_data)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching task: {str(e)}"
        )


# Update task by ID
def update_task(task_id: str, task: TaskCreate):
    try:
        updated_task = tasks.update_one(
            {"_id": ObjectId(task_id)},
            {
                "$set": {
                    "title": task.title,
                    "description": task.description,
                    "assigned_to": task.assigned_to,
                    "assigned_at": task.assigned_at,
                    "assigned_by": task.assigned_by,
                    "priority": task.priority,
                    "status": task.status,
                    "remarks": task.remarks,
                    "actual_closure": task.actual_closure,
                    "updated_by": task.updated_by,
                    "updated_at": datetime.now()
                }
            }
        )
        if updated_task.modified_count:
            return {"message": "Task updated successfully"}
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No changes made to the task"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating task: {str(e)}"
        )


# Update task status
def update_status(id: str, task: TaskStatus):
    try:
        update_status = tasks.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"status": task.status}}
        )
        if update_status.modified_count:
            return {"message": "Task status updated successfully"}
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No changes made to the task status"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating task status: {str(e)}"
        )


# Add remark to task
def update_remarks_byid(id: str, remark: Remark):
    try:
        emp = tasks.find_one({"_id": ObjectId(id)})
        if not emp:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        new_remark = {
            "emp_id": emp.get("assigned_to"),
            "description": remark.description,
            "created_at": datetime.now()
        }

        update_result = tasks.update_one(
            {"_id": ObjectId(id)},
            {"$push": {"remarks": new_remark}}
        )

        if update_result.modified_count:
            return {"message": "Remark added successfully", "remark": new_remark}
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No changes were made"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating remarks: {str(e)}"
        )


# Get tasks by manager ID
def get_task_by_manager_id(manager_id: int):
    try:
        manager_tasks = []
        for task in tasks.find({"assigned_by": manager_id}):
            manager_tasks.append(Task(**task))
        if not manager_tasks:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No tasks found for this manager"
            )
        return manager_tasks
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching manager tasks: {str(e)}"
        )


# Delete task by ID
def delete_task_by_id(id: str):
    try:
        task_data = tasks.find_one({"_id": ObjectId(id)})
        if task_data:
            tasks.delete_one(task_data)
            return {"message": "Task deleted successfully"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting task: {str(e)}"
        )


# # manager_assign_task endpoints
# def assign_task():
#     roleverification  is manager checks with manger id in the tasks collection 
#     if he is the manger he can assign the task to an existing employee
#     and whne th task is assigned the status should change to "in-progreses"

# def raise_issue():
#     if the role is employee he can raise an issue regarding the task assigned to him
#     when teh task is in the status "in-progress" then the employee can raise an remark
#     this remark should be in the notifications of assigned manager and even when the manager replies 
#     should be in employee notifications  

# utils/task_service.py
