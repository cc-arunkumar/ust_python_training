from sqlalchemy import create_engine,Column,Integer,String,ForeignKey

from sqlalchemy.orm import sessionmaker,declarative_base,relationship

DATABASE_URL="mysql+pymysql://root:pass%40word1@localhost:3306/ust_asset_db"

engine = create_engine(DATABASE_URL,echo=True)

SessionLocal= sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()

class Department(Base):
    __tablename__="department"
    
    id = Column(Integer, primary_key=True,index=True)
    
    name= Column(String(50))
    
    employees=relationship("Employee", back_populates="department")
    
class Employee(Base):
    __tablename__="employees"
    
    id = Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    department_id = Column(Integer, ForeignKey("department.id"))  
    
    department= relationship("Department", back_populates="employees")
    
print("Creating tables...")
Base.metadata.create_all(engine)
print("Table created")

def create_department(name:str):
    session=SessionLocal()
    
    dept=Department(name=name)
    
    session.add(dept)
    session.commit()
    session.refresh(dept)
    session.close()
    return dept
    

def create_employee(name:str,department_id:int):
    session=SessionLocal()
    
    emp = Employee(name=name, department_id=department_id)
    
    session.add(emp)
    session.commit()
    session.refresh(emp)
    session.close()
    return emp

dept = create_department("IT")

new_emp = create_employee("sohan", 12)

print("Employee created:")
print("ID:", new_emp.id)
print("Name:", new_emp.name)
print("Department ID:", new_emp.department_id)


def get_all_employees():
    session = SessionLocal()
    employees = session.query(Employee).all()
    session.close()
    return employees

def get_employees_by_department(dept_id: int):
    session = SessionLocal()
    employees = session.query(Employee).filter(Employee.department_id == dept_id).all()
    session.close()
    return employees

def get_department_with_employees(dept_id: int):
    session = SessionLocal()
    dept = session.query(Department).filter(Department.id == dept_id).first()
    session.close()
    return dept   

def get_employee_with_department(emp_id: int):
    session = SessionLocal()
    emp = session.query(Employee).filter(Employee.id == emp_id).first()
    session.close()
    return emp

    

    