from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from app.db.mysql import Base


# -------------------------
# Employees Table
# -------------------------

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(String(10), unique=True, nullable=False)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    designation = Column(String(50))
    manager_id = Column(String(10), nullable=True)
    is_active = Column(Boolean, default=True)






# -------------------------
# Users Table
# -------------------------
class User(Base):
    __tablename__ = "users"

    emp_id = Column(String(5), ForeignKey("employees.emp_id"), primary_key=True)
    password = Column(String(100), nullable=False)
    roles = Column(String(20), nullable=False)   # admin / manager / developer
    status = Column(String(20), nullable=False) # active / inactive
    is_active = Column(Boolean, default=True)
