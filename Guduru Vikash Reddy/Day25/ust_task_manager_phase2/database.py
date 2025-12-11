from sqlalchemy import Boolean, create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Database URL for MySQL connection
DATABASE_URL = "mysql+pymysql://root:pass123@localhost:3306/ust_task_manager_db"

# Create engine and sessionmaker for database interaction
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for models
Base = declarative_base()

# User model to represent the 'users' table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    tasks = relationship("Task", back_populates="owner")  # One-to-many relationship with tasks

# Task model to represent the 'tasks' table
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Foreign key to User
    owner = relationship("User", back_populates="tasks")  # Many-to-one relationship with User

Base.metadata.create_all(bind=engine)  # Create the tables in the database

# Function to create a new task in the database
def create_task(title: str, description: str, user_id: int, completed: bool = False):
    session = SessionLocal()  # Start a database session
    try:
        new_task = Task(title=title, description=description, completed=completed, user_id=user_id)
        session.add(new_task)  # Add the task to the session
        session.commit()  # Commit the transaction
        session.refresh(new_task)  # Refresh the task object with DB values
        return new_task  # Return the newly created task
    except Exception as e:
        session.rollback()  # Rollback if any exception occurs
        print("Exception:", e)
        return None
    finally:
        session.close()  # Close the session

# Function to get all tasks assigned to a specific user
def get_all_tasks(user_id: int):
    session = SessionLocal()
    try:
        tasks = session.query(Task).filter(Task.user_id == user_id).all()  # Fetch tasks by user ID
        return tasks
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()

# Function to get a specific task by task_id and user_id
def get_task_by_id(task_id: int, user_id: int):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()  # Fetch task
        return task
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()

# Function to update a specific task
def update_task(task_id: int, title: str, description: str, completed: bool, user_id: int):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
        if not task:
            return None  # Return None if task not found
        task.title = title
        task.description = description
        task.completed = completed
        session.commit()  # Commit changes
        session.refresh(task)  # Refresh updated task
        return task
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()

# Function to delete a task
def delete_task(task_id: int, user_id: int):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
        if not task:
            return None  # Return None if task not found
        session.delete(task)  # Delete the task
        session.commit()  # Commit the deletion
        return True  # Return True if task deleted successfully
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()  # Ensure session is closed

 
 