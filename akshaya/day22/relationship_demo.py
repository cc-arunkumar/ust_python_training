from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "mysql+pymysql://root:akshaya@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    employees = relationship("Employee", back_populates='department')

    def __repr__(self):
        return f"<Department(id={self.id}, name='{self.name}')>"

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship('Department', back_populates='employees')

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.name}', department_id={self.department_id})>"

# print("creating tables in mysql db...")
# Base.metadata.create_all(bind=engine)
# print("table creation completed")

def create_department(name: str):
    try:
        session = SessionLocal()
        new_dept = Department(name=name)
        session.add(new_dept)
        session.commit()
        session.refresh(new_dept)
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return new_dept.__dict__

def create_employee(name: str, department_id: int):
    try:
        session = SessionLocal()
        new_emp = Employee(name=name, department_id=department_id)
        session.add(new_emp)
        session.commit()
        session.refresh(new_emp)
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return new_emp.__dict__

def get_employees_by_department(department_name: str):
    employees = []   
    session = SessionLocal()
    try:
        department = session.query(Department).filter(Department.name == department_name).first()
        if department:
            employees = department.employees
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return employees

def get_department_with_employees(department_id: int):
    try:
        session = SessionLocal()
        department = session.query(Department).filter(Department.id == department_id).first()
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return department

def get_employee_with_department(employee_id: int):
    try:
        session = SessionLocal()
        employee = session.query(Employee).filter(Employee.id == employee_id).first()
        if employee:
            department_name = employee.department.name if employee.department else None
            employee_info = {"employee_name": employee.name, "department_name": department_name}
        else:
            employee_info = None
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return employee_info

def get_all_employees():
    try:
        session = SessionLocal()
        employees = session.query(Employee).all()
        for data in employees:
            print({"id": data.id, "name": data.name, "department_id": data.department_id})
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return employees


for emp in get_employees_by_department("IT"):
    print(emp)

print(get_department_with_employees(1))

print(get_employee_with_department(1))

get_all_employees()
