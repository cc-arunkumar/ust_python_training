"""from sqlalchemy import (
    Column, Integer, String, DateTime, Enum, ForeignKey, Text, Date
)
from sqlalchemy.sql import func
from app.database.connection import Base
import enum


class TaskPriority(enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TaskStatus(enum.Enum):
    TO_DO = "TO_DO"
    IN_PROGRESS = "IN_PROGRESS"
    REVIEW = "REVIEW"
    COMPLETED = "COMPLETED"


class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)
    remarks = Column(Text, nullable=True)

    priority = Column(Enum(TaskPriority), default=TaskPriority.medium, nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.TO_DO, nullable=False)

    assigned_to = Column(Integer, ForeignKey("employees.emp_id"), nullable=False)
    assigned_by = Column(Integer, ForeignKey("users.emp_id"), nullable=True)
    reviewer = Column(Integer, ForeignKey("users.emp_id"), nullable=False)

    created_by = Column(Integer, ForeignKey("users.emp_id"), nullable=True)
    updated_by = Column(Integer, ForeignKey("users.emp_id"), nullable=True)

    assigned_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    expected_closure = Column(Date, nullable=True)
    actual_closure = Column(Date, nullable=True)
"""

from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Text, Date
from sqlalchemy.sql import func
from app.database.connection import Base
import enum

class TaskPriority(enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskStatus(enum.Enum):
    TO_DO = "TO_DO"
    IN_PROGRESS = "IN_PROGRESS"
    REVIEW = "REVIEW"
    COMPLETED = "COMPLETED"

class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    remarks = Column(Text, nullable=True)
    priority = Column(Enum(TaskPriority), default=TaskPriority.medium, nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.TO_DO, nullable=False)
    assigned_to = Column(Integer, ForeignKey("employees.emp_id"), nullable=False)
    assigned_by = Column(Integer, ForeignKey("users.emp_id"), nullable=True)
    reviewer = Column(Integer, ForeignKey("users.emp_id"), nullable=False)
    created_by = Column(Integer, ForeignKey("users.emp_id"), nullable=True)
    updated_by = Column(Integer, ForeignKey("users.emp_id"), nullable=True)
    assigned_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    expected_closure = Column(Date, nullable=True)
    actual_closure = Column(Date, nullable=True)