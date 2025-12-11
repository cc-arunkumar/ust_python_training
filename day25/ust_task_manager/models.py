from pydantic import BaseModel, Field  # Import Pydantic for data validation and settings
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey  # Import SQLAlchemy modules for defining columns and relationships
from sqlalchemy.orm import relationship  # Import relationship for ORM associations
from database import Base  # Import the base class for SQLAlchemy models from the 'database' module

# UserDB class represents a user in the database
class UserDB(Base):
    __tablename__ = "users"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the user table
    username = Column(String(255), unique=True)  # Unique username field
    password = Column(String(255))  # Password field for the user

    # Relationship to the TaskDB model, back-populates tasks for each user
    tasks = relationship("TaskDB", back_populates="owner")


# TaskDB class represents a task in the database
class TaskDB(Base):
    __tablename__ = "tasks"  # Table name for tasks

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the task table
    title = Column(String(255))  # Title of the task
    description = Column(String(255))  # Description of the task
    completed = Column(Boolean, default=False)  # Status of task completion (default is False)
    user_id = Column(Integer, ForeignKey("users.id"))  # Foreign key linking the task to a user

    # Relationship to the UserDB model, back-populates owner for each task
    owner = relationship("UserDB", back_populates="tasks")


# LoginRequest class is used for request data when a user logs in (validation using Pydantic)
class LoginRequest(BaseModel):
    username: str  # The username of the user
    password: str  # The password for the user

# Token class represents the structure of a JWT token response (for authentication)
class Token(BaseModel):
    access_token: str  # The JWT access token
    token_type: str  # The type of token (usually 'bearer')

# User class used for representing a user in API responses (without password)
class User(BaseModel):
    username: str  # The username of the user

# Task class is used for task-related data validation (in API requests and responses)
class Task(BaseModel):
    id: int  # The unique ID of the task
    title: str  # The title of the task
    description: str  # The description of the task
    completed: bool  # Whether the task is completed or not

# CreateTask class is used when creating a new task (does not require ID, and default completed is False)
class CreateTask(BaseModel):
    title: str  # The title of the task
    description: str  # The description of the task
    completed: bool = False  # Default completion status is False
