from sqlalchemy import create_engine, Column, String,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base,Session
from services.database import Base
from schemas.employee import EmployeeSchema


class Employee(Base):
    __tablename__ = "employees"

    emp_id = Column(String(50), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    designation = Column(String(100), nullable=False)
    mgr_id = Column(String(50), ForeignKey("employees.emp_id"), nullable=True)  # Manager ID (string FK)


def create_employee(db:Session, emp:EmployeeSchema):
    data = emp.dict()
    # If designation provided as list, store as comma-separated string in SQL column
    if isinstance(data.get('designation'), list):
        data['designation'] = ','.join(data['designation'])
    # Normalize empty manager id to None so DB stores NULL instead of empty string
    if 'mgr_id' in data and (data['mgr_id'] is None or str(data['mgr_id']).strip() == ''):
        data['mgr_id'] = None
    new_emp=Employee(**data)
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

def get_employees(db: Session):
    return db.query(Employee).all()


# READ ONE
def get_employee(db: Session, emp_id: str):
    return db.query(Employee).filter(Employee.emp_id == emp_id).first()


# UPDATE
def update_employee(db: Session, emp_id: str, emp_data: EmployeeSchema):
    emp = db.query(Employee).filter(Employee.emp_id == emp_id).first()

    if not emp:
        return None

    incoming = emp_data.dict()
    if isinstance(incoming.get('designation'), list):
        incoming['designation'] = ','.join(incoming['designation'])
    # Normalize empty manager id to None so DB stores NULL instead of empty string
    if 'mgr_id' in incoming and (incoming['mgr_id'] is None or str(incoming['mgr_id']).strip() == ''):
        incoming['mgr_id'] = None
    for key, value in incoming.items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)
    return emp


# DELETE
def delete_employee(db: Session, emp_id: str):
    emp = db.query(Employee).filter(Employee.emp_id == emp_id).first()

    if not emp:
        return False

    db.delete(emp)
    db.commit()
    return True
    
    
