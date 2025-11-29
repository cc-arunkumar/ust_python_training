import pymysql
from typing import List,Optional
from models import Employee

# Function to establish a connection to the MySQL database
def get_db_connection():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "pass@word1",
        database = "ust_asset_db"
    )
    return conn


# Function to fetch a specific employee by their employee_id
def fetch_employee_by_id(emp_id : int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM employees WHERE employee_id = %s",(emp_id, ))
        return cursor.fetchone()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


# Function to create a new employee in the database
def create_new_employee(emp : Employee):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            """
            INSERT INTO employees(first_name,last_name,email,position,salary,hire_date)
            VALUES(%s, %s, %s, %s, %s, %s)
            """,(
                emp.first_name,
                emp.last_name,
                emp.email,
                emp.position,
                emp.salary,
                emp.hire_date
            )
        )
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()

 
# Function to remove an employee from the database by their employee_id        
def remove_employee(emp_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM employees WHERE employee_id = %s", (emp_id,))
        conn.commit()  # Commit the transaction to delete the employee
    except Exception as e:
        raise e  # Raise any errors that occur during the execution
    finally:
        cursor.close()
        conn.close()


# Function to update an existing employee's details
def modify_employee(employee_id: int, employee: Employee):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE employees
            SET first_name = %s, last_name = %s, email = %s, position = %s, salary = %s, hire_date = %s
            WHERE employee_id = %s
            """, (
                employee.first_name,
                employee.last_name,
                employee.email,
                employee.position,
                employee.salary,
                employee.hire_date,
                employee_id
            )
        )
        conn.commit()  # Commit the transaction to update the employee record
    except Exception as e:
        raise e  # Raise any errors that occur during the execution
    finally:
        cursor.close()
        conn.close()
        
        
        
