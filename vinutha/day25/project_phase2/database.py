from sqlalchemy import create_engine  # Import SQLAlchemy's create_engine to establish a connection to the database
from sqlalchemy.orm import sessionmaker, declarative_base  # Import sessionmaker to create sessions and declarative_base for base class

# Define the connection string for MySQL using pymysql as the driver
DATABASE_URL = "mysql+pymysql://root:password1@localhost/ust_task_manager_db"

# Create the database engine, which will manage connections to the MySQL database
engine = create_engine(DATABASE_URL)

# Create a session factory that can be used to instantiate database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for all SQLAlchemy models; all models will inherit from this
Base = declarative_base()

# Dependency to get the database session
def get_db():
    """
    Provides a database session that can be used in FastAPI endpoints.
    
    This function is used as a dependency in routes to ensure a new session is created for each request.
    After the request completes, the session is closed to avoid resource leaks.
    """
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session for use in the route
    finally:
        db.close()  # Close the session when the request is done
