from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL (MySQL with pymysql driver)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:pass1word@localhost:3306/ust_task_manager_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session factory (handles DB sessions)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

# Dependency function to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db   
    finally:
        db.close() 
