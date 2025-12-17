from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    ForeignKey,
    Text,
    Date,
    TIMESTAMP,
    BigInteger,
    func,
)
from sqlalchemy.orm import relationship
from app.database import Base


# ---------------- EMPLOYEE MODEL ----------------

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), nullable=False, unique=True, index=True)
    designation = Column(String(100), nullable=False)
    manager_id = Column(Integer, ForeignKey("employees.id"), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    manager = relationship("Employee", remote_side=[id], backref="subordinates")


# ---------------- TASK MODEL ----------------

class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)

    # UPDATED STATUS ENUM: TO_DO → IN_PROGRESS → REVIEW → COMPLETED
    status = Column(
        Enum("TO_DO", "IN_PROGRESS", "REVIEW", "COMPLETED", name="task_status_enum"),
        nullable=False,
        server_default="TO_DO",
    )

    assigned_to = Column(Integer, ForeignKey("employees.id"), nullable=False)
    assigned_by = Column(Integer, ForeignKey("employees.id"), nullable=False)
    reviewer = Column(Integer, ForeignKey("employees.id"), nullable=True)

    priority = Column(
        Enum("Low", "Medium", "High", "Critical", name="task_priority_enum"),
        nullable=False,
        server_default="Medium",
    )

    remarks = Column(Text, nullable=True)
    expected_closure = Column(Date, nullable=True)
    actual_closure = Column(Date, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    updated_by = Column(Integer, ForeignKey("employees.id"), nullable=True)

    attachments = relationship("TaskAttachment", back_populates="task")


# ---------------- ATTACHMENT MODEL ----------------

class TaskAttachment(Base):
    __tablename__ = "task_attachments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey("tasks.task_id"), nullable=False)
    file_name = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_size = Column(BigInteger, nullable=False)
    uploaded_by = Column(Integer, ForeignKey("employees.id"), nullable=False)
    uploaded_at = Column(TIMESTAMP, server_default=func.now())

    task = relationship("Task", back_populates="attachments")


# ---------------- USER MODEL ----------------

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    emp_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    password = Column(String(255), nullable=False)

    roles = Column(
        Enum("Admin", "Manager", "Employee", name="user_roles_enum"),
        nullable=False,
        server_default="Employee",
    )

    status = Column(
        Enum("Active", "Inactive", name="user_status_enum"),
        nullable=False,
        server_default="Active",
    )

    created_at = Column(TIMESTAMP, server_default=func.now())
