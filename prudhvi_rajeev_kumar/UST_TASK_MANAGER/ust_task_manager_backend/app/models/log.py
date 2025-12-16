from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.db.sql import Base

class LogEntry(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    level = Column(String(20), nullable=False)
    message = Column(Text, nullable=False)
    actor_id = Column(String(64), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    context = Column(String(200), nullable=True)
