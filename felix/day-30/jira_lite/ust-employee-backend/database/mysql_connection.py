from sqlalchemy import Column, Integer, String, Enum, ForeignKey, create_engine, JSON
from sqlalchemy.orm import relationship, declarative_base,sessionmaker
from sqlalchemy.ext.mutable import MutableList
import enum
 
DATABASE_URL = "mysql+pymysql://root:felix_123@localhost:3306/ust_jira_lite"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base = declarative_base()
 
# Enum for status
class StatusEnum(enum.Enum):
    inactive = "inactive"
    active = "active"
 
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    designation = Column(String(100))
    manager_id = Column(Integer)  # no FK if you prefer
    users = relationship("User", back_populates="employee")
    
# print("Creating Employee table.")
# Base.metadata.create_all(bind=engine)
# print("Table creation completed")
 
 
class User(Base):

    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(Integer, ForeignKey("employees.id"), nullable=False)  # link to Employee
    password = Column(String(255), nullable=False, default="default_password")
    # store roles as a JSON array in MySQL (JSON column)
    # existing values may need migration if previously stored as comma-separated strings
    
    role = Column(MutableList.as_mutable(JSON), nullable=True, default=list)

    status = Column(Enum(StatusEnum), default=StatusEnum.inactive)
    employee = relationship("Employee", back_populates="users")
    def __repr__(self):

        return f"<User(emp_id={self.emp_id}, status={self.status}, role={self.role})>"
    
# print("Creating User table in mysql DB...")
# Base.metadata.create_all(bind=engine)
# print("Table creation completed")

