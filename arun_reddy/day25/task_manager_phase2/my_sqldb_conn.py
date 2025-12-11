import pymysql
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from models import TaskModel

# Database connection string
DATABASE_URL = "mysql+pymysql://root:password123@localhost:3306/ust_task_manager_db"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for ORM models
Base = declarative_base()

# ---------------------------
# User Model
# ---------------------------
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), unique=True, nullable=False)
    task = relationship("Task", back_populates="user")


# ---------------------------
# Task Model
# ---------------------------
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    description = Column(String(100))
    completed = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationship with User
    user = relationship("User", back_populates="task")


# Create tables in MySQL DB
print("Creating Tables in MySQL DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")


# ---------------------------
# Utility Functions
# ---------------------------

def get_all_users():
    """
    Fetch all users from the database.
    """
    session = SessionLocal()
    try:
        users = session.query(User).all()
        return users
    except Exception as e:
        raise Exception(f"Error fetching users: {str(e)}")
    finally:
        session.close()


def create_tasks(taskcreate: TaskModel, user: str):
    """
    Create a new task for the given user.
    """
    db = SessionLocal()
    try:
        user_detail = db.query(User).filter(User.username == user).first()
        if not user_detail:
            raise Exception("User not found")

        task = Task(
            title=taskcreate.title,
            description=taskcreate.description,
            completed=taskcreate.completed,
            user_id=user_detail.id
        )

        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    except Exception as e:
        db.rollback()
        raise Exception(f"Error creating task: {str(e)}")
    finally:
        db.close()


def get_all_tasks(user: str):
    """
    Get all tasks for a given user.
    """
    db = SessionLocal()
    try:
        user_detail = db.query(User).filter(User.username == user).first()
        if not user_detail:
            raise Exception("User not found")

        tasks = db.query(Task).filter(Task.user_id == user_detail.id).all()
        return tasks
    except Exception as e:
        db.rollback()
        raise Exception(f"Error fetching tasks: {str(e)}")
    finally:
        db.close()


def get_task_by_id(id: int):
    """
    Get a task by its ID.
    """
    db = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == id).first()
        if not task:
            raise Exception("Task not found")
        return task
    except Exception as e:
        db.rollback()
        raise Exception(f"Error fetching task by ID: {str(e)}")
    finally:
        db.close()


def update_task_by_id(id: int, taskcreate: TaskModel, user: str):
    """
    Update a task by its ID for a given user.
    """
    db = SessionLocal()
    try:
        user_detail = db.query(User).filter(User.username == user).first()
        if not user_detail:
            raise Exception("User not found")

        task = db.query(Task).filter(Task.user_id == user_detail.id).filter(Task.id == id).first()
        if not task:
            raise Exception("Invalid task_id")

        # Update task fields
        task.title = taskcreate.title
        task.description = taskcreate.description

        db.commit()
        db.refresh(task)
        return task
    except Exception as e:
        db.rollback()
        raise Exception(f"Error updating task: {str(e)}")
    finally:
        db.close()


def delete_task_by_id(id: int, user: str):
    """
    Delete a task by its ID for a given user.
    """
    db = SessionLocal()
    try:
        user_detail = db.query(User).filter(User.username == user).first()
        if not user_detail:
            raise Exception("User not found")

        task = db.query(Task).filter(Task.user_id == user_detail.id).filter(Task.id == id).first()
        if not task:
            raise Exception("Task not found")

        db.delete(task)
        db.commit()
        return {"message": "Deleted successfully"}
    except Exception as e:
        db.rollback()
        raise Exception(f"Error deleting task: {str(e)}")
    finally:
        db.close()
