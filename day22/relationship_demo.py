from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Database connection string (MySQL with PyMySQL driver)
DATABASE_URL = 'mysql+pymysql://root:password1@localhost:3306/ust_db'

# Create engine (echo=True prints SQL statements executed)
engine = create_engine(DATABASE_URL, echo=True)

# Session factory for DB transactions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for ORM models
Base = declarative_base()

# Department table
class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    # One-to-many relationship with Employee
    employees = relationship("Employee", back_populates='department')

# Employee table
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    # Many-to-one relationship with Department
    department = relationship('Department', back_populates='employees')

print("Creating tables...")
Base.metadata.create_all(engine)   # Creates tables if not exist
print("Tables created successfully")

# ---------------- CRUD Functions ---------------- #

def create_department(name):
    """Create a new department"""
    db = SessionLocal()
    try:
        dept = Department(name=name)
        db.add(dept)
        db.commit()
        db.refresh(dept)
        print("Department created:", dept.name)
        return dept
    except Exception as e:
        db.rollback()
        print("Exception:", e)
    finally:
        db.close()
        
def create_employee(name, department_id):
    """Create a new employee under a department"""
    db = SessionLocal()
    try:
        emp = Employee(name=name, department_id=department_id)
        db.add(emp)
        db.commit()
        db.refresh(emp)
        print("Employee created:", emp.name)
        return emp
    except Exception as e:
        db.rollback()
        print("Exception:", e)
    finally:
        db.close()
        

def get_all_employees():
    """Fetch all employees"""
    db = SessionLocal()
    try:
        employees = db.query(Employee).all()
        return employees
    except Exception as e:
        print("Exception:", e)
    finally:
        db.close()
        
        
def get_employees_by_department(dept_name):
    """Fetch employees by department name"""
    db = SessionLocal()
    try:
        employees = db.query(Employee).join(Department).filter(Department.name == dept_name).all()
        return employees
    except Exception as e:
        print("Exception:", e)
    finally:
        db.close()
        
def get_department_with_employees(dept_id):
    """Fetch department and its employees"""
    db = SessionLocal()
    try:
        dept = db.query(Department).filter(Department.id == dept_id).first()
        if dept:
            return {"department": dept, "employees": dept.employees}
        return None
    except Exception as e:
        print("Exception:", e)
    finally:
        db.close()
        
        
def get_employee_with_department(emp_id):
    """Fetch employee and their department"""
    db = SessionLocal()
    try:
        emp = db.query(Employee).filter(Employee.id == emp_id).first()
        if emp:
            return {"employee": emp, "department": emp.department}
        return None
    except Exception as e:
        print("Exception:", e)
    finally:
        db.close()


# ---------------- Main Execution ---------------- #

if __name__ == "__main__":
    # Create departments
    dept1 = create_department("HR")
    dept2 = create_department("IT")

    # Create employees
    emp1 = create_employee("varsha", dept1.id)
    emp2 = create_employee("yashu", dept1.id)
    emp3 = create_employee("vinu", dept2.id)

    # Get all employees
    print("\nAll Employees:")
    employees = get_all_employees()
    for e in employees:
        print(f"Employee(id={e.id}, name={e.name}, dept_id={e.department_id})")

    # Get employees by department name
    print("\nEmployees in HR Department:")
    hr_employees = get_employees_by_department("HR")
    for e in hr_employees:
        print(f"{e.name}")

    # Get department with employees
    print("\nDepartment with Employees (IT):")
    dept_data = get_department_with_employees(dept2.id)
    print("Department:", dept_data["department"].name)
    for e in dept_data["employees"]:
        print("Employee:", e.name)

    # Get employee with department
    print("\nEmployee with Department (varsha):")
    emp_data = get_employee_with_department(emp1.id)
    print("Employee:", emp_data["employee"].name, "Department:", emp_data["department"].name)



# Output


# Creating tables...
# Tables created successfully
# Department created: HR
# Department created: IT
# Employee created: varsha
# Employee created: yashaswini
# Employee created: Charlie

# All Employees:
# Employee(id=1, name=varsha, dept_id=1)
# Employee(id=2, name=yashu, dept_id=1)
# Employee(id=3, name=vinu, dept_id=2)

# Employees in HR Department:
# Alice
# Bob

# Department with Employees (IT):
# Department: IT
# Employee: Charlie

# Employee with Department (varsha):
# Employee: Alice Department: HR
