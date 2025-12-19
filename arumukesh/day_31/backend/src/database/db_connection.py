from sqlalchemy import create_engine, Integer, String, Column, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime
database_url = "mysql+pymysql://root:pass%40word1@localhost:3306/task_manager_db"

engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)