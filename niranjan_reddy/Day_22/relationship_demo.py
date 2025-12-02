# Import required SQLAlchemy components
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base


# ----------------------------
# DATABASE CONFIGURATION
# ----------------------------

# MySQL database connection URL
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/ust_db"

# Create SQLAlchemy engine (echo=True prints SQL queries)
engine = create_engine(DATABASE_URL, echo=True)

# Create session factory for DB transactions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for all ORM models
Base = declarative_base()


# ----------------------------
# ORM MODELS
# ----------------------------

class Department(Base):
    """
    Department table model
    """
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    # Relationship: One department → many employees
    employees = relationship("Employee", back_populates="department")


class Employee(Base):
    """
    Employee table model
    """
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    # Foreign key linking employee to department
    department_id = Column(Integer, ForeignKey("departments.id"))

    # Relationship: Employee belongs to one department
    department = relationship("Department", back_populates="employees")


# Create tables in MySQL
print("Creating tables in MySQL DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed.")


# ----------------------------
# CRUD OPERATIONS
# ----------------------------

def create_department(name: str):
    """
    Create a new department.
    """
    try:
        session = SessionLocal()

        # Create department object
        dept = Department(name=name)

        # Add and save to DB
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


def create_employee(name: str, department_id: int):
    """
    Create a new employee under a given department.
    """
    try:
        session = SessionLocal()

        emp = Employee(name=name, department_id=department_id)

        session.add(emp)
        session.commit()
        session.refresh(emp)

        return emp

    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None

    finally:
        session.close()


def get_all_employess():
    """
    Fetch all employees.
    """
    try:
        session = SessionLocal()
        employees = session.query(Employee).all()
        return employees

    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None

    finally:
        session.close()


def get_employees_by_department(department_name: str):
    """
    Fetch all employees belonging to a specific department name.
    """
    session = SessionLocal()

    dept = session.query(Department).filter(Department.name == department_name).first()

    if dept:
        return dept.employees  # Access related employees

    session.close()


def get_department_with_all_emp(department_name: str):
    """
    Fetch one department along with all its employees.
    """
    session = SessionLocal()

    department = session.query(Department).filter(Department.name == department_name).first()

    if department:
        print(f"Department Name: {department.name}")
        print(f"Department ID: {department.id}")
        print("Employees:")

        # List employees in this department
        for emp in department.employees:
            print(f"  Employee ID: {emp.id}, Name: {emp.name}, Department ID: {emp.department_id}")

        return department

    session.close()


# ----------------------------
# MAIN EXECUTION
# ----------------------------

if __name__ == "__main__":

    # Example to create department and employees
    # department = create_department("HR")
    # print("Department Name:", department.name)

    # emp1 = create_employee("Niru", department.id)
    # print("Employee:", emp1.name)

    # Fetch all employees
    # emp_list = get_all_employess()
    # for e in emp_list:
    #     print(f"Name: {e.name}, Department_id: {e.department_id}")

    department_name = "Finance"

    # Fetch department and all employees
    department = get_department_with_all_emp(department_name)

    if department:
        print(f"Department '{department_name}' and its employees were fetched successfully.")
    else:
        print("Department and employees not found.")
