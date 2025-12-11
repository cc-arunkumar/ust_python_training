from sqlalchemy import Text, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MySQL Database URL
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:1234@localhost/ust_task_manager_db")

# Set up the database engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the Base class after engine setup
Base = declarative_base()

# SQLAlchemy models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    password = Column(String(100))
    
    tasks = relationship("Task", back_populates="owner")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    completed = Column(Boolean, default=False)

    # Add ForeignKey to link Task to User
    user_id = Column(Integer, ForeignKey('users.id'), index=True)  # This is the ForeignKey relationship
    
    # Set up back_populates for bidirectional relationship
    owner = relationship("User", back_populates="tasks")


def get_db():
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Yield the session to be used by route handlers
    finally:
        db.close()
