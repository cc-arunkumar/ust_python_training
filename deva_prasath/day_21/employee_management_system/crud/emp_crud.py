import pymysql
from typing import List,Optional
from models.emp_models import Employee

# Function to establish and return a database connection
def get_db_connection():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "pass@word1",
        database = "employee"
    )
    return conn


# Function to check if an email already exists in the employees table
def email_exists(email: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT email FROM employees WHERE email=%s", (email,))
        result = cursor.fetchone()  # Returns result if email exists
        return result is not None   # True → exists, False → does not exist
    finally:
        cursor.close()
        conn.close()


# Fetch a single employee record by employee_id
def fetch_employee_by_id(emp_id : int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM employees WHERE employee_id = %s",(emp_id, ))
        return cursor.fetchone()  # Returns one row or None
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()

# Insert a new employee record into the database
def create_emp(ob: Employee):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if email already exists before inserting
    cursor.execute("SELECT email FROM employees WHERE email=%s", (ob.email,))
    if cursor.fetchone():
        raise Exception("Email already exists")

    try:
        cursor.execute(
            """
            INSERT INTO employees (first_name, last_name, email, position, salary, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                ob.first_name,
                ob.last_name,
                ob.email,
                ob.position,
                ob.salary,
                ob.hire_date
            )
        )
        conn.commit()  # Save changes to database
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()

        
# Delete an employee using employee_id
def remove_employee(emp_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM employees WHERE employee_id = %s", (emp_id,))
        conn.commit()  # Commit delete operation
    except Exception as e:
        raise e  # Forward database error
    finally:
        cursor.close()
        conn.close()


# Update an existing employee using employee_id
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
        conn.commit()  # Save updated values
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
