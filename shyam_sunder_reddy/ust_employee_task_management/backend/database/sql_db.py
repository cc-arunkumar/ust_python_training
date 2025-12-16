from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:password123@localhost:3306/ust_task_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Shared Base for all schema modules so ForeignKey references resolve
Base = declarative_base()


def get_connection():
    return SessionLocal()
    