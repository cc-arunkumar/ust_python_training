# import SQLAlchemy core and ORM modules
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "mysql+pymysql://root:password123@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    employees = relationship("Employee", back_populates="department")

    def __repr__(self):
        return f"Department(id={self.id}, name='{self.name}')"

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="employees")

    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', department_id={self.department_id})"

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

def get_all_departments():
    session = SessionLocal()
    depts = session.query(Department).all()
    session.close()
    return depts

def get_all_employees():
    session = SessionLocal()
    emps = session.query(Employee).all()
    session.close()
    return emps

def update_department(dept_id: int, new_name: str):
    session = SessionLocal()
    dept = session.query(Department).filter(Department.id == dept_id).first()
    if dept:
        dept.name = new_name
        session.commit()
        session.refresh(dept)
    session.close()
    return dept

def update_employee(emp_id: int, new_name: str = None, new_dept_id: int = None):
    session = SessionLocal()
    emp = session.query(Employee).filter(Employee.id == emp_id).first()
    if emp:
        if new_name:
            emp.name = new_name
        if new_dept_id:
            emp.department_id = new_dept_id
        session.commit()
        session.refresh(emp)
    session.close()
    return emp

def delete_department(dept_id: int):
    session = SessionLocal()
    dept = session.query(Department).filter(Department.id == dept_id).first()
    if dept:
        session.delete(dept)
        session.commit()
    session.close()
    return dept

def delete_employee(emp_id: int):
    session = SessionLocal()
    emp = session.query(Employee).filter(Employee.id == emp_id).first()
    if emp:
        session.delete(emp)
        session.commit()
    session.close()
    return emp

# fetch all employees across all departments
def fetch_all_employees():
    return get_all_employees()

# fetch employees of a specific department
def fetch_employees_by_department(dept_name: str):
    session = SessionLocal()
    emps = session.query(Employee).join(Department).filter(Department.name == dept_name).all()
    session.close()
    return emps

# fetch a department with all employees
def fetch_department_with_employees(dept_name: str):
    session = SessionLocal()
    dept = session.query(Department).filter(Department.name == dept_name).first()
    session.close()
    return dept

# fetch employee with department name
def fetch_employee_with_department():
    session = SessionLocal()
    emps = session.query(Employee, Department).join(Department).all()
    session.close()
    return emps


if __name__ == "__main__":
    print("Creating tables in MySQL DB.......")
    Base.metadata.create_all(bind=engine)
    print("Table creation completed")

    # CREATE
    hr = create_department("HR")
    it = create_department("IT")

    lucas = create_employee("Lucas", hr.id)
    maxine = create_employee("Maxine", hr.id)
    nancy = create_employee("Nancy", it.id)
    steve = create_employee("Steve", it.id)

    # READ
    print("\nDepartments:", get_all_departments())
    print("Employees:", get_all_employees())

    # UPDATE
    updated_dept = update_department(hr.id, "Human Resources")
    updated_emp = update_employee(lucas.id, new_name="Lucas Sinclair", new_dept_id=it.id)
    print("\nUpdated Department:", updated_dept)
    print("Updated Employee:", updated_emp)

    # DELETE
    deleted_emp = delete_employee(steve.id)
    deleted_dept = delete_department(it.id)
    print("\nDeleted Employee:", deleted_emp)
    print("Deleted Department:", deleted_dept)

    print("\nRemaining Departments:", get_all_departments())
    print("Remaining Employees:", get_all_employees())

    # Extra fetch examples
    print("\nAll Employees:", fetch_all_employees())
    print("Employees in IT:", fetch_employees_by_department("IT"))
    print("HR Department with employees:", fetch_department_with_employees("Human Resources"))
    print("Employees with Department info:", fetch_employee_with_department())



# o/p:
# Creating tables...
# Tables created successfully
# Department created: HR
# Department created: IT
# Employee created: Lucas
# Employee created: Maxine
# Employee created: Nancy
# Employee created: Steve

# All Employees:
# Employee(id=1, name=Lucas, dept_id=1)
# Employee(id=2, name=Maxine, dept_id=1)
# Employee(id=3, name=Nancy, dept_id=2)
# Employee(id=4, name=Steve, dept_id=2)

# Employees in HR Department:
# Lucas
# Maxine

# Department with Employees (IT):
# Department: IT
# Employee: Nancy
# Employee: Steve

# Employee with Department (Lucas):
# Employee: Lucas Department: HR
