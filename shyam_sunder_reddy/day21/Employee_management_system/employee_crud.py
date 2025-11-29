# Import PyMySQL to interact with MySQL databases
import pymysql
# Import the Employee Pydantic model for structured validation and response handling
from employee_model import Employee
# Import the database connection helper function
from db_connection import get_connection

def read_employee_by_id(employee_id):
    # """
    # Fetch a single employee record by ID from the database.
    # Args:
    #     employee_id (int): The unique identifier of the employee.
    # Returns:
    #     Employee object if found, otherwise None.
    # """
    conn = None
    try:
        conn = get_connection()              # Establish DB connection
        cursor = conn.cursor()               # Create a cursor for executing queries
        cursor.execute(
            "SELECT * FROM ust_db.employees WHERE employee_id=%s", 
            (employee_id,)
        )                                    # Execute SELECT query with parameter binding
        row = cursor.fetchone()              # Fetch one record
        if row:
            return Employee(**row)           # Map result to Employee model
        return None                          # Return None if no record found
    except Exception as e:
        print(e)                             # Log exception for debugging
        return None
    finally:
        if conn and conn.open:               # Ensure resources are closed
            cursor.close()
            conn.close()
            
def create_employee(emp: Employee):
    # """
    # Insert a new employee record into the database.
    # Args:
    #     emp (Employee): Employee object containing details to insert.
    # Returns:
    #     Employee object with auto-generated ID if successful, otherwise None.
    # """
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
                emp.hire_date.strftime("%Y-%m-%d")  # Convert date to string format
            )
        )                                    # Execute INSERT query
        conn.commit()                        # Commit transaction
        new_id = cursor.lastrowid            # Retrieve auto-generated employee_id
        return read_employee_by_id(new_id)   # Return full Employee object
    except Exception as e:
        print("Error in create_employee:", e)
        return None
    finally:
        if conn and conn.open:
            cursor.close()
            conn.close()

def update_employee_by_id(employee_id, emp: Employee):
    # """
    # Update an existing employee record by ID.
    # Args:
    #     employee_id (int): The unique identifier of the employee.
    #     emp (Employee): Employee object containing updated details.
    # Returns:
    #     Updated Employee object if successful, otherwise None.
    # """
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
            (
                emp.first_name,
                emp.last_name,
                emp.email,
                emp.position,
                emp.salary,
                emp.hire_date,
                employee_id
            )
        )                                    # Execute UPDATE query
        conn.commit()
        return read_employee_by_id(employee_id)  # Return updated Employee object
    except Exception as e:
        print(e)
        return None
    finally:
        if conn and conn.open:
            cursor.close()
            conn.close()

def delete_employee_by_id(emp_id):
    # """
    # Delete an employee record by ID.
    # Args:
    #     emp_id (int): The unique identifier of the employee.
    # Returns:
    #     True if deletion successful, False otherwise.
    # """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if read_employee_by_id(emp_id):      # Check if employee exists before deletion
            cursor.execute(
                "DELETE FROM ust_db.employees WHERE employee_id=%s", 
                (emp_id,)
            )
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
