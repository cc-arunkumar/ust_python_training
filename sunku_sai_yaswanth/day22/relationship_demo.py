from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
 
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/ust_db"
 
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

# Insert new department record
def create_department(name:str):
    try:
        session=SessionLocal()
        dep=Department(name=name)
        session.add(dep)        # Insert object into session
        session.commit()        # Save to database
        session.refresh(dep)    # Refresh to get updated data (id)
        return dep
    except Exception as e:
        print("Exception: ",e)
        return None
    finally:
        session.close()

# Insert new employee record
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

# Fetch all employees
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

# Fetch employees by department ID
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

# Fetch employees using relationship by department name
def get_department_all_employees(name:str):
    try:
        session=SessionLocal()
        data=session.query(Department).filter(Department.name==name).first()
        return data.employees  # returns list of Employee objects
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()

# Fetch employees by department name using join-like logic manually
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
    dep1=create_department("IT")
    dep2=create_department("HR")# Create department example
    print(dep1,dep2)

    # Create employees
    emp1=create_employee("sai",dep1.id)
    emp2=create_employee("yaswanth",dep1.id)
    emp3=create_employee("vamshi",dep2.id)
    print(emp1.id,emp1.name,emp1.department_id)
    
    # Get all employees
    data=get_all_employees()
    for row in data:
        print(row.id,row.name,row.department_id)

    # Get employees by dept id
    data=get_all_employees_by_dep_id(1)
    for row in data:
        print(row.id,row.name,row.department_id)

    # Get employees by department name using manual filter
    data=get_employee_by_department_name("IT")
    if data:
        for row in data:
            print(row.id,row.name,row.department_id)

    # Get employees using relationship
    data=get_department_all_employees("IT")
    if data:
        for row in data:
            print(row.id,row.name,row.department_id)
    else:
        print("No employees found or department does not exist")
 
 
#  2025-12-02 09:39:21,660 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2025-12-02 09:39:21,660 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-02 09:39:21,662 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2025-12-02 09:39:21,662 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-02 09:39:21,662 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2025-12-02 09:39:21,662 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-02 09:39:21,664 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,664 INFO sqlalchemy.engine.Engine DESCRIBE `ust_db`.`departments`
# 2025-12-02 09:39:21,664 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-02 09:39:21,668 INFO sqlalchemy.engine.Engine DESCRIBE `ust_db`.`employees`
# 2025-12-02 09:39:21,668 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-02 09:39:21,670 INFO sqlalchemy.engine.Engine 
# CREATE TABLE departments (
# 	id INTEGER NOT NULL AUTO_INCREMENT, 
# 	name VARCHAR(50) NOT NULL, 
# 	PRIMARY KEY (id)
# )


# 2025-12-02 09:39:21,670 INFO sqlalchemy.engine.Engine [no key 0.00012s] {}
# 2025-12-02 09:39:21,705 INFO sqlalchemy.engine.Engine CREATE INDEX ix_departments_id ON departments (id)
# 2025-12-02 09:39:21,705 INFO sqlalchemy.engine.Engine [no key 0.00019s] {}
# 2025-12-02 09:39:21,735 INFO sqlalchemy.engine.Engine 
# CREATE TABLE employees (
# 	id INTEGER NOT NULL AUTO_INCREMENT, 
# 	name VARCHAR(50) NOT NULL, 
# 	department_id INTEGER, 
# 	PRIMARY KEY (id), 
# 	FOREIGN KEY(department_id) REFERENCES departments (id)
# )


# 2025-12-02 09:39:21,735 INFO sqlalchemy.engine.Engine [no key 0.00017s] {}
# 2025-12-02 09:39:21,787 INFO sqlalchemy.engine.Engine CREATE INDEX ix_employees_id ON employees (id)
# 2025-12-02 09:39:21,787 INFO sqlalchemy.engine.Engine [no key 0.00021s] {}
# 2025-12-02 09:39:21,808 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-02 09:39:21,816 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,817 INFO sqlalchemy.engine.Engine INSERT INTO departments (name) VALUES (%(name)s)
# 2025-12-02 09:39:21,818 INFO sqlalchemy.engine.Engine [generated in 0.00026s] {'name': 'IT'}
# 2025-12-02 09:39:21,819 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-02 09:39:21,824 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,829 INFO sqlalchemy.engine.Engine SELECT departments.id, departments.name 
# FROM departments 
# WHERE departments.id = %(pk_1)s
# 2025-12-02 09:39:21,829 INFO sqlalchemy.engine.Engine [generated in 0.00031s] {'pk_1': 1}
# 2025-12-02 09:39:21,830 INFO sqlalchemy.engine.Engine ROLLBACK
# 2025-12-02 09:39:21,831 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,832 INFO sqlalchemy.engine.Engine INSERT INTO departments (name) VALUES (%(name)s)
# 2025-12-02 09:39:21,832 INFO sqlalchemy.engine.Engine [cached since 0.01438s ago] {'name': 'HR'}
# 2025-12-02 09:39:21,833 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-02 09:39:21,840 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,840 INFO sqlalchemy.engine.Engine SELECT departments.id, departments.name 
# FROM departments 
# WHERE departments.id = %(pk_1)s
# 2025-12-02 09:39:21,840 INFO sqlalchemy.engine.Engine [cached since 0.01175s ago] {'pk_1': 2}
# 2025-12-02 09:39:21,841 INFO sqlalchemy.engine.Engine ROLLBACK
# <__main__.Department object at 0x000001D72117F620> <__main__.Department object at 0x000001D72114BB10>
# 2025-12-02 09:39:21,842 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,843 INFO sqlalchemy.engine.Engine INSERT INTO employees (name, department_id) VALUES (%(name)s, %(department_id)s)
# 2025-12-02 09:39:21,843 INFO sqlalchemy.engine.Engine [generated in 0.00019s] {'name': 'sai', 'department_id': 1}
# 2025-12-02 09:39:21,844 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-02 09:39:21,848 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,849 INFO sqlalchemy.engine.Engine SELECT employees.id, employees.name, employees.department_id 
# FROM employees 
# WHERE employees.id = %(pk_1)s
# 2025-12-02 09:39:21,850 INFO sqlalchemy.engine.Engine [generated in 0.00018s] {'pk_1': 1}
# 2025-12-02 09:39:21,851 INFO sqlalchemy.engine.Engine ROLLBACK
# 2025-12-02 09:39:21,852 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,852 INFO sqlalchemy.engine.Engine INSERT INTO employees (name, department_id) VALUES (%(name)s, %(department_id)s)
# 2025-12-02 09:39:21,852 INFO sqlalchemy.engine.Engine [cached since 0.009509s ago] {'name': 'yaswanth', 'department_id': 1}
# 2025-12-02 09:39:21,853 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-02 09:39:21,857 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,857 INFO sqlalchemy.engine.Engine SELECT employees.id, employees.name, employees.department_id 
# FROM employees 
# WHERE employees.id = %(pk_1)s
# 2025-12-02 09:39:21,858 INFO sqlalchemy.engine.Engine [cached since 0.008217s ago] {'pk_1': 2}
# 2025-12-02 09:39:21,858 INFO sqlalchemy.engine.Engine ROLLBACK
# 2025-12-02 09:39:21,859 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,860 INFO sqlalchemy.engine.Engine INSERT INTO employees (name, department_id) VALUES (%(name)s, %(department_id)s)
# 2025-12-02 09:39:21,860 INFO sqlalchemy.engine.Engine [cached since 0.01706s ago] {'name': 'vamshi', 'department_id': 2}
# 2025-12-02 09:39:21,860 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-02 09:39:21,867 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,867 INFO sqlalchemy.engine.Engine SELECT employees.id, employees.name, employees.department_id 
# FROM employees 
# WHERE employees.id = %(pk_1)s
# 2025-12-02 09:39:21,868 INFO sqlalchemy.engine.Engine [cached since 0.01815s ago] {'pk_1': 3}
# 2025-12-02 09:39:21,868 INFO sqlalchemy.engine.Engine ROLLBACK
# 1 sai 1
# 2025-12-02 09:39:21,869 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,870 INFO sqlalchemy.engine.Engine SELECT employees.id AS employees_id, employees.name AS employees_name, employees.department_id AS employees_department_id 
# FROM employees
# 2025-12-02 09:39:21,870 INFO sqlalchemy.engine.Engine [generated in 0.00017s] {}
# 2025-12-02 09:39:21,871 INFO sqlalchemy.engine.Engine ROLLBACK
# 1 sai 1
# 2 yaswanth 1
# 3 vamshi 2
# 2025-12-02 09:39:21,872 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,873 INFO sqlalchemy.engine.Engine SELECT employees.id AS employees_id, employees.name AS employees_name, employees.department_id AS employees_department_id 
# FROM employees 
# WHERE employees.department_id = %(department_id_1)s
# 2025-12-02 09:39:21,873 INFO sqlalchemy.engine.Engine [generated in 0.00018s] {'department_id_1': 1}
# 2025-12-02 09:39:21,874 INFO sqlalchemy.engine.Engine ROLLBACK
# 1 sai 1
# 2 yaswanth 1
# 2025-12-02 09:39:21,875 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,876 INFO sqlalchemy.engine.Engine SELECT departments.id AS departments_id, departments.name AS departments_name 
# FROM departments 
# WHERE departments.name = %(name_1)s 
#  LIMIT %(param_1)s
# 2025-12-02 09:39:21,876 INFO sqlalchemy.engine.Engine [generated in 0.00018s] {'name_1': 'IT', 'param_1': 1}
# 2025-12-02 09:39:21,877 INFO sqlalchemy.engine.Engine SELECT employees.id AS employees_id, employees.name AS employees_name, employees.department_id AS employees_department_id 
# FROM employees 
# WHERE employees.department_id = %(department_id_1)s
# 2025-12-02 09:39:21,877 INFO sqlalchemy.engine.Engine [cached since 0.004604s ago] {'department_id_1': 1}
# 2025-12-02 09:39:21,879 INFO sqlalchemy.engine.Engine ROLLBACK
# 1 sai 1
# 2 yaswanth 1
# 2025-12-02 09:39:21,881 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-02 09:39:21,881 INFO sqlalchemy.engine.Engine SELECT departments.id AS departments_id, departments.name AS departments_name 
# FROM departments 
# WHERE departments.name = %(name_1)s 
#  LIMIT %(param_1)s
# 2025-12-02 09:39:21,881 INFO sqlalchemy.engine.Engine [cached since 0.005466s ago] {'name_1': 'IT', 'param_1': 1}
# 2025-12-02 09:39:21,884 INFO sqlalchemy.engine.Engine SELECT employees.id AS employees_id, employees.name AS employees_name, employees.department_id AS employees_department_id 
# FROM employees 
# WHERE %(param_1)s = employees.department_id
# 2025-12-02 09:39:21,884 INFO sqlalchemy.engine.Engine [generated in 0.00015s] {'param_1': 1}
# 2025-12-02 09:39:21,885 INFO sqlalchemy.engine.Engine ROLLBACK
# 1 sai 1
# 2 yaswanth 1