from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship,declarative_base,sessionmaker

# Database connection URL for MySQL
DATABASE_URL="mysql+pymysql://root:vinnu_4545@localhost:3306/ust_db"

# Engine helps SQLAlchemy talk to the database
engine=create_engine(DATABASE_URL,echo=True)

# SessionLocal is used to interact with database (insert, update, read, delete)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

# Base class for all ORM models (mapping between classes & tables)
Base=declarative_base()

# --------------------- MODEL CLASSES -------------------------

# Department Table Mapping (ORM Model)
class Department(Base):
    __tablename__="departments"   # Table name inside DB
    
    id=Column(Integer,primary_key=True,index=True)  # Primary Key column
    name=Column(String(50),nullable=False)          # Department name column
    
    # Relationship -> One Department has many Employees (One-to-Many)
    employees=relationship("Employee",back_populates="departments")

# Employee Table Mapping (ORM Model)
class Employee(Base):
    __tablename__="employeees"  # Table name inside DB (typo but works)
    
    id=Column(Integer,primary_key=True,index=True)  # Employee ID
    name=Column(String(50),nullable=False)          # Employee name
    
    # Foreign Key linking to department table
    department_id=Column(Integer,ForeignKey("departments.id"))
    
    # Relationship -> Each Employee belongs to one Department
    departments=relationship("Department",back_populates="employees")

# Create all tables in MySQL based on the above models
Base.metadata.create_all(bind=engine)


# --------------------- CRUD FUNCTIONS -------------------------

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


# --------------------- TEST EXECUTION -------------------------
if __name__=="__main__":
    dep=create_department("IT")  # Create department example
    print(dep)

    # Create employees
    emp1=create_employee("vinnu",dep.id)
    emp2=create_employee("hima",dep.id)
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
        
        
#SAMPLE OUTPUT:
# 2025-12-01 22:06:50,943 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2025-12-01 22:06:50,943 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:06:50,945 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2025-12-01 22:06:50,945 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:06:50,946 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2025-12-01 22:06:50,947 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:06:50,947 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:06:50,948 INFO sqlalchemy.engine.Engine DESCRIBE `ust_db`.`departments`
# 2025-12-01 22:06:50,949 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:06:50,952 INFO sqlalchemy.engine.Engine DESCRIBE `ust_db`.`employeees`
# 2025-12-01 22:06:50,952 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:06:50,954 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-01 22:06:50,959 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:06:50,961 INFO sqlalchemy.engine.Engine INSERT INTO departments (name) VALUES (%(name)s)
# 2025-12-01 22:06:50,961 INFO sqlalchemy.engine.Engine [generated in 0.00036s] {'name': 'IT'}
# 2025-12-01 22:06:50,963 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-01 22:06:50,971 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:06:50,975 INFO sqlalchemy.engine.Engine SELECT departments.id, departments.name
# FROM departments
# WHERE departments.id = %(pk_1)s
# 2025-12-01 22:06:50,980 INFO sqlalchemy.engine.Engine [generated in 0.00523s] {'pk_1': 2}
# 2025-12-01 22:06:50,982 INFO sqlalchemy.engine.Engine ROLLBACK
# <__main__.Department object at 0x0000029B4111AF90>
# 2025-12-01 22:06:50,983 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:06:50,984 INFO sqlalchemy.engine.Engine INSERT INTO employeees (name, department_id) VALUES (%(name)s, %(department_id)s)
# 2025-12-01 22:06:50,984 INFO sqlalchemy.engine.Engine [generated in 0.00031s] {'name': 'vinnu', 'department_id': 
# 2}
# 2025-12-01 22:06:50,985 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-01 22:06:50,989 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:06:50,990 INFO sqlalchemy.engine.Engine SELECT employeees.id, employeees.name, employeees.department_id
# FROM employeees
# WHERE employeees.id = %(pk_1)s
# 2025-12-01 22:06:50,991 INFO sqlalchemy.engine.Engine [generated in 0.00038s] {'pk_1': 3}
# 2025-12-01 22:06:50,992 INFO sqlalchemy.engine.Engine ROLLBACK
# 2025-12-01 22:06:50,992 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:06:50,993 INFO sqlalchemy.engine.Engine INSERT INTO employeees (name, department_id) VALUES (%(name)s, %(department_id)s)
# 2025-12-01 22:06:50,993 INFO sqlalchemy.engine.Engine [cached since 0.009097s ago] {'name': 'hima', 'department_id': 2}
# 2025-12-01 22:06:50,994 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-01 22:06:50,999 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:06:51,000 INFO sqlalchemy.engine.Engine SELECT employeees.id, employeees.name, employeees.department_id
# FROM employeees
# WHERE employeees.id = %(pk_1)s
# 2025-12-01 22:06:51,006 INFO sqlalchemy.engine.Engine [cached since 0.01616s ago] {'pk_1': 4}
# 2025-12-01 22:06:51,008 INFO sqlalchemy.engine.Engine ROLLBACK
# 3 vinnu 2
# 2025-12-01 22:06:51,010 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:06:51,011 INFO sqlalchemy.engine.Engine SELECT employeees.id AS employeees_id, employeees.name AS employeees_name, employeees.department_id AS employeees_department_id
# FROM employeees
# 2025-12-01 22:06:51,011 INFO sqlalchemy.engine.Engine [generated in 0.00036s] {}
# 2025-12-01 22:06:51,012 INFO sqlalchemy.engine.Engine ROLLBACK
# 1 vinnu 1
# 2 hima 1
# 3 vinnu 2
# 4 hima 2
# 2025-12-01 22:06:51,013 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:06:51,014 INFO sqlalchemy.engine.Engine SELECT employeees.id AS employeees_id, employeees.name AS employeees_name, employeees.department_id AS employeees_department_id
# FROM employeees
# WHERE employeees.department_id = %(department_id_1)s
# 2025-12-01 22:06:51,014 INFO sqlalchemy.engine.Engine [generated in 0.00034s] {'department_id_1': 1}
# 2025-12-01 22:06:51,015 INFO sqlalchemy.engine.Engine ROLLBACK
# 1 vinnu 1
# 2 hima 1
# 2025-12-01 22:06:51,016 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:06:51,017 INFO sqlalchemy.engine.Engine SELECT departments.id AS departments_id, departments.name AS departments_name
# FROM departments
# WHERE departments.name = %(name_1)s
#  LIMIT %(param_1)s
# 2025-12-01 22:06:51,018 INFO sqlalchemy.engine.Engine [generated in 0.00039s] {'name_1': 'IT', 'param_1': 1}     
# 2025-12-01 22:06:51,018 INFO sqlalchemy.engine.Engine SELECT employeees.id AS employeees_id, employeees.name AS employeees_name, employeees.department_id AS employeees_department_id
# FROM employeees
# WHERE employeees.department_id = %(department_id_1)s
# 2025-12-01 22:06:51,019 INFO sqlalchemy.engine.Engine [cached since 0.004731s ago] {'department_id_1': 1}        
# 2025-12-01 22:06:51,020 INFO sqlalchemy.engine.Engine ROLLBACK
# 1 vinnu 1
# 2 hima 1
# 2025-12-01 22:06:51,020 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:06:51,021 INFO sqlalchemy.engine.Engine SELECT departments.id AS departments_id, departments.name AS departments_name
# FROM departments
# WHERE departments.name = %(name_1)s
#  LIMIT %(param_1)s
# 2025-12-01 22:06:51,021 INFO sqlalchemy.engine.Engine [cached since 0.004022s ago] {'name_1': 'IT', 'param_1': 1}2025-12-01 22:06:51,023 INFO sqlalchemy.engine.Engine SELECT employeees.id AS employeees_id, employeees.name AS employeees_name, employeees.department_id AS employeees_department_id
# FROM employeees
# WHERE %(param_1)s = employeees.department_id
# 2025-12-01 22:06:51,023 INFO sqlalchemy.engine.Engine [generated in 0.00036s] {'param_1': 1}
# 2025-12-01 22:06:51,024 INFO sqlalchemy.engine.Engine ROLLBACK
# 1 vinnu 1
# 2 hima 1