from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Adjust with your own MySQL credentials
DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/task_manager"

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
