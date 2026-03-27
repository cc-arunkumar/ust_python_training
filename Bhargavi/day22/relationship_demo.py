# This script defines two models, Department and Employee, and manages their relationships
# using SQLAlchemy. It includes functions to create departments, create employees, and 
# retrieve employees by department or individual employee details. 
# The script uses a MySQL database to store and query these entities.

# Import necessary libraries from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Database URL configuration (MySQL connection details)
DATABASE_URL = "mysql+pymysql://root:bhargavi_123@localhost:3306/ust_db"
# Create engine to connect to the database with SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Session configuration for SQLAlchemy ORM
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Declare the base class for the ORM models
Base = declarative_base()

# Department model representing departments table in the database
class Department(Base):
    __tablename__ = "departments"
     
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    # Establish relationship with the Employee model
    employees = relationship("Employee", back_populates="department")
    
    def __repr__(self):
        return f"Department(id={self.id}, name='{self.name}')"


# Employee model representing employees table in the database
class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    department_id = Column(Integer, ForeignKey("departments.id"))  # Foreign key to the department table
    
    # Establish relationship with the Department model
    department = relationship("Department", back_populates="employees")
    
    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', department_id={self.department_id})"

# Create tables for the models in the database
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully")

# Function to create a department in the database
def create_department(name: str):
    try:
        session = SessionLocal()  # Open a session
        new_department = Department(name=name)  # Create a new department object
        session.add(new_department)  # Add department to the session
        session.commit()  # Commit transaction to the database
        session.refresh(new_department)  # Refresh the object to get updated values
        return new_department
    except Exception as e:
        session.rollback()  # Rollback in case of an error
        print("Error creating department:", e)
    finally:
        session.close()  # Close the session

# Function to create an employee in the database
def create_employee(name: str, department_id: int):
    try:
        session = SessionLocal()  # Open a session
        new_employee = Employee(name=name, department_id=department_id)  # Create a new employee object
        session.add(new_employee)  # Add employee to the session
        session.commit()  # Commit transaction to the database
        session.refresh(new_employee)  # Refresh the object to get updated values
        return new_employee
    except Exception as e:
        session.rollback()  # Rollback in case of an error
        print("Error creating employee:", e)
    finally:
        session.close()  # Close the session

# Function to fetch all employees from the database
def fetch_all_employees():
    try:
        session = SessionLocal()  # Open a session
        employees = session.query(Employee).all()  # Query all employees
        return employees
    except Exception as e:
        session.rollback()  # Rollback in case of an error
        print("error in fetch", e)
    finally:
        session.close()  # Close the session

# Function to fetch employees by department name
def fetch_employees_by_department(department_id: int):
    try:
        session = SessionLocal()  # Open a session
        # Fetch employees by their department_id
        employees = session.query(Employee).filter(Employee.department_id == department_id).all()
        return employees
    except Exception as e:
        print(f"Error fetching employees from department ID {department_id}:", e)
    finally:
        session.close()  # Close the session


# Function to fetch a department and its employees by department ID
def fetch_department_with_employees(department_id: int):
    try:
        session = SessionLocal()  # Open a session
        department = session.query(Department).filter(Department.id == department_id).first()  # Query department by ID
        if department:
            return department, department.employees  # Return department and its employees
        else:
            print(f"No department found with id {department_id}")
            return None
    except Exception as e:
        print("Error fetching department with employees:", e)
    finally:
        session.close()  # Close the session

# Function to fetch an employee with their department by employee ID
def fetch_employee_with_department(employee_id: int):
    try:
        session = SessionLocal()  # Open a session
        employee = session.query(Employee).filter(Employee.id == employee_id).first()  # Query employee by ID
        if employee:
            return employee, employee.department.name if employee.department else None  # Return employee and department name
        else:
            print(f"No employee found with id {employee_id}")
            return None
    except Exception as e:
        print("Error fetching employee with department:", e)
    finally:
        session.close()  # Close the session


if __name__ == "__main__":
    # Create IT and HR departments
    it_department = create_department('IT')
    hr_department = create_department('HR')
    
    # Add employees to departments
    create_employee('Bhargavi', it_department.id)
    create_employee('Meena', it_department.id)
    create_employee('Veena', hr_department.id)

    # Fetch and display all employees
    all_employees = fetch_all_employees()
    print("All Employees:", all_employees)

    # Fetch employees in IT department
    it_employees = fetch_employees_by_department('IT')
    print("Employees in IT Department:", it_employees)

    # Fetch department and employees by department ID
    dept, employees_in_dept = fetch_department_with_employees(it_department.id)
    if dept:
        print(f"Department {dept.name} with employees:", employees_in_dept)

    # Fetch an employee with their department by employee ID
    employee, department_name = fetch_employee_with_department(1)
    if employee:
        print(f"Employee {employee.name} is in {department_name} department")

#output
# Creating tables...
# Tables created successfully
# All Employees: [Employee(id=1, name='Bhargavi', department_id=1), Employee(id=2, name='Meena', department_id=1), Employee(id=3, name='Veena', department_id=2), Employee(id=4, name='Bhargavi', department_id=3), Employee(id=5, name='Meena', department_id=3), Employee(id=6, name='Veena', department_id=4), Employee(id=7, name='Bhargavi', department_id=5), Employee(id=8, name='Meena', department_id=5), Employee(id=9, name='Veena', department_id=6), Employee(id=10, name='Bhargavi', department_id=7), Employee(id=11, name='Meena', department_id=7), Employee(id=12, name='Veena', department_id=8), Employee(id=13, name='Bhargavi', department_id=9), Employee(id=14, name='Meena', department_id=9), Employee(id=15, name='Veena', department_id=10), Employee(id=16, name='Bhargavi', department_id=11), Employee(id=17, name='Meena', department_id=11), Employee(id=18, name='Veena', department_id=12)]
# Employees in IT Department: [Employee(id=1, name='Bhargavi', department_id=1), Employee(id=2, name='Meena', department_id=1)]
# Department IT with employees: [Employee(id=13, name='Bhargavi', department_id=9), Employee(id=14, name='Meena', department_id=9)]
# Employee Bhargavi is in IT department