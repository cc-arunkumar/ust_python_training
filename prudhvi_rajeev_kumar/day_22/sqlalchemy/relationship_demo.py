from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    employees = relationship("Employee", back_populates="department", cascade="all, delete-orphan")

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    department = relationship("Department", back_populates="employees")

print("Creating Tables...")
Base.metadata.create_all(engine)
print("Tables Created.")

def create_department(name: str):
    with SessionLocal() as session:
        try:
            new_department = Department(name=name)
            session.add(new_department)
            session.commit()
            session.refresh(new_department)
            return new_department
        except Exception as e:
            session.rollback()
            print("Exception:", e)
            return None

def create_employee(name: str, department_id: int):
    with SessionLocal() as session:
        try:
            new_employee = Employee(name=name, department_id=department_id)
            session.add(new_employee)
            session.commit()
            session.refresh(new_employee)
            return new_employee
        except Exception as e:
            session.rollback()
            print("Exception:", e)
            return None

def fetch_all_employees():
    with SessionLocal() as session:
        try:
            return session.query(Employee).all()
        except Exception as e:
            print("Exception:", e)
            return None

def fetch_employee_by_dept(dept_id: int):
    with SessionLocal() as session:
        try:
            department = session.query(Department).filter(Department.id == dept_id).first()
            if department is None:
                print("No department found.")
                return None
            return department.employees
        except Exception as e:
            print("Exception:", e)
            return None

def fetch_dept_with_all_employees(dept_name: str):
    with SessionLocal() as session:
        try:
            department = session.query(Department).filter(Department.name == dept_name).first()
            if department is None:
                print("No department found.")
                return None
            return department.employees
        except Exception as e:
            print("Exception:", e)
            return None

if __name__ == "__main__":
    # Create departments
    it_dept = create_department("IT Dept.")
    hr_dept = create_department("HR Dept.")
    sales_dept = create_department("Sales Dept.")
    
    print(f"Department: {it_dept.name}, Id: {it_dept.id}")
    print(f"Department: {hr_dept.name}, Id: {hr_dept.id}")
    print(f"Department: {sales_dept.name}, Id: {sales_dept.id}")
    
    # Create employees
    create_employee("Rohit", hr_dept.id)
    create_employee("Priya", it_dept.id)
    create_employee("Amit", it_dept.id)
    create_employee("Sneha", sales_dept.id)
    create_employee("Vikas", sales_dept.id)
    
    # Fetch all employees
    employees = fetch_all_employees()
    print("\nAll Employees:")
    for emp in employees:
        print(f"ID: {emp.id}, Name: {emp.name}, Department: {emp.department.name}")
    
    # Fetch employees by department id
    print("\nEmployees in IT Dept (id=1):")
    it_employees = fetch_employee_by_dept(it_dept.id)
    if it_employees:
        for emp in it_employees:
            print(f"Employee id: {emp.id}, Name: {emp.name}, Department: {emp.department.name}")
    
    # Fetch employees by department name
    print("\nEmployees in Sales Dept:")
    sales_employees = fetch_dept_with_all_employees("Sales Dept.")
    if sales_employees:
        for emp in sales_employees:
            print(f"Employee id: {emp.id}, Name: {emp.name}, Department: {emp.department.name}")
