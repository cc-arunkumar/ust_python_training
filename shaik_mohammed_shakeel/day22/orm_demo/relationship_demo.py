# Importing necessary components from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Database URL for connecting to the MySQL database
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/ust_db"

# Create the engine that will manage connections to the database
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal is a factory for creating new session objects that interact with the database
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for defining ORM models
Base = declarative_base()

# Department model represents a department in the company
class Department(Base):
    __tablename__ = "departments"  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the department
    name = Column(String(50), nullable=False)  # Department name (non-nullable)
    
    # One-to-many relationship: a department can have multiple employees
    employees = relationship("Employee", back_populates="department")  # Bidirectional relationship

# Employee model represents an employee in the company
class Employee(Base):
    __tablename__ = "employees"  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the employee
    name = Column(String(50), nullable=False)  # Employee name (non-nullable)
    
    # Foreign key referencing the department this employee belongs to
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    # Many-to-one relationship: each employee belongs to one department
    department = relationship("Department", back_populates="employees")

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Function to create a new department in the database
def create_department(name: str):
    try:
        session = SessionLocal()
        
        # Create a new department object
        department = Department(name=name)
        
        # Add the department to the session and commit it to the database
        session.add(department)
        session.commit()
        
        # Refresh the department object to get the updated fields (e.g., id)
        session.refresh(department)
    
    except Exception as e:
        # If any exception occurs, rollback the session and print the error
        session.rollback()
        print("Exception: ", e)
        return None
    
    finally:
        # Close the session after the operation
        session.close()
    
    return department

# Function to create a new employee and assign them to a department
def create_employee(name: str, department_id: int):
    try:
        session = SessionLocal()
        
        # Create a new employee object with the given department_id
        employee = Employee(name=name, department_id=department_id)
        
        # Add the employee to the session and commit the transaction
        session.add(employee)
        session.commit()
        
        # Refresh the employee object to get the updated fields (e.g., id)
        session.refresh(employee)
    
    except Exception as e:
        # If any exception occurs, rollback the session and print the error
        session.rollback()
        print("Exception: ", e)
        return None
    
    finally:
        # Close the session after the operation
        session.close()
    
    return employee

# Function to fetch all employees from the database
def fetch_all_employees():
    try:
        session = SessionLocal()
        
        # Query all employees from the database
        employees = session.query(Employee).all()
    
    except Exception as e:
        # If any exception occurs, print the error
        print("Exception: ", e)
        return None
    
    finally:
        # Close the session after the operation
        session.close()
    
    return employees

# Function to fetch employees of a specific department by its name
def fetch_employees_by_department(department_name: str):
    try:
        session = SessionLocal()
        
        # Query the department by name
        department = session.query(Department).filter(Department.name == department_name).first()
        
        if department:
            # If the department is found, retrieve its employees
            employees = department.employees
        else:
            # If no department is found, return an empty list
            employees = []
    
    except Exception as e:
        # If any exception occurs, print the error
        print("Exception: ", e)
        return None
    
    finally:
        # Close the session after the operation
        session.close()
    
    return employees

# Function to fetch the department with its employees using department name
def fetch_department_with_employees(department_name: str):
    try:
        session = SessionLocal()
        
        # Query the department by name
        department = session.query(Department).filter(Department.name == department_name).first()
    
    except Exception as e:
        # If any exception occurs, print the error
        print("Exception: ", e)
        return None
    
    finally:
        # Close the session after the operation
        session.close()
    
    return department

# Function to fetch employees along with their department names
def fetch_employees_with_department():
    try:
        session = SessionLocal()
        
        # Query employees along with the department name by joining the two tables
        employees = session.query(Employee, Department.name).join(Department).all()
    
    except Exception as e:
        # If any exception occurs, print the error
        print("Exception: ", e)
        return None
    
    finally:
        # Close the session after the operation
        session.close()
    
    return employees

# Function to insert some sample data into the database
def insert_sample_data():
    # Create some departments
    it_department = create_department("IT")
    hr_department = create_department("HR")
    finance_department = create_department("Finance")
    
    # Create some employees and assign them to departments
    create_employee("Shakeel", it_department.id)
    create_employee("sai", it_department.id)
    create_employee("abhi", hr_department.id)
    create_employee("vikas", finance_department.id)
    create_employee("yashwanth", it_department.id)

# Insert the sample data
insert_sample_data()

# Fetch and display different sets of employees and departments
all_employees = fetch_all_employees()
it_employees = fetch_employees_by_department("IT")
it_department_with_employees = fetch_department_with_employees("IT")
employees_with_departments = fetch_employees_with_department()

# Printing out the results
print("All Employees:", all_employees)
print("IT Department Employees:", it_employees)
print("IT Department with Employees:", it_department_with_employees)
print("Employees with Department Names:", employees_with_departments)
