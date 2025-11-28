import pymysql
from typing import List, Optional
from ..model.employee_model import EmployeeCreate

# Function to establish a connection to the MySQL database
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db",  
    )

# Function to fetch employees, with an optional status filter
def fetch_employees(status: Optional[str] = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if status:
            # If status is provided, filter employees by the status
            cursor.execute("SELECT * FROM employee_directory WHERE status=%s", (status,))
        else:
            # If no status is provided, return all employees
            cursor.execute("SELECT * FROM employee_directory")
        return cursor.fetchall()  # Return all the fetched employees
    finally:
        cursor.close()
        conn.close()

# Function to fetch a specific employee by their employee_id
def fetch_employee_by_id(employee_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Retrieve employee record based on the given employee_id
        cursor.execute("SELECT * FROM employee_directory WHERE emp_id=%s", (employee_id,))
        return cursor.fetchone()  # Return the fetched employee record
    finally:
        cursor.close()
        conn.close()

# Function to create a new employee in the database
def create_new_employee(employee: EmployeeCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO employee_directory(emp_code,full_name, email, phone, department,location, join_date, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                employee.emp_code,
                employee.full_name,
                employee.email,
                employee.phone,
                employee.department,
                employee.location,
                employee.join_date,
                employee.status,
            )
        )
        conn.commit()  # Commit the transaction to save the employee record
    except Exception as e:
        raise e  # Raise any errors that occur during the execution
    finally:
        cursor.close()
        conn.close()

# Function to update an existing employee's details
def modify_employee(employee_id: int, employee: EmployeeCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE employee_directory 
            SET emp_code = %s, full_name = %s, email = %s, phone = %s, department = %s,location = %s, status = %s, join_date = %s
            WHERE emp_id = %s
            """, (
                employee.emp_code,
                employee.full_name,
                employee.email,
                employee.phone,
                employee.department,
                employee.location,
                employee.status,
                employee.join_date,
                employee_id
            )
        )
        conn.commit()  # Commit the transaction to update the employee record
    except Exception as e:
        raise e  # Raise any errors that occur during the execution
    finally:
        cursor.close()
        conn.close()

# Function to update the status of an employee (e.g., from 'Active' to 'Inactive')
def modify_employee_status(employee_id: int, status: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE employee_directory SET status = %s WHERE emp_id = %s", (status, employee_id)
        )
        conn.commit()  # Commit the transaction to update the status
    except Exception as e:
        raise e  # Raise any errors that occur during the execution
    finally:
        cursor.close()
        conn.close()

# Function to remove an employee from the database by their employee_id
def remove_employee(employee_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM employee_directory WHERE emp_id = %s", (employee_id,))
        conn.commit()  # Commit the transaction to delete the employee
    except Exception as e:
        raise e  # Raise any errors that occur during the execution
    finally:
        cursor.close()
        conn.close()

# Function to search employees by a keyword (e.g., in their name, email, or department)
def find_employees_by_keyword(keyword: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
        SELECT * FROM employee_directory WHERE 
        full_name LIKE %s OR 
        email LIKE %s OR 
        department LIKE %s
        """
        like_keyword = f"%{keyword}%"  # Create a pattern to match the keyword
        cursor.execute(query, (like_keyword, like_keyword, like_keyword))
        return cursor.fetchall()  # Return all matching employee records
    finally:
        cursor.close()
        conn.close()

# Function to get the total count of employees in the database
def get_total_employee_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM employee_directory")
        return cursor.fetchone()[0]  # Return the count of employees
    finally:
        cursor.close()
        conn.close()
