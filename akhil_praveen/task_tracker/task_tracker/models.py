# models.py
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# ----- SQLAlchemy MODELS -----

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))

    tasks = relationship("TaskDB", back_populates="owner")


class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("UserDB", back_populates="tasks")


# ----- Pydantic MODELS (UNCHANGED FROM PHASE 1) -----

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str

class Task(BaseModel):
    id : int
    title : str
    description : str
    completed : bool

class CreateTask(BaseModel):
    title: str
    description: str
    completed: bool = False
