import pymysql
from employee_model import Employee
from db_connection import get_connection

def read_employee_by_id(employee_id):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_db.employees WHERE employee_id=%s", (employee_id,))
        row = cursor.fetchone()
        if row:
            return Employee(**row)
        return None  
    except Exception as e:
        print(e)
        return None
    finally:
        if conn and conn.open:
            cursor.close()
            conn.close()
            
def create_employee(emp: Employee):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO ust_db.employees 
            (first_name, last_name, email, position, salary, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            ''',
            (
                emp.first_name,
                emp.last_name,
                emp.email,
                emp.position,
                emp.salary,
                emp.hire_date.strftime("%Y-%m-%d")  
            )
        )
        conn.commit()
        new_id = cursor.lastrowid
        return read_employee_by_id(new_id)   
    except Exception as e:
        print("Error in create_employee:", e)
        return None
    finally:
        if conn and conn.open:
            cursor.close()
            conn.close()

def update_employee_by_id(employee_id, emp: Employee):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            UPDATE ust_db.employees 
            SET first_name=%s, last_name=%s, email=%s, 
                position=%s, salary=%s, hire_date=%s 
            WHERE employee_id=%s
            ''',
            (emp.first_name, emp.last_name, emp.email,
             emp.position, emp.salary, emp.hire_date, employee_id)
        )
        conn.commit()
        return read_employee_by_id(employee_id)  
    except Exception as e:
        print(e)
        return None  
    finally:
        if conn and conn.open:
            cursor.close()
            conn.close()

def delete_employee_by_id(emp_id):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if read_employee_by_id(emp_id):
            cursor.execute("DELETE FROM ust_db.employees WHERE employee_id=%s", (emp_id,))
            conn.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
    finally:
        if conn and conn.open:
            cursor.close()
            conn.close()
