from sqlalchemy import create_engine, Column, String, DateTime, ForeignKey

from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime
from services.database import Base
from services.employee_service import Employee
from sqlalchemy.orm import Session
from schemas.task import TaskSchema



class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(String(50), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)

    # Foreign Key: MATCHES String emp_id
    assigned_to = Column(String(50), ForeignKey("employees.emp_id"), nullable=False)
    assigned_by = Column(String(50), ForeignKey("employees.emp_id"), nullable=False)
    reviewer = Column(String(50), ForeignKey("employees.emp_id"), nullable=True)
    updated_by = Column(String(50), ForeignKey("employees.emp_id"), nullable=True)
    created_by = Column(String(50), ForeignKey("employees.emp_id"), nullable=False)

    assigned_at = Column(DateTime, default=datetime.utcnow)
    expected_closure = Column(DateTime, nullable=False)
    actual_closure = Column(DateTime, nullable=True)

    priority = Column(String(20), nullable=False)  
    status = Column(String(20), nullable=False)    
    remarks = Column(String(500), nullable=True)




# CREATE TASK
def create_task(db: Session, task: TaskSchema):
    new_task = Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# READ ALL TASKS
def get_tasks(db: Session):
    return db.query(Task).all()


# READ SINGLE TASK
def get_task(db: Session, task_id: str):
    return db.query(Task).filter(Task.task_id == task_id).first()

# Get tasks by assiginee
def get_tasks_by_assignee(db: Session, emp_id: str):
    return (
        db.query(Task)
        .filter(Task.assigned_to == emp_id)
        .all()
    )



# UPDATE TASK
def update_task(db: Session, task_id: str, task_data: TaskSchema):
    task = db.query(Task).filter(Task.task_id == task_id).first()

    if not task:
        return None

    for key, value in task_data.dict().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task


# DELETE TASK
def delete_task(db: Session, task_id: str):
    task = db.query(Task).filter(Task.task_id == task_id).first()

    if not task:
        return False

    db.delete(task)
    db.commit()
    return True

