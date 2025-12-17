from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.mysql import Base

class Employee(Base):
    __tablename__ = "employees"

    emp_id = Column(Integer, primary_key=True, index=True)
    emp_name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    designation = Column(String(100))
    manager_id = Column(Integer, ForeignKey("employees.emp_id"), nullable=True)

    manager = relationship("Employee", remote_side=[emp_id])
    users = relationship("User", back_populates="employee")
    assigned_tasks = relationship(
        "Task",
        foreign_keys="Task.assigned_to",
        back_populates="assignee"
    )