from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base,Relationship


D_B = "mysql+pymysql://root:password123@localhost:3306/new_db"
engine = create_engine(D_B,echo=True)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base= declarative_base()

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50),nullable=False)

    employees = Relationship("Employee",back_populates="departments")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50),nullable=False)

    department_id = Column(Integer,ForeignKey("departments.id"))

    departments = Relationship("Department",back_populates="employees")

print("Creating Table in Mysql")
Base.metadata.create_all(bind=engine)
print("Completed Creating")

def create_dep(name:str):
    try:
        session = SessionLocal()
        new_dep = Department(name=name)

        session.add(new_dep)

        session.commit()

        session.refresh(new_dep)

        return new_dep
    
    except Exception as e:
        session.rollback()
        print(str(e))
    
    finally:
        session.close()


def create_emp(name:str,dep_id=int):
    try:
        session = SessionLocal()
        new_emp = Employee(name=name,department_id=dep_id)

        session.add(new_emp)

        session.commit()

        session.refresh(new_emp)

        return new_emp
    
    except Exception as e:
        session.rollback()
        print(str(e))
    
    finally:
        session.close()

# dep = create_dep("HR")

# emp = create_emp("Arjun",dep.id)
# emp2 = create_emp("Rahul",dep.id)


def get_all():
    try:
        session = SessionLocal()
        emp = session.query(Employee).all()
        for da in emp:
            print(da.__dict__)
        dep = session.query(Employee).join(Department).where(Department.name=="IT").all()
        for da in dep:
            print(da.__dict__)
        data = session.query(Employee.name,Department.name).join(Department,Department.id==Employee.department_id).all()
        for da in data:
            print(da)

        
    
    except Exception as e:
        session.rollback()
        print(str(e))
    
    finally:
        session.close()


get_all()