from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base,relationship

DATABASE_URL = "mysql+pymysql://root:felix_123@localhost:3306/ust_db"

engine = create_engine(DATABASE_URL,echo=True)

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50),nullable=False)
    
    employees = relationship("Employee",back_populates="department")
    
print("Creating tables in mysql DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")

class Employee(Base):
    __tablename__ = "employees1"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50),nullable=False)
    
    department_id = Column(Integer,ForeignKey("departments.id"))
    
    department = relationship("Department",back_populates="employees")

print("Creating tables in mysql DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")
    
def create_department(name:str):
    try:
        session = SessionLocal()
        
        new_department = Department(name=name)
        
        session.add(new_department)
        
        session.commit()
        
        session.refresh(new_department)
        print("new department created")
    except Exception as e:
        session.rollback()
        print("ERROR: ,",e)
        return None
    finally:
        print("Completed")
    session.close()
    return new_department

def create_employee(name:str,department_id:int):
    try:
        session = SessionLocal()
        
        new_employee = Employee(name=name,department_id=department_id)
        
        session.add(new_employee)
        
        session.commit()
        
        session.refresh(new_employee)
    except Exception as e:
        session.rollback()
        print("ERROR: ,",e)
        return None
    finally:
        print("Completed")
    session.close()
    return new_employee


def get_all_employees():
    try:
        session = SessionLocal()
        
        employees = session.query(Employee).all()
        
        session.close()
        
        
        for emp in employees:
            print(f"ID: {emp.id} | Name: {emp.name} | Department ID: {emp.department_id}")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
def get_employee_by_id(emp_id:int):
    try:
        session = SessionLocal()
        
        emp = session.query(Employee).filter(Employee.id == emp_id).first()
        
        print(f"ID: {emp.id} | Name: {emp.name} | Department ID: {emp.department_id}")
        
        session.close()
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
def get_employee_by_dep_name(dep_name:str):
    try:
        session = SessionLocal()
        
        emps = session.query(Employee).all()
        dep = session.query(Department).all()
        for i in dep:
            if i.name == dep_name:
                dep_id = i.id
        
        for emp in emps:
            if emp.department_id == dep_id:
                print(f"ID: {emp.id} | Name: {emp.name} | Department : {dep_name}")
        
        session.close()
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        

        
        
        
if __name__ =="__main__":
    # create_department("IT service")
    # create_department("HR")
    # create_employee("Felix",1)
    # create_employee("Arun",1)
    # create_employee("Akhil",2)
    # create_employee("Arjun",2)
    # get_all_employees()
    # get_employee_by_id(1)
    get_employee_by_dep_name("HR")
    