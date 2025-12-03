from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

engine = create_engine(DATABASE_URL, echo=True)
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

print("Creating tables in MySQL DB..")
Base.metadata.create_all(engine)
print("Table creation completed")

# ---------------- Utility Functions ---------------- #

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
        print("Error while creating department:", e)
        return None
    finally:
        session.close()

def create_employee(name: str, department_id: int):
    session = SessionLocal()
    try:
        emp = Employee(name=name, department_id=department_id)
        session.add(emp)
        session.commit()
        session.refresh(emp)
        return emp
    except Exception as e:
        session.rollback()
        print("Error while creating employee:", e)
        return None
    finally:
        session.close()

def get_department_with_employees(dept_id: int):
    """Fetch a department and all its employees"""
    session = SessionLocal()
    try:
        dept = session.query(Department).filter(Department.id == dept_id).first()
        if not dept:
            print("Department not found")
            return None
        return dept
    except Exception as e:
        print("Error fetching department:", e)
        return None
    finally:
        session.close()

def get_all_departments():
    """Fetch all departments with their employees"""
    session = SessionLocal()
    try:
        departments = session.query(Department).all()
        return departments
    except Exception as e:
        print("Error fetching departments:", e)
        return []
    finally:
        session.close()

# ---------------- Calling Part ---------------- #

if __name__ == "__main__":
    # Create sample departments
    dept1 = create_department("IT")
    dept2 = create_department("HR")
    print("Created Departments:", dept1, dept2)

    # Create sample employees
    emp1 = create_employee("Taniya", dept1.id)
    emp2 = create_employee("Tanu", dept2.id)
    emp3 = create_employee("Rahul", dept1.id)
    print("Created Employees:", emp1, emp2, emp3)

    # Fetch one department with employees
    print("\n=== Department with Employees (IT) ===")
    dept = get_department_with_employees(dept1.id)
    if dept:
        print(f"Department: {dept.name}")
        for emp in dept.employees:
            print(f"   Employee ID: {emp.id}, Name: {emp.name}")

    # Fetch all departments with employees
    print("\n=== All Departments with Employees ===")
    departments = get_all_departments()
    for dept in departments:
        print(f"Department: {dept.name}")
        for emp in dept.employees:
            print(f"   Employee ID: {emp.id}, Name: {emp.name}")
