from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.sql import Base

class Employee(Base):
    __tablename__ = "employees"
    emp_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    designation = Column(String(100), nullable=False)
    manager_id = Column(Integer, ForeignKey("employees.emp_id"), nullable=True)

    manager = relationship("Employee", remote_side=[emp_id], backref="team_members")
    tasks_assigned = relationship("Task", foreign_keys="Task.assigned_to", backref="assignee")
    tasks_created = relationship("Task", foreign_keys="Task.created_by", backref="creator")
