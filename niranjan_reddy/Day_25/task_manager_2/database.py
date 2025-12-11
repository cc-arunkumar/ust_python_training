from sqlalchemy import Boolean, create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Database connection URL for MySQL
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/ust_task_manager_db"

# Create engine and sessionmaker for database interaction
engine = create_engine(DATABASE_URL, echo=True)  # Echo=True will log all SQL queries to the console
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()  # Base class for all models

# User model representing the users table in the database
class User(Base):
    __tablename__ = 'users'  # Table name in the database
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    username = Column(String(50), unique=True, nullable=False)  # Username field with uniqueness
    password = Column(String(100), nullable=False)  # Password field
    tasks = relationship("Task", back_populates="owner")  # One-to-many relationship with tasks

# Task model representing the tasks table in the database
class Task(Base):
    __tablename__ = 'tasks'  # Table name in the database
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    title = Column(String(100), nullable=False)  # Task title
    description = Column(String(255), nullable=False)  # Task description
    completed = Column(Boolean, default=False)  # Boolean to mark if the task is completed
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Foreign key referencing the User
    owner = relationship("User", back_populates="tasks")  # Relationship with User model

# Create all tables in the database
Base.metadata.create_all(bind=engine)
