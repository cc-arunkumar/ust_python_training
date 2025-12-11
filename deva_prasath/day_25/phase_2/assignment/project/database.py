# Import necessary modules from SQLAlchemy to set up the database and ORM
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Define the database URL, which specifies the MySQL database connection
DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost/ust_task_manager_db"


# Create a SQLAlchemy engine that connects to the database using the defined URL
engine = create_engine(DATABASE_URL)


# Create a sessionmaker to manage database sessions for transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare the base class for the ORM models (UserDB, TaskDB)
Base = declarative_base()

# Define the UserDB model, representing the "users" table in the database
class UserDB(Base):
    
    __tablename__ = "users"  # Table name in the database
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    username = Column(String(255), unique=True, index=True)  # Unique username
    password = Column(String(255))  # Password field
    tasks = relationship("TaskDB", back_populates="owner")

# Define the TaskDB model, representing the "tasks" table in the database
class TaskDB(Base):
    __tablename__ = "tasks"  # Table name in the database
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    title = Column(String(255), index=True)  # Task title
    description = Column(String(255))  # Task description
    completed = Column(Boolean, default=False)  # Boolean to track if task is completed
    user_id = Column(Integer, ForeignKey("users.id"))  # Foreign key to link task to a user
    owner = relationship("UserDB", back_populates="tasks")

# Create the tables in the database (if they don't already exist)
Base.metadata.create_all(bind=engine)

# Function to get the database session, ensuring that it's properly managed and closed after use
def get_db():
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session to be used in the calling code (e.g., in FastAPI dependency injection)
    finally:
        db.close()  # Close the session after use
