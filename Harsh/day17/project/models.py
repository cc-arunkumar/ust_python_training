# Pydantic models — keep EXACTLY as Phase 1
from typing import Optional
from pydantic import BaseModel

# SQLAlchemy ORM models for Phase 2
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False


class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    tasks = relationship("TaskDB", back_populates="owner")


class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(String(200), nullable=False)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("UserDB", back_populates="tasks")
