from sqlalchemy import Column, Integer, String
from database.sql_db import Base, engine

class EmployeeSchema(Base):
    __tablename__ = "employees"
    e_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email=Column(String(100),unique=True,nullable=False)
    designation= Column(String(50), nullable=False)  
    mgr_id=Column(Integer,nullable=False)
    

    def __repr__(self):
        return f"<Employee(e_id={self.e_id}, name={self.name}, email={self.email}, designation={self.designation}, manager id={self.mgr_id})>"
    
Base.metadata.create_all(bind=engine)