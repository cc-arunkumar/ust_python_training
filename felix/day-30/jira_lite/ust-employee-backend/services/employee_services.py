from database.mysql_connection import SessionLocal, Employee
from services.user_services import get_User_by_id

def get_all_employees_for_admin():
    try:
        session = SessionLocal()
        employees = session.query(Employee).all()      
        session.close()
        if not employees:
            return {"detail":"No employees found"}
        return employees
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
def get_emploee_by_id(emp_id:int):
    try:
        session = SessionLocal()
        emp = session.query(Employee).filter(Employee.id == emp_id).first()
        session.close()
        
        return emp
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
def get_all_employees(manager_id:int):
    try:
        session = SessionLocal()
        employees = session.query(Employee).filter(Employee.manager_id == manager_id).all()      
        session.close()
        if not employees:
            return {"detail":"No employees found"}
        return employees
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
def get_employee_by_id(emp_id:int,manager_id:int):
    try:
        session = SessionLocal()
        emp = session.query(Employee).filter(Employee.id == emp_id).filter(Employee.manager_id == manager_id).first()
        session.close()
        
        return emp
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
def create_employee(employee_data):
    try:
        session = SessionLocal()
        
        new_employee = Employee(
            name=employee_data.name, 
            email=employee_data.email, 
            designation=employee_data.designation, 
            manager_id=employee_data.manager_id
        )
        
        session.add(new_employee)
        session.commit()
        session.refresh(new_employee)
    except Exception as e:
        session.rollback()
        print("ERROR: ,",e)
        return None
    finally:
        print("Completed")
    session.close()
    return new_employee

def update_employee(emp_id,manager_id, updated_data):
    try:
        session = SessionLocal()
        
        # Fetch the employee by ID
        employee = session.query(Employee).filter(Employee.id == emp_id).filter(Employee.manager_id == manager_id).first()
        if not employee:
            print("Employee not found")
            return None
        
        # Update fields
        employee.name = updated_data.name
        employee.email = updated_data.email
        employee.designation = updated_data.designation
        employee.manager_id = updated_data.manager_id
        
        session.commit()
        session.refresh(employee)
        return employee
    except Exception as e:
        session.rollback()
        print("ERROR:", e)
        return None
    finally:
        print("Completed")
        session.close()
        
def delete_employee(emp_id,manager_id):
    try:
        session = SessionLocal()
        
        # Fetch the employee by ID
        employee = session.query(Employee).filter(Employee.id == emp_id).filter(Employee.manager_id == manager_id).first()
        if not employee:
            print("Employee not found")
            return None
        
        session.delete(employee)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print("ERROR:", e)
        return False
    finally:
        print("Completed")
        session.close()