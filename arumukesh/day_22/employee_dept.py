from sqlalchemy import create_engine,Integer,String,Column,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base,relationship



database_url = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

engine=create_engine(database_url,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)


Base=declarative_base()

class Department(Base):
    __tablename__="departments"
    
    id=Column(Integer,nullable=False,primary_key=True,index=True)
    name=Column(String(50),nullable=False)
    
    employees=relationship("Employee",back_populates="departments")
    
class Employee(Base):
    __tablename__="employees"
    
    id=Column(Integer,primary_key=True,index=True,unique=True)
    name=Column(String(50),nullable=False)
    dept_id=Column(Integer,ForeignKey("departments.id"))
    
    departments=relationship("Department",back_populates="employees")
    
    def __repr__(self):
        return f"<Employee id={self.id}, name='{self.name}', dept_id={self.dept_id}>"
 

print("creating tables")
Base.metadata.create_all(bind=engine)
print("table created ")

def create_dept(name:str):
    session=SessionLocal()
    dept=Department(name=name)
    session.add(dept)
    session.commit()
    session.refresh(dept)
    session.close()
    return dept
def create_emp(name:str,dept_id:int):
    session=SessionLocal()
    emp=Employee(name=name,dept_id=dept_id)
    session.add(emp)
    session.commit()
    session.refresh(emp)
    session.close()
    
       
    return emp


# create_dept("IT")
# create_dept("HR")
# def get_all_emp():
create_emp("arumuekesh",2)
create_emp("Arun",1)
def get_all_emp():
    session=SessionLocal()
    emps=session.query(Employee).all()
    return emps
    # session.
    
print(get_all_emp())
    
    