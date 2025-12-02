from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Correct DATABASE_URL
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/ust_db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

# Session local for managing the DB session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    employees = relationship("Employee", back_populates='department')  

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    department = relationship('Department', back_populates="employees") 

Base.metadata.create_all(bind=engine)

def create_department(name: str):
    try:
        session = SessionLocal()  
        
        department = Department(name=name)
        
        session.add(department)
        session.commit()
        
        session.refresh(department)
        
    except Exception as e:
        session.rollback()
        print("Exception: ", e)  
        return None
    
    finally:
        session.close()
    
    return department

def create_employee(name: str, department_id: int):
    try:
        session = SessionLocal()  
        
        employee = Employee(name=name, department_id=department_id) 
        
        session.add(employee)
        session.commit()
        
        session.refresh(employee)
        
    except Exception as e:
        session.rollback()
        print("Exception: ", e)  
        return None
    
    finally:
        session.close()
    
    return employee

def fetch_all_employees():
    try:
        session = SessionLocal()
        employees = session.query(Employee).all()  
    except Exception as e:
        print("Exception: ", e)
        return None
    finally:
        session.close()
    
    return employees

def fetch_employees_by_department(department_name: str):
    try:
        session = SessionLocal()
        # Fetch employees by department name
        department = session.query(Department).filter(Department.name == department_name).first()
        if department:
            employees = department.employees  
        else:
            employees = []
    except Exception as e:
        print("Exception: ", e)
        return None
    finally:
        session.close()
    
    return employees

def fetch_department_with_employees(department_name: str):
    try:
        session = SessionLocal()
        department = session.query(Department).filter(Department.name == department_name).first()
    except Exception as e:
        print("Exception: ", e)
        return None
    finally:
        session.close()
    
    return department

def fetch_employees_with_department():
    try:
        session = SessionLocal()
        employees = session.query(Employee, Department.name).join(Department).all()
    except Exception as e:
        print("Exception: ", e)
        return None
    finally:
        session.close()
    
    return employees

# def insert_sample_data():
#     # Create some departments
#     it_department = create_department("IT")
#     hr_department = create_department("HR")
#     finance_department = create_department("Finance")
    
#     # Create some employees
#     create_employee("Abhi", it_department.id)
#     create_employee("Vicky", it_department.id)
#     create_employee("Shaki", hr_department.id)
#     create_employee("Niru", finance_department.id)
#     create_employee("vamsi", it_department.id)

# Call the insert_sample_data to add random data
# insert_sample_data()

#  calls to fetch functions
all_employees = fetch_all_employees()
it_employees = fetch_employees_by_department("IT")
it_department_with_employees = fetch_department_with_employees("IT")
employees_with_departments = fetch_employees_with_department()

# Print results for checking
print("All Employees:", all_employees)
print("IT Department Employees:", it_employees)
print("IT Department with Employees:", it_department_with_employees)
print("Employees with Department Names:", employees_with_departments)