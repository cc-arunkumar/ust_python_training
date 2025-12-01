from db_connection import get_connection
from employee_inventory import Employee
import datetime

def create_employee(emp: Employee):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO employees (
                first_name, last_name, email, position, salary, hire_date)
                VALUES (%s, %s, %s, %s, %s, %s)"""
                
            cursor.execute(sql, (
                emp.first_name, emp.last_name, emp.email,
                emp.position, emp.salary, datetime.datetime.now().strftime("%Y-%m-%d")
            )) 
            
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()

def get_employee_by_id(emp_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM employees WHERE employee_id=%s", (emp_id,))
            return cursor.fetchone()
    finally:
        conn.close()
        
def get_all_employees():
    conn = get_connection()
    try:
        with conn.cursor() as cursor: 
            cursor.execute("SELECT * FROM employees")
            return cursor.fetchall()
    finally:
        conn.close()
        
def update_employee(emp_id: int, emp: Employee):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            UPDATE employees
            SET first_name=%s, last_name=%s, email=%s, position=%s, salary=%s,
                hire_date=%s WHERE emp_id=%s
            """
            cursor.execute(sql, (
                emp.first_name, emp.last_name, emp.email, emp.position,
                emp.salary, emp.hire_date.strftime("%Y-%m-%d"), emp_id
            ))
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()


def delete_employee(emp_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM employees WHERE employee_id=%s", (emp_id,))
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()
