from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from datetime import datetime
from database.mysql import get_db
from database.mongo import reviews_collection, audit_logs_collection, fs
from schemas.task import *
from models.task import Task
from services.task import TaskService
from auth.auth import get_current_user
from services.employees import EmployeeService
from pymongo.errors import PyMongoError

task_router = APIRouter(prefix="/tasks", tags=["Tasks"])


@task_router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db),
               user=Depends(get_current_user)):
    try:
        # ADMIN can view all tasks
        if "ADMIN" in user.role:
            return db.query(Task).all()
        
        # MANAGER can view tasks assigned to employees under them + tasks assigned to them + tasks created by them
        elif "MANAGER" in user.role:
            subordinate_ids = EmployeeService.get_subordinate_ids(db, user.emp_id)
            return db.query(Task).filter(
                (Task.assigned_to.in_(subordinate_ids)) |
                (Task.assigned_to == user.emp_id) |
                (Task.created_by == user.emp_id) |
                (Task.reviewer == user.emp_id)
            ).all()
        
        # DEVELOPER can only view tasks assigned to them or reviewed by them
        elif "DEVELOPER" in user.role:
            return db.query(Task).filter(
                (Task.assigned_to == user.emp_id) |
                (Task.reviewer == user.emp_id)
            ).all()
        
        else:
            raise HTTPException(403, "Insufficient permissions")
    
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(500, f"Internal server error: {str(e)}")


@task_router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, 
             db: Session = Depends(get_db),
             user=Depends(get_current_user)):
    try:
        task = db.query(Task).filter(Task.task_id == task_id).first()
        if not task:
            raise HTTPException(404, "Task not found")
        
        # ADMIN can view any task
        if "ADMIN" in user.role:
            return task
        
        # MANAGER can view tasks assigned to employees under them + their own tasks
        elif "MANAGER" in user.role:
            subordinate_ids = EmployeeService.get_subordinate_ids(db, user.emp_id)
            if (task.assigned_to in subordinate_ids or 
                task.assigned_to == user.emp_id or 
                task.created_by == user.emp_id or
                task.reviewer == user.emp_id):
                return task
            raise HTTPException(403, "You can only view tasks related to you or your team")
        
        # DEVELOPER can view tasks assigned to them or they are reviewing
        elif "DEVELOPER" in user.role:
            if task.assigned_to == user.emp_id or task.reviewer == user.emp_id:
                return task
            raise HTTPException(403, "You can only view tasks assigned to you")
        
        else:
            raise HTTPException(403, "Insufficient permissions")
    
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(500, f"Internal server error: {str(e)}")


@task_router.post("/", response_model=TaskResponse, status_code=201)
def create_task(payload: TaskCreate,
                db: Session = Depends(get_db),
                user=Depends(get_current_user)):
    try:
        if not any(r in user.role for r in ["ADMIN", "MANAGER"]):
            raise HTTPException(403, "Admin or Manager only")

        # MANAGER can only assign tasks to employees under them
        if "MANAGER" in user.role and "ADMIN" not in user.role:
            if payload.assigned_to:
                subordinate_ids = EmployeeService.get_subordinate_ids(db, user.emp_id)
                if payload.assigned_to not in subordinate_ids and payload.assigned_to != user.emp_id:
                    raise HTTPException(403, "You can only assign tasks to employees under you")

        if payload.assigned_to and payload.reviewer and payload.assigned_to == payload.reviewer:
            raise HTTPException(400, "assigned_to and reviewer cannot be same")

        task = TaskService.create(db, payload.dict(), user)

        # Log to MongoDB with error handling
        try:
            audit_logs_collection.insert_one({
                "action": "TASK_CREATED",
                "task_id": task.task_id,
                "emp_id": user.emp_id,
                "timestamp": datetime.utcnow()
            })
        except PyMongoError as e:
            print(f"Failed to log audit: {str(e)}")
        
        return task
    
    except HTTPException:
        raise
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(400, f"Database integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(500, f"Internal server error: {str(e)}")


@task_router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int,
                payload: TaskUpdate,
                db: Session = Depends(get_db),
                user=Depends(get_current_user)):
    try:
        task = db.query(Task).filter(Task.task_id == task_id).first()
        if not task:
            raise HTTPException(404, "Task not found")
        
        # ADMIN can update any task
        if "ADMIN" in user.role:
            pass  # Admin can proceed
        
        # MANAGER can update tasks they created or assigned to their team
        elif "MANAGER" in user.role:
            subordinate_ids = EmployeeService.get_subordinate_ids(db, user.emp_id)
            if task.created_by != user.emp_id and task.assigned_to not in subordinate_ids:
                raise HTTPException(403, "You can only update tasks you created or assigned to your team")
            
            # MANAGER can only reassign to their team
            if "assigned_to" in payload.dict(exclude_unset=True):
                new_assignee = payload.assigned_to
                if new_assignee and new_assignee not in subordinate_ids and new_assignee != user.emp_id:
                    raise HTTPException(403, "You can only assign tasks to employees under you")
        
        # DEVELOPER cannot update tasks
        else:
            raise HTTPException(403, "Developers cannot update tasks. Use status patch endpoint instead.")

        data = payload.dict(exclude_unset=True)
        
        # Get current values or new values
        assigned_to = data.get("assigned_to", task.assigned_to)
        reviewer = data.get("reviewer", task.reviewer)
        
        # Validate assigned_to and reviewer are not the same
        if assigned_to and reviewer and assigned_to == reviewer:
            raise HTTPException(400, "assigned_to and reviewer cannot be same")

        return TaskService.update(db, task, data, user)
    
    except HTTPException:
        raise
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(400, f"Database integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(500, f"Internal server error: {str(e)}")


@task_router.patch("/{task_id}/status")
def patch_status(task_id: int,
                 payload: TaskStatusPatch,
                 db: Session = Depends(get_db),
                 user=Depends(get_current_user)):
    try:
        task = db.query(Task).filter(Task.task_id == task_id).first()
        if not task:
            raise HTTPException(404, "Task not found")
        
        # ADMIN can update any task status
        if "ADMIN" in user.role:
            pass
        
        # MANAGER can update status of tasks they created or assigned to their team
        elif "MANAGER" in user.role:
            subordinate_ids = EmployeeService.get_subordinate_ids(db, user.emp_id)
            if (task.assigned_to not in subordinate_ids and 
                task.assigned_to != user.emp_id and
                task.created_by != user.emp_id and
                task.reviewer != user.emp_id):
                raise HTTPException(403, "You can only update status of tasks related to you or your team")
        
        # DEVELOPER can update status of tasks assigned to them
        elif "DEVELOPER" in user.role:
            if task.assigned_to != user.emp_id:
                raise HTTPException(403, "You can only update status of tasks assigned to you")
        
        else:
            raise HTTPException(403, "Insufficient permissions")

        TaskService.update_status(db, task, payload.status, user)

        # Handle review and audit logs with error handling
        try:
            if payload.review:
                reviews_collection.insert_one({
                    "task_id": task_id,
                    "review": payload.review,
                    "reviewed_by": user.user_id,
                    "created_at": datetime.utcnow()
                })

            audit_logs_collection.insert_one({
                "action": "STATUS_UPDATED",
                "task_id": task_id,
                "user_id": user.user_id,
                "timestamp": datetime.utcnow()
            })
        except PyMongoError as e:
            print(f"Failed to log to MongoDB: {str(e)}")

        return {"message": "Status updated"}
    
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(500, f"Internal server error: {str(e)}")


@task_router.post("/{task_id}/upload")
async def upload_file(task_id: int, 
                     file: UploadFile,
                     db: Session = Depends(get_db),
                     user=Depends(get_current_user)):
    try:
        # Verify task exists
        task = db.query(Task).filter(Task.task_id == task_id).first()
        if not task:
            raise HTTPException(404, "Task not found")
        
        # Check authorization
        if "ADMIN" in user.role:
            pass
        elif "MANAGER" in user.role:
            subordinate_ids = EmployeeService.get_subordinate_ids(db, user.emp_id)
            if (task.assigned_to not in subordinate_ids and 
                task.assigned_to != user.emp_id and
                task.created_by != user.emp_id):
                raise HTTPException(403, "You can only upload files to tasks related to you or your team")
        elif "DEVELOPER" in user.role:
            if task.assigned_to != user.emp_id:
                raise HTTPException(403, "You can only upload files to tasks assigned to you")
        else:
            raise HTTPException(403, "Insufficient permissions")
        
        # Validate file
        if not file.filename:
            raise HTTPException(400, "No filename provided")
        
        # Upload to GridFS
        try:
            await fs.upload_from_stream(
                file.filename,
                file.file,
                metadata={
                    "task_id": task_id, 
                    "uploaded_at": datetime.utcnow(),
                    "uploaded_by": user.emp_id
                }
            )
        except PyMongoError as e:
            raise HTTPException(500, f"Failed to upload file to GridFS: {str(e)}")
        
        return {"message": "File uploaded", "filename": file.filename}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Internal server error: {str(e)}")