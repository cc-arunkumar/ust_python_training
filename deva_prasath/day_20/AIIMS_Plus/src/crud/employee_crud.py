import pymysql  # MySQL connector for database interaction
from typing import List, Optional  # Type hinting for List and Optional
from ..models.employee_model import EmployeeCreate  # Importing EmployeeCreate model from employee_model

# Function to establish a connection to the MySQL database
def get_db_connection():
    return pymysql.connect(
        host="localhost",  # Database host
        user="root",  # Database username
        password="pass@word1",  # Database password
        database="aiims",  # Database name
    )

# Function to get employees, optionally filtered by status
def get_employees(status: Optional[str] = None):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor for database operations
    try:
        if status:  # If status filter is provided
            cursor.execute("select * FROM employee_directory WHERE status=%s", (status,))
        else:  # No filter, return all employees
            cursor.execute("select * FROM employee_directory")
        return cursor.fetchall()  # Return all the fetched employees
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to get a specific employee by their ID
def get_employee_by_id(emp_id: int):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute("select * FROM employee_directory WHERE emp_id=%s", (emp_id,))
        return cursor.fetchone()  # Return the employee data
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to create a new employee in the database
def create_employee(employee: EmployeeCreate):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute(
            """
            insert INTO employee_directory(employee_id, full_name, email, phone, department, status, join_date, status)
            values (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                employee.full_name,  # Employee full name
                employee.email,  # Employee email
                employee.phone,  # Employee phone number
                employee.department,  # Employee department
                employee.status,  # Employee status
                employee.location,  # Employee location
                employee.join_date,  # Employee join date
                employee.status  # Employee status (again)
            )
        )
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to update an existing employee's information
def update_employee(employee_id: int, employee: EmployeeCreate):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute(
            """
            update employee_directory 
            SET full_name = %s, email = %s, phone = %s, department = %s, status = %s
            WHERE employee_id = %s
            """, (
                employee.full_name,  # Employee full name
                employee.email,  # Employee email
                employee.phone,  # Employee phone number
                employee.department,  # Employee department
                employee.status,  # Employee status
            )
        )
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to update the status of an employee
def update_employee_status(employee_id: int, status: str):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute(
            "update employee_directory SET status = %s WHERE employee_id = %s", (status, employee_id)
        )
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to delete an employee by their ID
def delete_employee(employee_id: int):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute("delete FROM employee_directory WHERE employee_id = %s", (employee_id,))
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to search for employees based on a keyword
def search_employees(keyword: str):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        query = """
        select * FROM employee_directory WHERE 
        full_name LIKE %s OR 
        email LIKE %s OR 
        department LIKE %s
        """
        like_keyword = f"%{keyword}%"  # Prepare the keyword for SQL LIKE query
        cursor.execute(query, (like_keyword, like_keyword, like_keyword))
        return cursor.fetchall()  # Return all results
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to count the total number of employees
def count_employees():
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute("select COUNT(*) FROM employee_directory")  # Count all employees
        return cursor.fetchone()[0]  # Return the count
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection
