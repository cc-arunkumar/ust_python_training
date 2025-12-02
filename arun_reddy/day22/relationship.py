from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
 
DATABASE_URL = 'mysql+pymysql://root:password123@localhost:3306/ust_db'
 
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
 
Base = declarative_base()
 
class Department(Base):
    __tablename__='departments'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50),nullable=False)
    employees=relationship("Employee",back_populates='department')
class Employee(Base):
    __tablename__='employees'
    id = Column(Integer, primary_key=True,index=True)
    name=Column(String(50),nullable=False)
    department_id=Column(Integer,ForeignKey("departments.id"))
    department=relationship('Department',back_populates='employees')
 
print("creating table..")
Base.metadata.create_all(engine)
print("table created")
 
def create_department(name):
    db=SessionLocal()
    try:
        dept=Department(name=name)
        db.add(dept)
        db.commit()
        db.refresh(dept)
        return dept
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.close()
def create_employee(name,department_id):
    db=SessionLocal()
    try:
        emp=Employee(name=name,department_id=department_id)
        db.add(emp)
        db.commit()
        db.refresh(emp)
        return emp
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.close()

 
def get_all_employees():
    db=SessionLocal()
    try:
        employees=db.query(Employee).all()
        return employees
    except Exception as e:
        print(e)
    finally:
        db.close()

def get_employees_by_department(dept_name):
    db=SessionLocal()
    try:
        employees=db.query(Employee).join(Department).filter(Department.name==dept_name).all()
        return employees
    except Exception as e:
        print(e)
    finally:
        db.close()
def get_department_with_employees(dept_id):
    db=SessionLocal()
    try:
        dept=db.query(Department).filter(Department.id==dept_id).first()
        if dept:
            return {"department":dept,"employees":dept.employees}
        return None
    except Exception as e:
        print(e)
    finally:
        db.close()

def get_employee_with_department(emp_id):
    db=SessionLocal()
    try:
        emp=db.query(Employee).filter(Employee.id==emp_id).first()
        if emp:
            return {"employee":emp,"department":emp.department}
        return None
    except Exception as e:
        print(e)
    finally:
        db.close()