from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base,relationship

DATABASEURL = 'mysql+pymysql://root:password123@localhost:3306/ust_db'
engine = create_engine(DATABASEURL,echo=True)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit = False)
Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50),nullable=False)
    
    employees = relationship("Employee",back_populates='department')
    
class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer,primary_key=True,index=False)
    name = Column(String(50),nullable=False)
    
    department_id = Column(Integer,ForeignKey('departments.id'))
    
    department = relationship('Department',back_populates='employees')
    
Base.metadata.create_all(bind=engine)
def create_department(name:str):
    session = SessionLocal()
    department = Department(name = name)
    session.add(department)
    session.commit()
    session.refresh(department)
    session.close()
    
    return department

def create_employee(name:str,department_id : int):
    session = SessionLocal()
    emp = Employee(name = name, department_id=department_id)
    session.add(emp)
    session.commit()
    session.refresh(emp)
    session.close()
    
    return emp 


def get_all_emp():
    session = SessionLocal()
    data = session.query(Employee).all()
    session.close()
    return data 

def get_emp_by_id(id:int):
    session = SessionLocal()
    data = session.query(Employee).filter(Employee.id == id).first()
    session.close()
    return data 

def get_all_emp_by_dept(dpt_id:int):
    session = SessionLocal()
    data = session.query(Employee).filter(Employee.department_id == dpt_id).all()
    
    session.close()
    
    return data 

def get_emp_by_dept_name(name:str):
    session = SessionLocal()
    data_id = session.query(Department).filter(Department.name == name).first()
    if data_id is None:
        session.close()
        return []
    data = session.query(Employee).filter(Employee.department_id == data_id.id).all()
    session.close()
    return data

if __name__ == '__main__':
    emps = get_emp_by_dept_name("HR")
    for i in emps:
        print(i.id, i.name, i.department_id)
        
        
# d1 = create_department('HR')
# d2 = create_department('Engineering')
# d3 = create_department('Sales')

# # create employees
# e1 = create_employee('Anjan', d1.id)
# e2 = create_employee('Ganesh', d2.id)
# e3 = create_employee('Carlos', d3.id)
# print('Employees created:', e1.id, e2.id, e3.id)  

# emps = get_all_emp_by_dept(4)
# for i in emps:
#     print(i.id,i.name,i.department_id)