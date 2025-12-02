from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "mysql+pymysql://root:12345@localhost:3306/ust_db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")


Base.metadata.create_all(bind=engine)

def create_department(name: str):
    session = SessionLocal()
    dept = Department(name=name)
    session.add(dept)
    session.commit()
    session.refresh(dept)
    session.close()
    return dept

def create_employee(name: str, department_id: int):
    session = SessionLocal()
    emp = Employee(name=name, department_id=department_id)
    session.add(emp)
    session.commit()
    session.refresh(emp)
    session.close()
    return emp

if __name__ == "__main__":
    dept = create_department("HR")
    create_employee("Niranjan", dept.id)
    
def get_all_employees():
    session = SessionLocal()
    employees = session.query(Employee).all()
    session.close()
    return employees

def get_employees_by_department(department_id: int):
    session = SessionLocal()
    employees = session.query(Employee).filter(Employee.department_id == department_id).all()
    session.close()
    return employees

def get_department_with_employees(department_id: int):
    session = SessionLocal()
    department = session.query(Department).filter(Department.id == department_id).first()
    session.close()
    return department

def get_employees_with_department():
    session = SessionLocal()
    results = (
        session.query(Employee.id, Employee.name, Department.name.label("department_name")).join(Department, Employee.department_id == Department.id).all())
    session.close()
    return results

# all_emps = get_all_employees()
# print("\nAll Employees:")
# for emp in all_emps:
#     print(f"{emp.id} - {emp.name} (Dept ID: {emp.department_id})")


# it_emps = get_employees_by_department(dept.id)
# print("\nEmployees in IT Department:")
# for emp in it_emps:
#     print(f"{emp.id} - {emp.name}")

   
# dept = get_department_with_employees(dept.id)
# print(f"\nDepartment: {dept.name}")
# for emp in dept.employees:
#     print(f"{emp.id} - {emp.name}")

if __name__ == "__main__":
    employees_with_dept = get_employees_with_department()
    print("\nEmployees with Department Names:")
    for emp_id, emp_name, dept_name in employees_with_dept:
        print(f"{emp_id} - {emp_name} (Department: {dept_name})")
        
        
        
        
