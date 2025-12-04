from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "mysql+pymysql://root:raswanthi_1@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# -----------------------------
# Models
# -----------------------------
class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    employees = relationship("Employee", back_populates="department")

    def __repr__(self):
        return f"<Department(id={self.id}, name='{self.name}')>"


class Employee(Base):
    __tablename__ = "employees"
    
    emp_id = Column(Integer, primary_key=True, index=True)
    emp_name = Column(String(50), nullable=False)
    
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")

    def __repr__(self):
        return f"<Employee(id={self.emp_id}, name='{self.emp_name}', department_id={self.department_id})>"

# -----------------------------
# Create tables
# -----------------------------
Base.metadata.create_all(engine)

# -----------------------------
# CRUD Functions with prints
# -----------------------------
def create_department(name: str):
    try:
        session = SessionLocal()
        dept = Department(name=name)
        session.add(dept)
        session.commit()
        session.refresh(dept)
        print(f"Department created: {dept}")
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None 
    finally:
        session.close()
    return dept


def create_employee(emp_name: str, department_id: int):
    try:
        session = SessionLocal()
        emp = Employee(emp_name=emp_name, department_id=department_id)
        session.add(emp)
        session.commit()
        session.refresh(emp)
        print(f"Employee created: {emp.emp_name}, Department ID: {emp.department_id}")
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None 
    finally:
        session.close()
    return emp


def get_all_employees():
    try:
        session = SessionLocal()
        employees = session.query(Employee).all()
        for emp in employees:
            print(f"Employee: {emp.emp_name}, Department: {emp.department.name}")
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return employees


def get_employee_of_department(name: str):
    """Fetch employees of a specific department by name"""
    try:
        session = SessionLocal()
        dept = session.query(Department).filter(Department.name == name).first()
        if dept:
            print(f"Employees in {dept.name} Department:")
            for emp in dept.employees:
                print(f"- {emp.emp_name}")
            return dept.employees
        else:
            print(f"No department found with name {name}")
            return []
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()


def get_department_with_employees(department_id: int):
    """Fetch a department with all employees"""
    try:
        session = SessionLocal()
        dept = session.query(Department).filter(Department.id == department_id).first()
        if dept:
            print(f"Department: {dept.name}, Employees: {[emp.emp_name for emp in dept.employees]}")
        else:
            print(f"No department found with ID {department_id}")
        return dept
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()


def get_employee_with_department(emp_id: int):
    """Fetch an employee along with their department"""
    try:
        session = SessionLocal()
        emp = session.query(Employee).filter(Employee.emp_id == emp_id).first()
        if emp:
            print(f"Employee: {emp.emp_name}, Department: {emp.department.name}")
        else:
            print(f"No employee found with ID {emp_id}")
        return emp
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()

# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    # create_department("IT")
    # create_department("HR")

    create_employee("Sameera",1)
    create_employee("Sindhu",2)

    get_all_employees()
    get_employee_of_department("IT")
    get_department_with_employees(1)
    get_employee_with_department(1)
