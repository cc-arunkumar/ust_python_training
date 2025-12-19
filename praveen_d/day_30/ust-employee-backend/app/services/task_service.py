from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Integer
from sqlalchemy.orm import relationship, Session
from datetime import datetime
from services.database import Base
from schemas.task import TaskSchema


class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(String(50), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)

    # Foreign Keys
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
    remarks = Column(String(500), nullable=True)  # Keep this for backward compatibility
    
    # Relationship to task remarks
    task_remarks = relationship("TaskRemark", back_populates="task", cascade="all, delete-orphan")


class TaskRemark(Base):
    __tablename__ = "task_remarks"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(String(50), ForeignKey("tasks.task_id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(String(50), ForeignKey("employees.emp_id", ondelete="CASCADE"), nullable=False, index=True)
    remark_text = Column(Text, nullable=True)
    file_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    task = relationship("Task", back_populates="task_remarks")


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


# Get tasks by assignee
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