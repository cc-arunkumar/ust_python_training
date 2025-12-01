from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base,relationship

DATABASE_URL = "mysql+pymysql://root:password123@localhost:3306/ust_db"

engine = create_engine(DATABASE_URL)
sessionlocal = sessionmaker(bind=engine,autoflush=False,autocommit = False)
Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True,index = True)
    name = Column(String(50))
    
    employees = relationship("Employees",back_populates="department")

class Employees(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True,index = True)
    name = Column(String(50))
    
    department_id = Column(Integer,ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")
    
print("Creating tables...")
Base.metadata.create_all(engine)
print("Tables create successfully.")

def create_dept(name:str):
    try:
        session = sessionlocal()
        new_dept = Department(name = name)
        
        session.add(new_dept)
        session.commit()
        session.refresh(new_dept)
        return new_dept
    except Exception as e:
        session.rollback()
        print(e)
        return None
    finally:
        session.close()

def create_emp(name:str,department_id : int):
    try:
        session = sessionlocal()
        new_emp = Employees(name=name,department_id=department_id)
        session.add(new_emp)
        session.commit()
        session.refresh(new_emp)
        return new_emp
    except Exception as e:
        session.rollback()
        print(e)
        return None
    finally:
        session.close()
        
        
def get_all():
    try:
        session = sessionlocal()
        data = session.query(Employees).all()
        for each in data:
            print(each.__dict__)
    except Exception as e:
        session.rollback()
        print(e)
        return None
    finally:
        session.close()
    
def emp_specific_dept():
    try:
        session = sessionlocal()
        data = session.query(Employees).join(Department).where(Department.name == "HR").all()
        if not data:
            print("No data found")
            return None
        for each in data:
            print(each.__dict__)
    except Exception as e:
        session.rollback()
        print(e)
        return None
    finally:
        session.close()
        
def emp_with_dept():
    try:
        session = sessionlocal()
        data = session.query(Employees.name,Department.name).join(Department,Department.id == Employees.department_id).all()
        if not data:
            print("No data found")
            return None
        for each,dept in data:
            print(each,dept)
    except Exception as e:
        session.rollback()
        print(e)
        return None
    finally:
        session.close()
        
        
        
# print(create_dept("HR"))  
# print(create_emp("Arjun",2))

# get_all()
# emp_specific_dept()
emp_with_dept()