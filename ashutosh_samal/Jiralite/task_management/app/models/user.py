from sqlalchemy import Column, Integer, String, Enum, JSON
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    e_id = Column(Integer, primary_key=True, index=True)
    password = Column(String(100), nullable=False)      # plain password (as required)
    roles = Column(JSON, nullable=False)                # ["ADMIN","MANAGER","DEVELOPER"]
    status = Column(Enum("ACTIVE", "INACTIVE"), default="ACTIVE")
