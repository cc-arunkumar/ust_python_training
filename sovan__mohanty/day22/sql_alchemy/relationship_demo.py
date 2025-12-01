from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Database connection URL
DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

# Create engine and session
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# Department model
class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    # Relationship with Employee
    employee = relationship("Employee", back_populates="department")

# Employee model
class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    # Relationship with Department
    department = relationship("Department", back_populates="employee")

# Create tables
print("Creating tables...")
Base.metadata.create_all(engine)
print("Tables created successfully")

# Create a department
def create_department(name: str):
    session = SessionLocal()
    try:
        dept = Department(name=name)
        session.add(dept)
        session.commit()
        session.refresh(dept)
        return dept
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()

new_dept = create_department("IT")
print(new_dept)

# Create an employee
def create_employee(name: str, dept_id: int):
    session = SessionLocal()
    try:
        new_employee = Employee(name=name, department_id=dept_id)
        session.add(new_employee)
        session.commit()
        session.refresh(new_employee)
        return new_employee
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()

# Fetch all employees
def get_all_employees():
    session = SessionLocal()
    try:
        employee = session.query(Employee).all()
        return employee
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return []
    finally:
        session.close()

print(get_all_employees())

# Fetch employees by department id
def get_employees_by_department(dept_id: int):
    session = SessionLocal()
    try:
        employee = session.query(Employee).filter(Employee.department_id == dept_id).all()
        return employee
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return []
    finally:
        session.close()

print(get_employees_by_department(1))

# Fetch all departments
def get_all_department():
    session = SessionLocal()
    try:
        employee = session.query(Department).all()
        return employee
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return []
    finally:
        session.close()

print(get_all_department())

# Fetch employees with their department name
def get_employees_with_department():
    session = SessionLocal()
    try:
        employee = session.query(Employee).all()
        return [{"id": emp.id, "name": emp.name, "department": emp.department.name if emp.department else None}
                for emp in employee]
    finally:
        session.close()

print(get_employees_with_department())
