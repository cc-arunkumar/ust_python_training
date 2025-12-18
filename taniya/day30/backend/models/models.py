from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, Date, Text
from sqlalchemy.orm import relationship
from database import Base
import enum

# Enums
class RoleEnum(str, enum.Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    EMPLOYEE = "EMPLOYEE"

class StatusEnum(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"

class PriorityEnum(str, enum.Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

class TaskStatusEnum(str, enum.Enum):
    TO_DO = "TO_DO"
    IN_PROGRESS = "IN_PROGRESS"
    REVIEW = "REVIEW"
    DONE = "DONE"

# Employee Model
class Employee(Base):
    __tablename__ = "employees"

    emp_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    # email = Column(String(150), unique=True, nullable=False)
    designation = Column(String(100))
    manager_id = Column(Integer, ForeignKey("employees.emp_id"), nullable=True)

    # Relationships
    user = relationship("User", back_populates="employee", uselist=False)
    tasks_assigned = relationship("Task", foreign_keys="[Task.assigned_to]", back_populates="assignee")
    tasks_created = relationship("Task", foreign_keys="[Task.assigned_by]", back_populates="creator")
    tasks_updated = relationship("Task", foreign_keys="[Task.updated_by]", back_populates="updater")

# User Model
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(Integer, ForeignKey("employees.emp_id"), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.ACTIVE)

    # Relationship
    employee = relationship("Employee", back_populates="user")

# Task Model
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    assigned_to = Column(Integer, ForeignKey("employees.emp_id"), nullable=False)
    assigned_by = Column(Integer, ForeignKey("employees.emp_id"), nullable=False)
    assigned_at = Column(DateTime)
    updated_by = Column(Integer, ForeignKey("employees.emp_id"), nullable=True)
    updated_at = Column(DateTime)
    priority = Column(Enum(PriorityEnum), default=PriorityEnum.MEDIUM)
    status = Column(Enum(TaskStatusEnum), default=TaskStatusEnum.TO_DO)
    review = Column(Text)
    remark = Column(Text)
    expected_closure = Column(Date)
    actual_closure = Column(Date)

    # Relationships
    assignee = relationship("Employee", foreign_keys=[assigned_to], back_populates="tasks_assigned")
    creator = relationship("Employee", foreign_keys=[assigned_by], back_populates="tasks_created")
    updater = relationship("Employee", foreign_keys=[updated_by], back_populates="tasks_updated")
