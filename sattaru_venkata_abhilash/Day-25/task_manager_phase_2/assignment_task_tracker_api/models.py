from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db_connection_sql import Base
from pydantic import BaseModel
from typing import List

# Task model for MySQL database
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))  # Foreign Key to User

    # Relationship with User (many tasks can belong to one user)
    owner = relationship("User", back_populates="tasks")


# User model for MySQL database
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)  # This should be a hashed password

    # Relationship with tasks (using string reference to avoid circular dependencies)
    tasks = relationship("Task", back_populates="owner")


# Pydantic models for validation

class UserLogin(BaseModel):
    username: str
    password: str


# Base model for Task (used for validation)
class TaskBase(BaseModel):
    title: str
    description: str


# Model for creating a new task (without the 'completed' field)
class TaskCreate(TaskBase):
    """Used for creating a task (no 'completed' in request)"""
    pass


# Model for updating an existing task (with the 'completed' field)
class TaskUpdate(TaskBase):
    """Used for updating a task (full update, includes 'completed')"""
    completed: bool


# TaskResponse is used to serialize the task object for response
class TaskResponse(TaskBase):
    """Response model for a task"""
    id: int
    completed: bool = False
    user_id: int  # Changed from owner_id to user_id to match SQLAlchemy field name

    class Config:
        from_attributes = True  # Changed from 'orm_mode' to 'from_attributes' for Pydantic V2
