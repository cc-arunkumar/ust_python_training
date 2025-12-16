from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.sql import Base

class Task(Base):
    __tablename__ = "tasks"
    taskid = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    assigned_to = Column(Integer, ForeignKey("employees.emp_id"), nullable=False)
    assigned_by = Column(Integer, ForeignKey("employees.emp_id"), nullable=False)
    assigned_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    priority = Column(String(20), nullable=False)  # e.g., low, medium, high, critical
    status = Column(String(30), nullable=False)    # e.g., open, in_progress, review, done, closed
    remark = Column(String(500), nullable=True)
    reviewer = Column(Integer, ForeignKey("employees.emp_id"), nullable=True)
    expected_closure = Column(DateTime, nullable=True)
    actual_closure = Column(DateTime, nullable=True)
    updated_by = Column(Integer, ForeignKey("employees.emp_id"), nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = Column(Integer, ForeignKey("employees.emp_id"), nullable=False)
