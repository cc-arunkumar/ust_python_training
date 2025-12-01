from models.employee_model import Employee
from datetime import date
from fastapi import HTTPException
from config.db_connection import get_connection

def create_employee(emp:Employee):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        query="""INSERT INTO EMPLOYEE(
            first_name,last_name,email,position,salary,hire_date)
            VALUES (%s,%s,%s,%s,%s,%s)
        """
        data = (
            emp.first_name,
            emp.last_name,
            emp.email,
            emp.position,
            emp.salary,
            emp.hire_date
        )
        cursor.execute(query,data)
        conn.commit()
        return {"message": "Employee created successfully"}
    except Exception as e:
        print("Error:",e)
        raise HTTPException(status_code=500, detail="Error Adding employee")
    finally:
        cursor.close()
        conn.close()
        
def get_all_employee():
    try:
        conn = get_connection()
        cursor = conn.cursor()  

        query = """SELECT * FROM EMPLOYEE"""
        cursor.execute(query)  
        result = cursor.fetchall() 

        return result

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Error getting employees")
    finally:
        cursor.close()
        conn.close()

def delete_employee(emp_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "DELETE FROM EMPLOYEE WHERE employee_id = %s"
        cursor.execute(query, (emp_id,))
        conn.commit()
        
        return {"message": f"Employee with id {emp_id} deleted successfully"}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Error deleting employee")
    finally:
        cursor.close()
        conn.close()


def get_employee_by_id(emp_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM EMPLOYEE WHERE employee_id = %s"
        cursor.execute(query, (emp_id,))
        result = cursor.fetchone()
        
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")
        
        return result
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Error fetching employee")
    finally:
        cursor.close()
        conn.close()


def update_employee(emp_id: int, emp: Employee):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        query = """
        UPDATE EMPLOYEE
        SET first_name=%s, last_name=%s, email=%s, position=%s, salary=%s, hire_date=%s
        WHERE employee_id=%s
        """
        data = (
            emp.first_name,
            emp.last_name,
            emp.email,
            emp.position,
            emp.salary,
            emp.hire_date,
            emp_id
        )
        cursor.execute(query, data)
        conn.commit()
        
        return {"message": f"Employee with id {emp_id} updated successfully"}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Error updating employee")
    finally:
        cursor.close()
        conn.close()
