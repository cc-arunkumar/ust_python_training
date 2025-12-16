from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database.sql_db import Base, engine

class TaskSchema(Base):
    __tablename__ = "tasks"
    t_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description=Column(String(250),unique=True,nullable=False)
    assigned_to= Column(Integer, ForeignKey("employees.e_id"))  
    assigned_by=Column(Integer, ForeignKey("employees.e_id"))
    assigned_at=Column(DateTime)
    updated_by=Column(Integer, ForeignKey("employees.e_id"))
    updated_at=Column(DateTime)
    priority=Column(String(10),nullable=False)
    status=Column(String(20),nullable=False)
    reviewer=Column(Integer, ForeignKey("employees.e_id"))
    created_by=Column(Integer, ForeignKey("employees.e_id"))
    expected_closure=Column(DateTime,nullable=False)
    actual_closure=Column(DateTime)
    
    

    def __repr__(self):
        return f"<Employee(e_id={self.e_id}, name={self.name}, email={self.email}, designation={self.designation}, manager id={self.mgr_id})>"
    
Base.metadata.create_all(bind=engine)