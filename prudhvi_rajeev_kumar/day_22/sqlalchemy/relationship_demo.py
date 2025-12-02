from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base  = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    employees = relationship("Employee", back_populates='department')
    
class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    department = relationship("Department", back_populates='employees')
    
print("Creating Tables...")
Base.metadata.create_all(engine)
print("Tables Created.")

def create_department(name : str):
    try:
        session = SessionLocal()
        new_department = Department(name=name)
        session.add(new_department)
        session.commit()
        session.refresh(new_department)
    except Exception as e:
        session.rollback()
        print("Exception as : ", e)
        return None
    finally:
        session.close()
    
    return new_department

def create_employee(name:str, department_id : int):
    try:
        session = SessionLocal()
        new_employee = Employee(name=name, department_id=department_id)
        session.add(new_employee)
        session.commit()
        session.refresh(new_employee)
    except Exception as e:
        session.rollback()
        print("Exception as : ", e)
        return None
    finally:
        session.close()
    
    return new_employee
def fetch_all_employees():
    try:
        session = SessionLocal()
        employees = session.query(Employee).all()
    except Exception as e:
        session.rollback()
        print("Exception as ", e)
        return None
    finally:
        session.close()
    return employees

def fetch_employee_by_dept(dept_id: int):
    try: 
        session = SessionLocal()
        department = session.query(Department).filter(Department.id == dept_id).first()
        if department is None:
            print("No department found.")
            return None
        # return department.employees   # returns a list
    except Exception as e:
        session.rollback()
        print("Exception in fetch_employees_for_department:", e)
        return None
    finally:
        session.close()
    return department

def fetch_dept_with_all_employees(dept_name : str):
    try:
        session = SessionLocal()
        employee = session.query(Department).filter(Department.name == dept_name).first()
        if employee is None:
            print("No Employee found.")
            return None
        return employee.employees
    except Exception as e:
        session.rollback()
        print("exception is ", e)
        return None
    finally:
        session.close()
        

if __name__ == "__main__":
    new_dept = create_department("IT Dept.")
    print(f"Department name : {new_dept.name}, Id : {new_dept.id}")
    new_dept = create_department("HR Dept.")
    print(f"Department name : {new_dept.name}, Id : {new_dept.id}")
    new_emp = create_employee("Rohit", 2)
    print(f"Employee id : {new_emp.id}, Name : {new_emp.name}, Department_id : {new_emp.department_id}")
    
    employees = fetch_all_employees()
    for i in employees:
        print(f"ID : {i.id}, Name : {i.name}, Department_id : {i.department_id}")
    
    fetch = fetch_employee_by_dept(1)
    if fetch:
        for emp in fetch:
            print(f"Employee id: {emp.id}, Name: {emp.name}, Department: {emp.department.name}")
