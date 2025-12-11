from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pymongo import MongoClient

DATABASE_URL = "mysql+pymysql://root:password123@localhost/ust_task_tracker_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

client = MongoClient("mongodb://localhost:27017/")
db = client["ust_task_tracker_db"]
audit_logs = db["audit_logs"]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

