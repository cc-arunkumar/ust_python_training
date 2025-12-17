from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.mysql import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(Integer, ForeignKey("employees.emp_id"), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)
    status = Column(String(20), default="ACTIVE")

    employee = relationship("Employee", back_populates="users")
