"""from sqlalchemy import Column, Integer, LargeBinary, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.connection import Base


class TaskFile(Base):
    __tablename__ = "task_files"

    file_id = Column(Integer, primary_key=True, index=True)

    task_id = Column(
        Integer,
        ForeignKey("tasks.task_id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    filename = Column(String(255), nullable=False)
    content_type = Column(String(100), nullable=False)

    file_data = Column(LargeBinary, nullable=False)

    uploaded_at = Column(DateTime, server_default=func.now())
"""

from sqlalchemy import Column, Integer, LargeBinary, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.connection import Base

class TaskFile(Base):
    __tablename__ = "task_files"
    file_id = Column(Integer, primary_key=True, index=True)
    task_id = Column(
        Integer,
        ForeignKey("tasks.task_id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    filename = Column(String(255), nullable=False)
    content_type = Column(String(100), nullable=False)
    file_data = Column(LargeBinary, nullable=False)
    uploaded_at = Column(DateTime, server_default=func.now())