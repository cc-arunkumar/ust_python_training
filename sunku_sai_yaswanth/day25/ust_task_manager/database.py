from sqlalchemy import Text, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MySQL Database URL - You can replace this with your own database URL in the .env file
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:1234@localhost/ust_task_manager_db")

# Set up the database engine (connect to MySQL) and session
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)  # echo=True enables SQL logging for debugging
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the Base class after engine setup. This will be used to create models.
Base = declarative_base()

# Define the User model (table in the database)
class User(Base):
    __tablename__ = "users"  # The table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key with auto-increment
    username = Column(String(100), unique=True, index=True)  # Unique and indexed username
    password = Column(String(100))  # Store the password (hashed in real-world applications)

    # Establish relationship with the Task model (one-to-many relationship)
    tasks = relationship("Task", back_populates="owner")

# Define the Task model (table in the database)
class Task(Base):
    __tablename__ = "tasks"  # The table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key with auto-increment
    title = Column(String(255))  # Task title
    description = Column(Text)  # Task description (can be long text)
    completed = Column(Boolean, default=False)  # Boolean to mark if the task is completed or not

    # Add ForeignKey to link Task to User. This creates a many-to-one relationship (many tasks can belong to one user)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)  # Foreign key pointing to the User model
    
    # Set up bidirectional relationship (back_populates makes this relationship two-way)
    owner = relationship("User", back_populates="tasks")

# Dependency to get a database session
def get_db():
    db = SessionLocal()  # Create a new session from SessionLocal
    try:
        yield db  # Yield the session so it can be used by FastAPI route handlers
    finally:
        db.close()  # Ensure the session is closed after use
