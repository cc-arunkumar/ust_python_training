from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from models import UserSchema, TaskSchema
from mongodb_logger import logger   # <-- Custom MongoDB logger

# ---------------- DATABASE CONNECTION ----------------
# Connect to MySQL using SQLAlchemy
DATABASE_URL = "mysql+pymysql://root:password123@localhost:3306/ust_mysql_db"
engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL queries
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# ---------------- USER MODEL ----------------
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)

    # Relationship: one user can have many tasks
    tasks = relationship("Task", back_populates="user")

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username='{self.username}')>"

# ---------------- TASK MODEL ----------------
class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False, unique=True)
    description = Column(String(100), nullable=False, unique=True)
    completed = Column(Boolean, nullable=False, default=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    # Relationship: each task belongs to one user
    user = relationship("User", back_populates="tasks")

    # Constraint to ensure completed is only 0 or 1
    __table_args__ = (
        CheckConstraint("completed IN (0,1)", name="valid_completed"),
    )

    def __repr__(self):
        return f"<Task(task_id={self.task_id}, title='{self.title}', description='{self.description}', completed={self.completed})>"

# Create tables in database
Base.metadata.create_all(bind=engine)

# ---------------- USER QUERIES ----------------
#creating new user
def create_u(user: UserSchema):
    try:
        session = SessionLocal()
        # Convert Pydantic schema -> SQLAlchemy ORM model
        db_user = User(
            username=user.username,
            password=user.password
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        logger.info(f"Created new user '{db_user.user_id}' with username={db_user.username}")
        return db_user
    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Failed to create user={user.username}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()

# Fetch all users from the database.
def fetch_all_users():
    try:
        session = SessionLocal()
        users = session.query(User).all()
        logger.info("Fetched all users successfully")
        return users
    except SQLAlchemyError as e:
        logger.error(f"Failed to fetch all users: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()

# Fetch a single user by username and password.
def fetch_user(user: UserSchema): 
    try:
        session = SessionLocal()
        db_user = session.query(User).filter(
            User.username == user.username,
            User.password == user.password
        ).first()
        if not db_user:
            logger.warning(f"User not found: {user.username}")
            raise HTTPException(status_code=404, detail="User not found")
        logger.info(f"Fetched user: {db_user.username}")
        return db_user
    except SQLAlchemyError as e:
        logger.error(f"Failed to fetch user {user.username}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()

# ---------------- TASKS CRUD ----------------
# Get all tasks for a given user.
def get_all_tasks(user_id: int):
    try:
        session = SessionLocal()
        tasks = session.query(Task).filter(Task.user_id == user_id).all()
        logger.info(f"Fetched all tasks for user_id={user_id}")
        return tasks
    except SQLAlchemyError as e:
        logger.error(f"Failed to fetch tasks for user_id={user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()

# Create a new task for a given user.
def create_task(new_task: TaskSchema, user_id: int):  
    try:
        session = SessionLocal()
        db_task = Task(
            title=new_task.title,
            description=new_task.description,
            completed=new_task.completed,
            user_id=user_id
        )
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        logger.info(f"Created new task '{db_task.title}' for user_id={user_id}")
        return db_task
    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Failed to create task for user_id={user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()

# Get a task by its ID, ensuring it belongs to the user.
def get_by_id(task_id: int, user_id: int):
    try:
        session = SessionLocal()
        task = session.query(Task).filter(Task.task_id == task_id).first()
        if not task or task.user_id != user_id:
            logger.warning(f"Task not found: task_id={task_id}, user_id={user_id}")
            raise HTTPException(status_code=404, detail="Task not found")
        logger.info(f"Fetched task_id={task_id} for user_id={user_id}")
        return task
    except SQLAlchemyError as e:
        logger.error(f"Failed to fetch task_id={task_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()

# Update an existing task.
def update_task(task_id: int, updated: TaskSchema, user_id: int):
    try:
        session = SessionLocal()
        task = session.query(Task).filter(Task.task_id == task_id).first()
        if not task or task.user_id != user_id:
            logger.warning(f"Task not found for update: task_id={task_id}, user_id={user_id}")
            raise HTTPException(status_code=404, detail="Task not found")
        task.title = updated.title
        task.description = updated.description
        task.completed = updated.completed
        session.commit()
        session.refresh(task)
        logger.info(f"Updated task_id={task_id} for user_id={user_id}")
        return task
    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Failed to update task_id={task_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()
        
# Delete a task by ID if it belongs to the user.
def delete_task(task_id: int, user_id: int):
    try:
        session = SessionLocal()
        task = session.query(Task).filter(Task.task_id == task_id, Task.user_id == user_id).first()
        if not task:
            logger.warning(f"Task not found for delete: task_id={task_id}, user_id={user_id}")
            raise HTTPException(status_code=404, detail="Task not found under user id")
        session.delete(task)
        session.commit()
        logger.info(f"Deleted task_id={task_id} for user_id={user_id}")
        return {"detail": "Task deleted successfully"}
    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Failed to delete task_id={task_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()
