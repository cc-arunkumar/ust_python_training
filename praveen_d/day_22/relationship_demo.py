from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "mysql+pymysql://root:pass%40word@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String(50), nullable=False)

    employees = relationship("Employee", back_populates='department')


class Employee(Base):
    __tablename__ = 'employees'

    emp_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    dept_id = Column(Integer, nullable=False)
    department = relationship("Department", back_populates='employees')


# Function to create a department
def create_department(name: str):
    session = SessionLocal()
    dept = Department(name=name)
    session.add(dept)
    session.commit()
    session.refresh(dept)
    session.close()

    return dept


# Function to create an employee
def create_employee(name: str, department_id: int):
    session = SessionLocal()
    emp = Employee(name=name, dept_id=department_id)
    session.add(emp)
    session.commit()
    session.refresh(emp)
    session.close()

    return emp


# Fetch all employees across all departments
def get_all_emp():
    session = SessionLocal()
    employees = session.query(Employee).all()
    session.close()
    return employees


# Fetch employees of a specific department
def fetch_emp_via_dept(dept_name: str):
    session = SessionLocal()

    # First, get the department by name
    department = session.query(Department).filter(Department.name == dept_name).first()
    
    if department is None:
        session.close()
        return []  # Return empty list if department not found

    # Then, get employees based on the department's id
    employees = session.query(Employee).filter(Employee.dept_id == department.id).all()
    session.close()

    return employees


# Fetch employees with department names
def fetch_emp_with_dept_name():
    session = SessionLocal()

    # Using join to fetch employees with their respective department names
    employees = session.query(Employee, Department).join(Department).all()
    session.close()

    return employees


def main():
    # Create a department
    dept = create_department("HR")

    # Create employees
    create_employee("Arun", dept.id)
    create_employee("Mohan", dept.id)

    # Get all employees
    employees = get_all_emp()
    for emp in employees:
        print(f"Employee ID: {emp.emp_id}, Name: {emp.name}")

    # Fetch employees of a specific department
    hr_employees = fetch_emp_via_dept("HR")
    for emp in hr_employees:
        print(f"HR Employee: {emp.name}")

    # Fetch employees with department names
    emp_with_dept = fetch_emp_with_dept_name()
    for emp, dept in emp_with_dept:
        print(f"Employee: {emp.name}, Department: {dept.name}")


if __name__ == "__main__":
    main()
