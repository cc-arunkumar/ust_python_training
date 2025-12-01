from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, joinedload

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")

print("Creating tables...")
Base.metadata.create_all(engine)
print("Tables Created Successfully")

def create_department(name: str):
    session = SessionLocal()
    dep = Department(name=name)
    session.add(dep)
    session.commit()
    session.refresh(dep)
    session.close()
    return dep

def create_employee(name: str, department_id: int):
    session = SessionLocal()
    emp = Employee(name=name, department_id=department_id)
    session.add(emp)
    session.commit()
    session.refresh(emp)
    session.close()
    return emp

def get_all_employees():
    session = SessionLocal()
    employees = session.query(Employee).all()
    session.close()
    return employees

def get_department_with_employees(department_id: int):
    session = SessionLocal()
    department = (
        session.query(Department)
        .options(joinedload(Department.employees))
        .filter(Department.id == department_id)
        .first()
    )
    session.close()
    return department

def get_employee_with_department(emp_name: str):
    session = SessionLocal()
    employee = (
        session.query(Employee)
        .options(joinedload(Employee.department).joinedload(Department.employees))
        .filter(Employee.name == emp_name)
        .first()
    )
    session.close()
    return employee

if __name__ == "__main__":
    dep = create_department("AIML")
    emp1 = create_employee("madhan", dep.id)
    emp2 = create_employee("Reveen", dep.id)

    employees = get_all_employees()
    print("All Employees:")
    for e in employees:
        print(f"Employee: {e.name}, Department ID: {e.department_id}")

    department = get_department_with_employees(dep.id)
    print(f"Department: {department.name}")
    for emp in department.employees:
        print(f"Employee: {emp.name}, ID: {emp.id}")

    employee = get_employee_with_department(emp1.name)
    print(f"Employee: {employee.name}, Department: {employee.department.name}")
    for emp in employee.department.employees:
        print(f"{emp.name}")


    """
    SAMPLE OUTPUT
    
    Creating tables...
Tables Created Successfully
All Employees:
Employee: madhan, Department ID: 1
Employee: reveen, Department ID: 1
Employee: madhan, Department ID: 2
Employee: reveen, Department ID: 2
Department: AIML
Employee: madhan, ID: 3
Employee: reveen, ID: 4
Employee: madhan, Department: AIML
madhan
reveen
    """