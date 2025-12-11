from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,Boolean   # Import SQLAlchemy core components
from sqlalchemy.orm import sessionmaker,declarative_base,relationship          # Import ORM utilities
from models import TaskModel                                                   # Import TaskModel (Pydantic or SQLAlchemy model)

DATABASE_URL = "mysql+pymysql://root:felix_123@localhost:3306/ust_task_manager_db"   # Database connection string

engine = create_engine(DATABASE_URL)   # Create SQLAlchemy engine to connect with MySQL DB

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)   # Configure session factory

Base = declarative_base()   # Base class for ORM models

class User(Base):   # Define User table model
    __tablename__ = "users"   # Table name in DB
    
    id = Column(Integer,primary_key=True,index=True)   # Primary key column
    username = Column(String(50),unique=True,nullable=False)   # Username must be unique and not null
    password = Column(String(50),unique=True,nullable=False)   # Password must be unique and not null
    
    task = relationship("Task",back_populates="user")   # Relationship with Task table (one-to-many)

class Task(Base):   # Define Task table model
    __tablename__ = "tasks"   # Table name in DB
    
    id = Column(Integer,primary_key=True,index=True)   # Primary key column
    title = Column(String(50))   # Task title
    description = Column(String(100))   # Task description
    completed = Column(Boolean)   # Boolean flag for completion status
    
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)   # Foreign key referencing User
    
    user = relationship("User",back_populates="task")   # Relationship back to User
    
    # def __repr__(self):   # Optional string representation for debugging
    #     return f"User_id = {self.id}, name = {self.name}' email = {self.email}"

# print("Creating tables in mysql DB...")   # Uncomment for debugging
Base.metadata.create_all(bind=engine)   # Create tables in DB based on models
# print("Table creation completed")       # Uncomment for debugging


def get_user_details():   # Function to fetch all users
    try:
        session = SessionLocal()   # Open DB session
        users = session.query(User).all()   # Query all users
        session.close()   # Close session
        return users
    except Exception as e:
        session.rollback()   # Rollback in case of error
        print(e)

def create_task(task:TaskModel,username:str):   # Function to create a new task for a user
    try:
        session = SessionLocal()
        user_data = session.query(User).filter(User.username == username).first()   # Find user by username

        new_task = Task(   # Create new Task object
            title = task.title,
            description = task.description,
            completed = task.completed,
            user_id = user_data.id
        )
        session.add(new_task)   # Add task to session
        session.commit()        # Commit transaction
        session.refresh(new_task)   # Refresh to get updated state
        session.close()
        
        return new_task
    except Exception as e:
        session.rollback()
        raise Exception

def get_all_tasks(username:str):   # Function to fetch all tasks for a user
    try:
        session = SessionLocal()
        user_data = session.query(User).filter(User.username == username).first()   # Find user
        tasks = session.query(Task).filter(Task.user_id == user_data.id).all()      # Get tasks for user
        session.close()
        
        if tasks:
            return tasks
        else:
            raise Exception("No tasks found")
    except Exception:
        raise Exception

def get_task_by_id(task_id,username):   # Function to fetch a specific task by ID
    try:
        session = SessionLocal()
        user_data = session.query(User).filter(User.username == username).first()   # Find user
        task = session.query(Task).filter(Task.user_id == user_data.id).filter(Task.id == task_id).first()   # Find task
        session.close()
        return task
    except Exception:
        raise Exception

def update_task_by_id(task_id,update_task:TaskModel,username):   # Function to update a task by ID
    try:
        session = SessionLocal()
        user_data = session.query(User).filter(User.username == username).first()   # Find user
        task = session.query(Task).filter(Task.user_id == user_data.id).filter(Task.id == task_id).first()   # Find task
    
        if task:
            task.title = update_task.title
            task.description = update_task.description
            task.completed = update_task.completed
            task.user_id = user_data.id
            session.commit()
            session.refresh(task)
        else:
            raise Exception("Task not found")
        session.close()
        
        return task
    except Exception:
        raise Exception

def delete_task_by_id(task_id,username):   # Function to delete a task by ID
    try:
        session = SessionLocal()
        user_data = session.query(User).filter(User.username == username).first()   # Find user
        task = session.query(Task).filter(Task.user_id == user_data.id).filter(Task.id == task_id).first()   # Find task
        print(task)   # Debug print
        if task:
            session.delete(task)   # Delete task
            session.commit()
        else:
            raise Exception("Task not found")
        session.close()
        
        return "Task deleted successfully"
    except Exception :
        raise Exception