# Import necessary modules: pymysql for database operations and get_connection for DB connection
import pymysql
from src.config.db_connection import get_connection

# CREATE: Add a new employee to the database
def create_employee(emp_code, full_name, email, phone, department, location, join_date, status):
    # Establish a connection to the database
    conn = get_connection()
    cursor = conn.cursor()
    
    # SQL query to insert a new employee into the employee_master table
    sql = """
    INSERT INTO employee_master (
        emp_code, full_name, email, phone, department, location, join_date, status
    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    # Execute the query with the provided employee details
    cursor.execute(sql, (emp_code, full_name, email, phone, department, location, join_date, status))
    # Commit the transaction to save changes
    conn.commit()
    
    # Retrieve the ID of the newly created employee
    emp_id = cursor.lastrowid
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Return the newly created employee's ID
    return emp_id

# READ: Get employee details by employee ID
def get_employee_by_id(emp_id):
    # Establish a connection to the database
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # Use DictCursor to return results as dictionaries
    
    # SQL query to retrieve an employee based on their employee ID
    cursor.execute("SELECT * FROM employee_master WHERE emp_id=%s", (emp_id,))
    
    # Fetch the first result (should be a single employee)
    result = cursor.fetchone()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Return the employee data
    return result

# READ: Get all employees, optionally filtered by status
def get_all_employees(status=None):
    # Establish a connection to the database
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # Use DictCursor for dictionary results
    
    # If a status is provided, filter employees by status
    if status:
        cursor.execute("SELECT * FROM employee_master WHERE status=%s", (status,))
    else:
        # Otherwise, retrieve all employees
        cursor.execute("SELECT * FROM employee_master")
    
    # Fetch all the results (all employees)
    results = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Return the list of employee records
    return results

# READ: Search employees based on a keyword (search in multiple fields)
def search_employees(keyword):
    # Establish a connection to the database
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    # Prepare the keyword for a LIKE search (case-insensitive)
    like = f"%{keyword}%"
    
    # SQL query to search for the keyword in multiple columns
    sql = """SELECT * FROM employee_master
             WHERE emp_code LIKE %s OR full_name LIKE %s OR email LIKE %s OR department LIKE %s"""
    
    # Execute the search query
    cursor.execute(sql, (like, like, like, like))
    
    # Fetch all matching results
    results = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Return the search results (matching employees)
    return results

# READ: Count the total number of employees
def count_employees():
    # Get all employees and return the count
    length = len(get_all_employees())
    return length

# UPDATE: Update an employee's details by employee ID
def update_employee(emp_id, emp_code, full_name, email, phone, department, location, join_date, status):
    # Establish a connection to the database
    conn = get_connection()
    cursor = conn.cursor()
    
    # SQL query to update an employee's information
    sql = """UPDATE employee_master
             SET emp_code=%s, full_name=%s, email=%s, phone=%s,
                 department=%s, location=%s, join_date=%s, status=%s
             WHERE emp_id=%s"""
    
    # Execute the update query with the new employee details
    cursor.execute(sql, (emp_code, full_name, email, phone, department, location, join_date, status, emp_id))
    
    # Commit the transaction to save changes
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Return True to indicate success
    return True

# UPDATE: Update an employee's status (e.g., active, inactive)
def update_employee_status(emp_id, status):
    # Establish a connection to the database
    conn = get_connection()
    cursor = conn.cursor()
    
    # SQL query to update the status of an employee
    cursor.execute("UPDATE employee_master SET status=%s WHERE emp_id=%s", (status, emp_id))
    
    # Commit the transaction to save changes
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Return True to indicate success
    return True

# DELETE: Delete an employee from the database by their ID
def delete_employee(emp_id):
    # Establish a connection to the database
    conn = get_connection()
    cursor = conn.cursor()
    
    # SQL query to delete an employee by their employee ID
    cursor.execute("DELETE FROM employee_master WHERE emp_id=%s", (emp_id,))
    
    # Commit the transaction to save changes
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Return True to indicate success
    return True
