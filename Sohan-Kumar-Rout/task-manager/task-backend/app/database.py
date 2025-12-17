from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ---------------------------------------------------------
# MySQL CONFIGURATION
# ---------------------------------------------------------

MYSQL_USER = "root"
MYSQL_PASSWORD = "pass%40word1"   # URL‑encoded password (pass@word1 → pass%40word1)
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "ust_employee_task"

# SQLAlchemy connection URL
DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

# ---------------------------------------------------------
# SQLAlchemy ENGINE + SESSION
# ---------------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # prevents stale connections
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all models
Base = declarative_base()
