from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    DateTime,
    Text,
    ForeignKey
)
from app.core.database import Base


class Task(Base):
    __tablename__ = "tasks"

    t_id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)
    description = Column(Text)

    assigned_to = Column(Integer, ForeignKey("employees.e_id"), nullable=False)

    created_by = Column(Integer, nullable=False)        # emp_id (Admin/Manager)
    assigned_by = Column(Integer, nullable=False)       # emp_id (Admin/Manager)
    reviewer = Column(Integer, nullable=True)           # Manager emp_id

    priority = Column(Enum("HIGH", "MEDIUM", "LOW"), default="MEDIUM")
    status = Column(
        Enum("TO_DO", "IN_PROGRESS", "REVIEW", "DONE"),
        default="TO_DO"
    )

    remarks = Column(Text, nullable=True)

    assigned_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    expected_closure = Column(DateTime, nullable=True)
    actual_closure = Column(DateTime, nullable=True)
