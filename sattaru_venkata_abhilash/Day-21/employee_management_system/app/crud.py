import pymysql
# from db_connection import get_connection
# from db_connection import get_connection
from .db_connection import get_connection


# from models import Employeefrom .models import Employee
from .models import Employee


def create_employee(employee: Employee):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO employees (first_name, last_name, email, position, salary, hire_date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                employee.first_name, 
                employee.last_name, 
                employee.email, 
                employee.position, 
                employee.salary, 
                employee.hire_date
            ))
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            conn.rollback()
            return {"error": f"Error inserting employee: {str(e)}"}
        finally:
            conn.close()

def get_employee_by_id(employee_id: int):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM employees WHERE employee_id = %s"
            cursor.execute(query, (employee_id,))
            employee = cursor.fetchone()
            if employee:
                return employee
            return {"error": "Employee not found"}
        finally:
            conn.close()

def update_employee(employee_id: int, employee: Employee):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                UPDATE employees
                SET first_name = %s, last_name = %s, email = %s, position = %s, salary = %s, hire_date = %s
                WHERE employee_id = %s
            """
            cursor.execute(query, (
                employee.first_name, 
                employee.last_name, 
                employee.email, 
                employee.position, 
                employee.salary, 
                employee.hire_date, 
                employee_id
            ))
            conn.commit()
            if cursor.rowcount == 0:
                return {"error": "Employee not found"}
            return {"message": "Employee updated successfully"}
        except Exception as e:
            conn.rollback()
            return {"error": f"Error updating employee: {str(e)}"}
        finally:
            conn.close()

def delete_employee(employee_id: int):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM employees WHERE employee_id = %s"
            cursor.execute(query, (employee_id,))
            conn.commit()
            if cursor.rowcount == 0:
                return {"error": "Employee not found"}
            return {"message": "Employee deleted successfully"}
        except Exception as e:
            conn.rollback()
            return {"error": f"Error deleting employee: {str(e)}"}
        finally:
            conn.close()
