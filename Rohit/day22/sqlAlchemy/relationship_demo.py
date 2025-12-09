from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_training_db"
engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    # Relationship to Employee 
    employees = relationship("Employee", back_populates="department")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")



Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)


def create_department(name: str):
    session = SessionLocal()
    try:
        depart = Department(name=name)
        session.add(depart)
        session.commit()
        session.refresh(depart)
        return depart
    except Exception as e:
        session.rollback()
        print("Error:", e)
    finally:
        session.close()


def create_employee(name: str, department_id: int):
    session = SessionLocal()
    try:
        employe = Employee(name=name, department_id=department_id)
        session.add(employe)
        session.commit()
        session.refresh(employe)
        return employe
    except Exception as e:
        session.rollback()
        print("Error:", e)
    finally:
        session.close()


def fetch_all_employees():
    session = SessionLocal()
    try:
        rows = session.query(Employee).all()
        for row in rows:
            print(
                f"ID={row.id}, Name={row.name}, DepartmentID={row.department_id}, DepartmentName={row.department.name}"
            )
        return rows
    finally:
        session.close()
def fetch_employees_by_department(department_id: int):
    session = SessionLocal()
    try:
        employees = session.query(Employee).filter(Employee.department_id == department_id).all()
        return employees
    finally:
        session.close()


def fetch_department_with_employees(department_id: int):
    session = SessionLocal()
    try:
        department = session.query(Department).filter(Department.id == department_id).first()
        if department:
            print("data",department.employees.e.id)
           
            return {
                "id": department.id,
                "name": department.name,
                "employees": [{"id": e.id, "name": e.name} for e in department.employees]
            }
        return None
    finally:
        session.close()


def fetch_employee_with_department(employee_id: int):
    session = SessionLocal()
    try:
        employee = session.query(Employee).filter(Employee.id == employee_id).first()
        if employee:
            return {
                "id": employee.id,
                "name": employee.name,
                "department_id": employee.department_id,
                "department_name": employee.department.name if employee.department else None
            }
        return None
    finally:
        session.close()

if __name__ == "__main__":
    # d1 = create_department("HR")
    # d2 = create_department("IT")
    # d3 = create_department("Finance")

    # print("Departments created:", d1.id, d2.id, d3.id)

    # # Create employees
    # e1 = create_employee("Alice", d1.id)
    # e2 = create_employee("Bob", d2.id)
    # e3 = create_employee("Charlie", d2.id)
    # e4 = create_employee("Diana", d3.id)
    # e5 = create_employee("Ethan", d1.id)

    # print("Employees created:", e1.id, e2.id, e3.id, e4.id, e5.id)
    fetch_all_employees()
    employees_it = fetch_employees_by_department(2)
    print("IT Department Employees:", [(e.id, e.name) for e in employees_it])

    dept_hr = fetch_department_with_employees(1)
    print("HR Department:", dept_hr)

    emp = fetch_employee_with_department(3)
    print("Employee with Department:", emp)

