from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# CHANGE THIS PASSWORD TO YOUR REAL MySQL ROOT PASSWORD
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost/ust_task_manager_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# This is the correct dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
"""import pymysql
from pymongo import MongoClient

# MySQL Connection
def get_db_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="pass@word1",
            database="ust_mysql_db"
        )
        return conn
    except Exception as e:
        print("DB connection Failed:", e)
        return None

# MongoDB Data Push
def push_data_to_mongo():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["ust_mongo_db"]
        collection = db.employees

    except Exception as e:
        print("Error in Pushing to MongoDB ->", e)

    finally:
        client.close()
        print("MongoDB connection closed")
"""