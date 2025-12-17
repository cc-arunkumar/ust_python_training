from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base


class Employee(Base):
    __tablename__ = "employees"

    e_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    designation = Column(String(50))
    manager_id = Column(Integer, ForeignKey("employees.e_id"), nullable=True)
