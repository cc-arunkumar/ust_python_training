from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException, status
from models.task import Task
from models.employees import Employee
from services.user import UserService
from datetime import datetime


class TaskService:

    @staticmethod
    def create(db: Session, data: dict, current_user) -> Task:
        try:
            # Validation: assigned_to and reviewer cannot be same
            if data.get("assigned_to") and data.get("reviewer"):
                if data["assigned_to"] == data["reviewer"]:
                    raise HTTPException(
                        status_code=400,
                        detail="assigned_to and reviewer cannot be same"
                    )
            
            # Validate assigned_to employee exists
            if data.get("assigned_to"):
                assignee = db.query(Employee).filter(
                    Employee.emp_id == data["assigned_to"]
                ).first()
                if not assignee:
                    raise HTTPException(404, f"Employee with ID {data['assigned_to']} not found")
            
            # Validate reviewer employee exists
            if data.get("reviewer"):
                reviewer = db.query(Employee).filter(
                    Employee.emp_id == data["reviewer"]
                ).first()
                if not reviewer:
                    raise HTTPException(404, f"Reviewer with ID {data['reviewer']} not found")

            task = Task(
                **data,
                created_by=current_user.emp_id,
                assigned_by=current_user.emp_id,
                updated_by=current_user.emp_id,
                updated_at=datetime.utcnow()
            )

            db.add(task)
            db.commit()
            db.refresh(task)

            # Auto user creation with error handling
            try:
                if task.assigned_to:
                    UserService.create_if_not_exists(db, task.assigned_to, "DEVELOPER")

                if task.reviewer:
                    UserService.create_if_not_exists(db, task.reviewer, "MANAGER")
            except Exception as e:
                # Log but don't fail the task creation
                print(f"Warning: Failed to create user accounts: {str(e)}")

            return task
        
        except HTTPException:
            db.rollback()
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

    @staticmethod
    def update(db: Session, task: Task, data: dict, current_user) -> Task:
        try:
            assigned_to = data.get("assigned_to", task.assigned_to)
            reviewer = data.get("reviewer", task.reviewer)

            # Validate assigned_to and reviewer are not the same
            if assigned_to and reviewer and assigned_to == reviewer:
                raise HTTPException(400, "assigned_to and reviewer cannot be same")
            
            # Validate assigned_to employee exists if being updated
            if "assigned_to" in data and data["assigned_to"]:
                assignee = db.query(Employee).filter(
                    Employee.emp_id == data["assigned_to"]
                ).first()
                if not assignee:
                    raise HTTPException(404, f"Employee with ID {data['assigned_to']} not found")
            
            # Validate reviewer employee exists if being updated
            if "reviewer" in data and data["reviewer"]:
                reviewer_emp = db.query(Employee).filter(
                    Employee.emp_id == data["reviewer"]
                ).first()
                if not reviewer_emp:
                    raise HTTPException(404, f"Reviewer with ID {data['reviewer']} not found")

            for key, value in data.items():
                setattr(task, key, value)

            task.updated_by = current_user.emp_id
            task.updated_at = datetime.utcnow()

            db.commit()
            db.refresh(task)

            return task
        
        except HTTPException:
            db.rollback()
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

    @staticmethod
    def update_status(db: Session, task: Task, status: str, current_user):
        try:
            # Validate status value
            valid_statuses = ["TODO", "IN_PROGRESS", "IN_REVIEW", "DONE", "BLOCKED"]
            if status not in valid_statuses:
                raise HTTPException(400, f"Invalid status. Must be one of: {', '.join(valid_statuses)}")

            task.status = status
            task.updated_by = current_user.emp_id
            task.updated_at = datetime.utcnow()

            if status == "DONE":
                task.actual_closure = datetime.utcnow()

            db.commit()
            db.refresh(task)
            return task
        
        except HTTPException:
            db.rollback()
            raise
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(500, f"Database error: {str(e)}")
        except Exception as e:
            db.rollback()
            raise HTTPException(500, f"Internal server error: {str(e)}")