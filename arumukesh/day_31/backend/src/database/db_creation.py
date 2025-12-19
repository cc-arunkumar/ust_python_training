from sqlalchemy import create_engine, Integer, String, Column, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime

database_url = "mysql+pymysql://root:pass%40word1@localhost:3306/task_manager_db"
engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    emp_id = Column(Integer, primary_key=True, unique=True)
    password = Column(String(50), nullable=False)
    # Store roles as comma-separated string or use a separate role table
    role = Column(String(100), nullable=False)  # e.g., "admin,manager,employee"
    
class Employee(Base):
    __tablename__ = "employees"
    emp_id = Column(String(20), primary_key=True, unique=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    designation = Column(String(50), nullable=False)
    mgr_id = Column(String(20), ForeignKey('employees.emp_id'), nullable=True)
    
    # Self-referential relationship for manager
    manager = relationship("Employee", remote_side=[emp_id], backref="subordinates")
    
class Tasks(Base):
    __tablename__ = "tasks"
    t_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    created_by = Column(String(50), ForeignKey('employees.emp_id'), nullable=False)
    assigned_to = Column(String(50), ForeignKey('employees.emp_id'), nullable=False)
    assigned_by = Column(String(50), ForeignKey('employees.emp_id'), nullable=False)
    assigned_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_by = Column(String(20), ForeignKey('employees.emp_id'))
    updated_at = Column(DateTime, onupdate=datetime.now)
    priority = Column(String(10), nullable=False)  # e.g., "high", "medium", "low"
    status = Column(String(20), nullable=False)    # e.g., "pending", "in_progress", "completed"
    remarks = Column(String(500))
    reviewer = Column(String(20), ForeignKey('employees.emp_id'), nullable=False)
    expected_closure = Column(DateTime, nullable=False)
    actual_closure = Column(DateTime)
    
    # Relationships
    creator = relationship("Employee", foreign_keys=[created_by], backref="tasks_created")
    assignee = relationship("Employee", foreign_keys=[assigned_to], backref="tasks_assigned")
    assigner = relationship("Employee", foreign_keys=[assigned_by], backref="tasks_assigned_by_me")
    updater = relationship("Employee", foreign_keys=[updated_by], backref="tasks_updated")
    reviewer_emp = relationship("Employee", foreign_keys=[reviewer], backref="tasks_to_review")

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")