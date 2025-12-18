from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database.connection import Base

class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500))

    status = Column(String(50))      # TO_DO / IN_PROGRESS / REVIEW / DONE
    priority = Column(String(50))    # High / Medium / Low

    assigned_to_id = Column(Integer, ForeignKey("employees.emp_id"))
    created_by_id = Column(Integer, ForeignKey("employees.emp_id"))
    assigned_by_id= Column(Integer, ForeignKey("employees.emp_id"))
    assigned_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    updated_by = Column(String(255))

    reviewer = Column(Integer, ForeignKey("employees.emp_id"))
    remarks = Column(String(500))

    expected_closure = Column(DateTime)
    actual_closure = Column(DateTime)

    assigned_to = relationship("EmployeeDB", foreign_keys=[assigned_to_id])
    assigned_by = relationship("EmployeeDB", foreign_keys=[assigned_by_id])
    created_by = relationship("EmployeeDB", foreign_keys=[created_by_id])
    reviewer_emp = relationship("EmployeeDB", foreign_keys=[reviewer])
