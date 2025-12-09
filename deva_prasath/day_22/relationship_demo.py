
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=True, autocommit=False)

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    employees = relationship("Employee", back_populates="department")

    def __repr__(self):
        return f"Department(id={self.id}, name={self.name})"

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")

    def __repr__(self):
        return f"Employee(id={self.id}, name={self.name}, department_id={self.department_id})"



def create_employee(name: str, department_id: int):
    with SessionLocal() as session:
        try:
            emp = Employee(name=name, department_id=department_id)
            session.add(emp)
            session.commit()
            session.refresh(emp)
            return emp
        except Exception as e:
            session.rollback()
            print("Exception in create_employee:", e)
            return None


def create_dept(name: str):
    with SessionLocal() as session:
        try:
            dep = Department(name=name)
            session.add(dep)
            session.commit()
            session.refresh(dep)
            return dep
        except Exception as e:
            session.rollback()
            print("Exception in create_dept:", e)
            return None


def fetch_emp():
    with SessionLocal() as session:
        try:
            emp_list = session.query(Employee).all()
            return emp_list
        except Exception as e:
            print("Exception in fetch_emp:", e)
            return None


def fet_emp_by_dep(department_id: int):
    with SessionLocal() as session:
        try:
            empdep = session.query(Employee).filter(Employee.department_id == department_id).first()
            return empdep
        except Exception as e:
            print("Exception in fet_emp_by_dep:", e)
            return None


def fetch_dep(department_id: int):
    with SessionLocal() as session:
        try:
            dep_emp = session.query(Employee).filter(Employee.department_id == department_id).all()
            return dep_emp
        except Exception as e:
            print("Exception in fetch_dep:", e)
            return None


if __name__ == "__main__":
    # create_employee("Deva", 1)

    all_emps = fetch_emp()
    print("All employees:", all_emps)            

    emp_from_dep = fet_emp_by_dep(2)
    print("First employee in department 2:", emp_from_dep)

    emps_in_dep = fetch_dep(2)
    print("All employees in department 2:")
    for e in emps_in_dep:
        print(" -", e.id, e.name, e.department_id)
