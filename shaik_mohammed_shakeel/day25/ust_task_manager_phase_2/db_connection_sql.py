from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
 
# MySQL connection URL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost/ust_task_manager_db"
 
# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"connect_timeout": 20})
 
# Create a session maker for managing connections
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
# Base class for our ORM models
Base = declarative_base()
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
# Test connection
if engine:
    print("MySQL connected successfully.")
else:
    print("MySQL connection failed.")
 
 