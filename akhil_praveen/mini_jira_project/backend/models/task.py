from sqlalchemy import (
    Column, Integer, String, Text, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.mysql import Base

class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)

    dept_name = Column(String(100))

    assigned_to = Column(Integer, ForeignKey("employees.emp_id"))
    assigned_by = Column(Integer, ForeignKey("employees.emp_id"))

    created_by = Column(Integer, ForeignKey("employees.emp_id"))
    updated_by = Column(Integer, ForeignKey("employees.emp_id"))

    priority = Column(String(20))
    status = Column(String(30))

    assigned_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    expected_closure = Column(DateTime,nullable=True)
    actual_closure = Column(DateTime)

    reviewer = Column(Integer, ForeignKey("employees.emp_id"))

    assignee = relationship("Employee", foreign_keys=[assigned_to])
