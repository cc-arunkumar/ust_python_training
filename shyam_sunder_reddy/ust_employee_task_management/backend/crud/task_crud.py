from database.sql_db import get_connection
from schema.task_schema import TaskSchema
from models.task import TaskReqRes
from crud.users_crud import get_user_by_id
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from datetime import datetime


def add_task(new_task: TaskReqRes, role, user):
    try:
        if role not in ["Manager", "Admin"]:
            raise HTTPException(status_code=403, detail="Only Manager and Admin can create a new task")
        session = get_connection()
        task = TaskSchema(
            title=new_task.title,
            description=new_task.description,
            assigned_to=new_task.assigned_to,
            assigned_by=None,
            assigned_at=None,
            updated_by=new_task.updated_by,
            updated_at=None,
            priority=new_task.priority,
            status="TO_DO",
            reviewer=new_task.reviewer,
            created_by=user.e_id,
            expected_closure=new_task.expected_closure,
            actual_closure=None
        )
        # set assigned_at if assigned_to is present
        q=None
        if task.assigned_to:
            q = get_user_by_id(task.assigned_to)
            if "Developer" not in q.role:
                q.role.append("Developer")
            task.assigned_by = user.e_id
            task.assigned_at = datetime.now()
        if task.reviewer:
            q = get_user_by_id(task.reviewer)
            if "Manager" not in q.role:
                q.role.append("Manager")

        session.add(task)
        session.commit()
        session.refresh(task)
        return TaskReqRes.from_orm(task)
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


def get_all_tasks(role, user):
    try:
        session = get_connection()
        if role == "Manager":
            if "Manager" in user.role:
                tasks = session.query(TaskSchema).filter(TaskSchema.reviewer == user.e_id).all()
            else:
                raise HTTPException(status_code=403, detail="Not Authorized")
        elif role == "Admin":
            if "Admin" in user.role:
                tasks = session.query(TaskSchema).all()
            else:
                raise HTTPException(status_code=403, detail="Not Authorized")
        else:
            if role in user.role:
                tasks = session.query(TaskSchema).filter(TaskSchema.assigned_to == user.e_id).all()
            else:
                raise HTTPException(status_code=403, detail="Not Authorized")
        return [TaskReqRes.from_orm(t) for t in tasks]
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


# FIXED: Added user parameter
def get_task_by_id(t_id: int,role, user):
    try:
        session = get_connection()
        t = session.query(TaskSchema).filter(TaskSchema.t_id == t_id).first()
        if not t:
            raise HTTPException(status_code=404, detail="Task Not Found")
        
        # Optional: Add authorization check
        # Uncomment if you want to restrict access based on user role
        if "Admin" not in user.role:
            if "Manager" in user.role and t.reviewer != user.e_id:
                raise HTTPException(status_code=403, detail="Not authorized to view this task")
            elif t.assigned_to != user.e_id:
                raise HTTPException(status_code=403, detail="Not authorized to view this task")
        
        return TaskReqRes.from_orm(t)
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


def get_task_by_status(status, role, user):
    try:
        data = get_all_tasks(role, user)
        new_data = [task for task in data if task.status == status]
        return new_data
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


def update_task(user,
    t_id: int,
    title: str = None,
    description: str = None,
    assigned_to: int = None,
    priority: str = None,
    status: str = None,
    reviewer: int = None,
    expected_closure: datetime = None,
    role: str = None
) :
    try:
        # Role-based access control
        if role not in ["Manager", "Admin"]:
            raise HTTPException(status_code=403, detail="You don't have permission to update this task")
        session=get_connection()
        # Retrieve task
        t = session.query(TaskSchema).filter(TaskSchema.t_id == t_id).first()
        if not t:
            raise HTTPException(status_code=404, detail="Task not found")

        # Update fields if provided
        if title:
            t.title = title
        if description:
            t.description = description
        if assigned_to:
            assigned_user = get_user_by_id(assigned_to)
            if not assigned_user:
                raise HTTPException(status_code=404, detail="Assigned user not found")
            t.assigned_to = assigned_to
            t.assigned_at = datetime.now()  # Update assignment timestamp
            t.assigned_by = user.e_id
        if priority:
            t.priority = priority
        if status:
            t.status = status
        if reviewer:
            reviewer_user = get_user_by_id(reviewer)
            if not reviewer_user:
                raise HTTPException(status_code=404, detail="Reviewer not found")
            t.reviewer = reviewer
        if expected_closure:
            t.expected_closure = expected_closure

        # Update timestamps
        t.updated_by = user.e_id
        t.updated_at = datetime.now()

        # Commit the transaction
        session.commit()
        session.refresh(t)

        # Return updated task as a response
        return TaskReqRes.from_orm(t)

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


# def update_task(t_id: int, updated: TaskReqRes, role, user):
#     try:
#         if role not in ["Manager", "Admin"]:
#             raise HTTPException(status_code=403, detail="Don't have access to update task")
#         session = get_connection()
#         t = session.query(TaskSchema).filter(TaskSchema.t_id == t_id).first()
#         if not t:
#             raise HTTPException(status_code=404, detail="Task Not Found")
#         if "status" in updated:
#             patch_status(updated["status"])
#         excluded_fields = ["assigned_by", "assigned_at", "updated_by", "updated_at", "created_by"]

#         for key, value in updated.items():
#             if key not in excluded_fields:
#                 setattr(t, key, value)

#         # handle assignment timestamp
#         if "assigned_to" in updated:
#             assigned_user = get_user_by_id(updated.get("assigned_to"))
#             if not assigned_user:
#                 raise HTTPException(status_code=404, detail="Assigned user not found")
#             if "Developer" not in assigned_user.role:
#                 assigned_user.role.append("Developer")
#             t.assigned_at = datetime.now()
#             t.assigned_by = user.e_id

#         if "reviewer" in updated:
#             q = get_user_by_id(updated.get("reviewer"))
#             if "Manager" not in q.role:
#                 q.role.append("Manager")

#         t.updated_by = user.e_id
#         t.updated_at = datetime.now()
#         session.commit()
#         session.refresh(t)
#         return TaskReqRes.from_orm(t)
#     except SQLAlchemyError as e:
#         session.rollback()
#         raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
#     finally:
#         session.close()

## patch the priority
def patch_priority(t_id: int, priority: str, role: str, user):
    try:
        # Retrieve task
        session=get_connection()
        t = session.query(TaskSchema).filter(TaskSchema.t_id == t_id).first()
        if not t:
            raise HTTPException(status_code=404, detail="Task not found")

        # Check if the user has permission to change the priority
        if role not in ["Manager", "Admin"]:
            raise HTTPException(status_code=403, detail="You do not have permission to change the priority of this task")

        # Ensure the user is the manager of the task if they are not an Admin
        if role == "Manager":
            if user.e_id != t.reviewer:  # Assuming `reviewer` is the manager of the task
                raise HTTPException(status_code=403, detail="You are not the manager of this task")

        # Update the priority of the task
        t.priority = priority
        t.updated_by = user.e_id
        t.updated_at = datetime.now()

        # Commit transaction
        session.commit()
        session.refresh(t)

        # Return updated task as a response
        return TaskReqRes.from_orm(t)

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


## patch the status
def patch_status(t_id, status, role, user):
    try:
        session = get_connection()
        t = session.query(TaskSchema).filter(TaskSchema.t_id == t_id).first()
        if not t:
            raise HTTPException(status_code=404, detail="Task Not Found")
        
        if role == "Manager":
            if user.e_id != t.reviewer:
                raise HTTPException(status_code=403, detail="Not Reviewer for the task")
            if (status.upper() == "IN_PROGRESS" or status.upper() == "DONE") and t.status.upper() == "REVIEW":
                if status.upper() == "DONE":
                    t.actual_closure = datetime.now()
                t.status = status
            else:
                raise HTTPException(status_code=409, detail="Can only change status to IN_PROGRESS or DONE from REVIEW status")
        else:
            if user.e_id != t.assigned_to:
                raise HTTPException(status_code=403, detail="Not assigned to this task")
            if status.upper() == "IN_PROGRESS"  and t.status.upper() == "TO_DO":
                t.status = status
            elif status.upper() == "REVIEW" and t.status.upper() == "IN_PROGRESS":
                t.status = status
            else:
                raise HTTPException(status_code=409, detail="Can only change status from TO_DO to IN_PROGRESS or from IN_PROGRESS to REVIEW")
        t.updated_at=datetime.now()
        t.updated_by=user.e_id
        session.commit()
        session.refresh(t)
        return TaskReqRes.from_orm(t)
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


# FIXED: Added user parameter
def delete_task(t_id: int, user):
    try:
        session = get_connection()
        t = session.query(TaskSchema).filter(TaskSchema.t_id == t_id).first()
        if not t:
            raise HTTPException(status_code=404, detail="Task Not Found")
        
        # Verify user has Admin role
        if "Admin" not in user.role:
            raise HTTPException(status_code=403, detail="Only Admin can delete tasks")
        
        session.delete(t)
        session.commit()
        return {"detail": "Task Deleted Successfully"}
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()