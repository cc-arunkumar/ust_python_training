from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship,declarative_base,sessionmaker

DATABASE_URL="mysql+pymysql://root:password123@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()

class Department(Base):
    __tablename__="departments"
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50),nullable=False)
    
    employees=relationship("Employee",back_populates="departments")
    
class Employee(Base):
    __tablename__="employeees"
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50),nullable=False)
    department_id=Column(Integer,ForeignKey("departments.id"))
    
    departments=relationship("Department",back_populates="employees")
    
Base.metadata.create_all(bind=engine)

def create_department(name:str):
    try:
        session=SessionLocal()
        dep=Department(name=name)
        session.add(dep)
        session.commit()
        session.refresh(dep)
        return dep
    except Exception as e:
        print("Exception: ",e)
        return None
    finally:
        session.close()
        
def create_employee(name:str,dep_id:int):
    try:
        session=SessionLocal()
        emp=Employee(name=name,department_id=dep_id)
        session.add(emp)
        session.commit()
        session.refresh(emp)
        return emp
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()
        
def get_all_employees():
    try:
        session=SessionLocal()
        data=session.query(Employee).all()
        return data
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()
        
def get_all_employees_by_dep_id(id:int):
    try:
        session=SessionLocal()
        data=session.query(Employee).filter(Employee.department_id==id).all()
        return data
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()

def get_department_all_employees(name:str):
    try:
        session=SessionLocal()
        data=session.query(Department).filter(Department.name==name).first()
        return data.employees
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()

def get_employee_by_department_name(name:str):
    try:
        session=SessionLocal()
        id_dep=session.query(Department).filter(Department.name==name).first()
        data=session.query(Employee).filter(Employee.department_id==id_dep.id).all()
        return data
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()
        
        
        
if __name__=="__main__":
    # dep=create_department("IT")
    # print(dep)
    
    # emp1=create_employee("shyam",dep.id)
    # emp2=create_employee("ram",dep.id)
    # print(emp1.id,emp1.name,emp1.department_id)
    # print(emp2.id,emp2.name,emp2.department_id)

    # data=get_all_employees()
    # for row in data:
    #     print(row.id,row.name,row.department_id)
    
    # data=get_all_employees_by_dep_id(1)
    # for row in data:
    #     print(row.id,row.name,row.department_id)
    
    # data=get_employee_by_department_name("IT")
    # if data:
    #     for row in data:
    #         print(row.id,row.name,row.department_id)
    
    data=get_department_all_employees("IT")
    for row in data:
        print(row.id,row.name,row.department_id)
    