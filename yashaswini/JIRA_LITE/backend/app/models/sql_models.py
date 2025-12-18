# app/models/sql_models.py
from sqlalchemy import Column, String, Integer, ForeignKey
from app.db.mysql import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(String(10), unique=True, nullable=False)   # PK for business logic
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    designation = Column(String(50), nullable=False)
    manager_id = Column(String(10), nullable=True)

class User(Base):
    __tablename__ = "users"
    emp_id = Column(String(10), ForeignKey("employees.emp_id"), primary_key=True)
    password = Column(String(255), nullable=False)
    roles = Column(String(50), nullable=False)
    status = Column(String(20), default="active")
