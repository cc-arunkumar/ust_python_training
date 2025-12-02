from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    
    employees = relationship("Employee", back_populates="department")


class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
    
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    department = relationship("Department", back_populates="employees")

Base.metadata.create_all(bind=engine)
print("Tables created")

def create_employee(name: str, email: str, department_id: int = None):
    try:
        session = SessionLocal()
        new_employee = Employee(name=name, email=email, department_id=department_id)
        session.add(new_employee)
        session.commit()
        session.refresh(new_employee)
        print("Created employee table")
        return new_employee
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        session.close()
        
def create_department(name: str):
    try:
        session = SessionLocal()
        new_department = Department(name=name)
        session.add(new_department)
        session.commit()
        session.refresh(new_department)
        print("Created department table")
        return new_department
    
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        session.close()
        
def get_all():
    try:
        session = SessionLocal()
        emps = session.query(Employee).all()
        depts=session.query(Department).all()
        for d in depts:
            print(f"{d.id},{d.name}")
        for e in emps:
            print(f"{e.id},{e.name},{e.email},{e.department.name}")
            
    except Exception as e:
        print("Error", e)
    finally:
        session.close()

def get_employee_by_id(id: int):
    try:
        session = SessionLocal()
        emp = session.query(Employee).filter(Employee.id == id).first()
        print(f"{emp.id}, {emp.name}, {emp.email}, {emp.department.name}")
    except Exception as e:
        print("Error:", e)
    finally:
        session.close()
        
def get_employee_by_dept(dept_id:int):
    try:
        session = SessionLocal()
        emp = session.query(Employee).filter(Employee.department_id == dept_id).all()
        for e in emp:
            print(f"{e.id}, {e.name}, {e.email}, {e.department.name}")
    except Exception as e:
        print("Error:", e)
    finally:
        session.close()


if __name__ == "__main__":
  
    create_department("IT")
    create_department("HR")
    create_department("Finance")
    create_department("CS")
    create_department("Sales")
    create_department("Banking")
    
    create_employee("prithvi","prithvi@ust.com",3)
    create_employee("rohit","rohit@ust.com",4)
    
    get_all()
    get_employee_by_id(1)
    get_employee_by_dept(4)
    

