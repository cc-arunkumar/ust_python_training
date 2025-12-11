from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from database import Base
from typing import Optional, List

# SQLAlchemy User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)  

    tasks = relationship("Task", back_populates="owner")

# SQLAlchemy Task model
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks")

# Pydantic model for Task creation
class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool = False

# Pydantic model for Task updates
class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool

# Pydantic model for Task response (with `orm_mode=True` to support SQLAlchemy models)
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    # Enable ORM mode to convert SQLAlchemy models into Pydantic models
    class Config:
        orm_mode = True

# Pydantic model for Login request
class LoginRequest(BaseModel):
    username: str
    password: str

# Pydantic model for the authentication token response
class Token(BaseModel):
    access_token: str
    token_type: str