from sqlalchemy import create_engine,Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker,relationship, declarative_base
import enum
 
DATABASE_URL = "mysql+pymysql://root:password123@localhost:3306/ust_emp_mang"
 
engine = create_engine(DATABASE_URL,echo=True)
 
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base = declarative_base()
 
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
 
 
class User(Base):
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(Integer, ForeignKey("employees.id"), nullable=False)  # link to Employee
    password = Column(String(255), nullable=False, default="default_password")
    role = Column(String(255))  # store as comma-separated or JSON string
    status = Column(Enum(StatusEnum), default=StatusEnum.inactive)
 
    employee = relationship("Employee", back_populates="users")
 
    def __repr__(self):
        return f"<User(emp_id={self.emp_id}, status={self.status}, role={self.role})>"

Base.metadata.create_all(bind=engine)