from src.config.db_connection import get_connection
from src.models.employee_model import EmployeeModel

# 1. Function to create an employee record in the database
def create_employee_db(employee: EmployeeModel):
    """
    Creates a new employee record in the 'employee_directory' table.
    Returns True if the employee was created successfully, False if there is a database connection issue.
    """
    conn = get_connection()
    if conn is None:
        return False  # Return False if the database connection fails
    with conn.cursor() as cursor:
        sql = """INSERT INTO employee_directory 
                 (emp_code, full_name, email, phone, department, location, join_date, status)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (
            employee.emp_code,
            employee.full_name,
            employee.email,
            employee.phone,
            employee.department,
            employee.location,
            employee.join_date,
            employee.status
        ))
        conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection
    return True  # Return True to indicate success

# 2. Function to search employees by a given keyword and value
def search_employees_db(keyword: str, value: str):
    """
    Searches for employees based on a keyword and value in the 'employee_directory' table.
    If the keyword is valid, the function performs a LIKE search.
    Returns the search results or an empty list if no results are found.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        like = f"%{value}%"  # Prepare the value for the LIKE query
        allowed_columns = ["emp_id", "emp_code", "full_name", "email", "phone",
                           "department", "location", "join_date", "status"]  # Allowed columns for search
        if keyword not in allowed_columns:
            return []  # Return an empty list if the keyword is invalid
        sql = f"SELECT * FROM employee_directory WHERE {keyword} LIKE %s"
        cursor.execute(sql, (like,))
        result = cursor.fetchall()  # Fetch all matching records
    conn.close()  # Close the database connection
    return result  # Return the search results

# 3. Function to get all employees
def get_all_employees_db():
    """
    Retrieves all employee records from the 'employee_directory' table.
    Returns a list of all employees or None if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM employee_directory")
        result = cursor.fetchall()  # Fetch all employee records
    conn.close()  # Close the database connection
    return result  # Return the list of employees

# 4. Function to list employees by status
def list_employees_by_status_db(status: str):
    """
    Retrieves employee records filtered by the given status.
    Returns the list of employees with the specified status, or None if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        # Perform a case-insensitive search for employees with the given status
        sql = "SELECT * FROM employee_directory WHERE LOWER(status) = LOWER(%s)"
        cursor.execute(sql, (status,))
        result = cursor.fetchall()  # Fetch the matching employee records
    conn.close()  # Close the database connection
    return result  # Return the list of employees with the given status

# 5. Function to get an employee by their ID
def get_employee_by_id_db(emp_id: int):
    """
    Retrieves an employee record by the given employee ID.
    Returns the employee record or None if the employee is not found or if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM employee_directory WHERE emp_id = %s", (emp_id,))
        result = cursor.fetchone()  # Fetch the employee record by ID
    conn.close()  # Close the database connection
    return result  # Return the employee record

# 6. Function to update an employee's record
def update_employee_db(emp_id: int, employee: EmployeeModel):
    """
    Updates an existing employee's record in the 'employee_directory' table.
    Returns True if the update is successful, False if there is an issue.
    """
    conn = get_connection()
    if conn is None:
        return False  # Return False if the database connection fails
    with conn.cursor() as cursor:
        sql = """UPDATE employee_directory 
                 SET emp_code=%s, full_name=%s, email=%s, phone=%s, 
                     department=%s, location=%s, join_date=%s, status=%s
                 WHERE emp_id=%s"""
        cursor.execute(sql, (
            employee.emp_code,
            employee.full_name,
            employee.email,
            employee.phone,
            employee.department,
            employee.location,
            employee.join_date,
            employee.status,
            emp_id
        ))
        conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection
    return True  # Return True to indicate success

# 7. Function to update an employee's status
def update_employee_status_db(emp_id: int, status: str):
    """
    Updates only the status of an existing employee.
    Returns True if the status was updated, False if no rows were affected (i.e., employee not found).
    """
    conn = get_connection()
    if conn is None:
        return False  # Return False if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("UPDATE employee_directory SET status = %s WHERE emp_id = %s",
                       (status, emp_id))
        conn.commit()  # Commit the transaction
        updated = cursor.rowcount  # Check how many rows were affected
    conn.close()  # Close the database connection
    return updated > 0  # Return True if one or more rows were updated, otherwise False

# 8. Function to delete an employee by their ID
def delete_employee_db(emp_id: int):
    """
    Deletes an employee record from the 'employee_directory' table by the given employee ID.
    Returns True if the employee was deleted, False if the employee was not found.
    """
    conn = get_connection()
    if conn is None:
        return False  # Return False if the database connection fails
    with conn.cursor() as cursor:
        # Perform the deletion by emp_id
        cursor.execute("DELETE FROM employee_directory WHERE emp_id = %s", (emp_id,))
        conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection
    return True  # Return True to indicate the deletion was successful

# 9. Function to count the total number of employees
def count_employees_db():
    """
    Returns the total count of employees in the 'employee_directory' table.
    Returns 0 if the database connection fails or no employees are found.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS total FROM employee_directory")
        result = cursor.fetchone()  # Fetch the total count of employees
    conn.close()  # Close the database connection
    return result["total"] if result else 0  # Return the total count, or 0 if no result
