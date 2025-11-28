import csv  # Importing the csv module to handle CSV file operations
from typing import Optional  # Importing Optional for optional type annotations
from src.models.employee_model import EmployeeDirectory  # Importing the EmployeeDirectory model
from src.config.db_connection import get_connection  # Importing the get_connection function to establish DB connection
from fastapi import HTTPException

# This function retrieves all employee records from the database, optionally filtered by status
def get_all(status_filter: Optional[str] = ""):
    """
    Retrieves all employee records from the database.
    If a status filter is provided, it retrieves employees with the specified status.
    
    :param status_filter: Optional filter for the employee status (active, inactive, etc.)
    :return: List of employee records or None if no records are found
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object to interact with the database
        
        # If no status filter is provided, fetch all employees; otherwise, fetch employees by status
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.employee_directory")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.employee_directory WHERE status=%s", (status_filter,))
        
        row = cursor.fetchall()  # Fetch all results
        
        return row if row else None  # Return the fetched rows or None if no data is found
    except Exception as e:
        raise ValueError  # Raise a ValueError if any error occurs during fetching
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# This function retrieves a specific employee by their ID
def get_by_id(emp_id):
    """
    Retrieves an employee record by the given employee ID.
    
    :param emp_id: Employee ID to search for
    :return: Employee record or None if no employee is found
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Execute the SQL query to fetch the employee by its ID
        cursor.execute("SELECT * FROM ust_aims_db.employee_directory WHERE emp_id= %s", (emp_id,))
        row = cursor.fetchone()  # Fetch a single row
        
        return row if row else None  # Return the found row or None if not found
    except Exception as e:
        raise ValueError  # Raise a ValueError if any error occurs during fetching
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# This function inserts a new employee into the database
def insert_emp(new_emp: EmployeeDirectory):
    """
    Inserts a new employee record into the database.
    
    :param new_emp: The employee data to insert into the database
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Execute the SQL query to insert a new employee
        cursor.execute(
            """
            INSERT INTO ust_aims_db.employee_directory (
                emp_code, full_name, email, phone, department, location, join_date, status
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                new_emp.emp_code, 
                new_emp.full_name, 
                new_emp.email, 
                new_emp.phone, 
                new_emp.department, 
                new_emp.location, 
                new_emp.join_date, 
                new_emp.status
            )
        )
        conn.commit()  # Commit the transaction to the database
        
    except Exception as e:
        print(f"Error: {e}")  # Print any errors that occur during insertion
        
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# This function updates an existing employee's data by their ID
def update_emp_by_id(emp_id: int, update_emp: EmployeeDirectory):
    """
    Updates an existing employee's details in the database by their employee ID.
    
    :param emp_id: The employee ID to update
    :param update_emp: The updated employee data
    :return: The updated employee record
    :raises HTTPException: If the employee with the given ID is not found
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Check if the employee exists before trying to update
        existing_emp = get_by_id(emp_id)
        if not existing_emp:
            raise HTTPException(status_code=404, detail=f"Employee with ID {emp_id} not found.")
        
        # Execute the SQL query to update the employee record
        cursor.execute("""
        UPDATE ust_aims_db.employee_directory 
        SET 
            full_name = %s,
            email = %s,
            phone = %s,
            department = %s,
            location = %s,
            join_date = %s,
            status = %s
        WHERE emp_id = %s
        """, (
            update_emp.full_name, 
            update_emp.email, 
            update_emp.phone, 
            update_emp.department, 
            update_emp.location, 
            update_emp.join_date, 
            update_emp.status, 
            emp_id
        ))
        
        conn.commit()  # Commit the transaction to the database
        return update_emp  # Return the updated employee record  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating employee: {str(e)}")  # Raise error if update fails
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# This function deletes an employee by their ID
def delete_emp(emp_id):
    """
    Deletes an employee from the database by their employee ID.
    
    :param emp_id: The employee ID to delete
    :return: True if the employee is successfully deleted
    :raises ValueError: If the employee with the given ID is not found
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Check if the employee exists before attempting to delete
        if get_by_id(emp_id):
            cursor.execute("DELETE FROM ust_aims_db.employee_directory WHERE emp_id = %s", (emp_id,))
            conn.commit()  # Commit the deletion to the database
            return True  # Return True indicating the deletion was successful
        else:
            raise ValueError  # If the employee is not found, raise an error
        
    except Exception as e:
        raise ValueError  # Raise an error if any issues occur during deletion
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# This function searches for employees based on a specific field and keyword
def search_emp(field_type: str, keyword: str):
    """
    Searches for employees based on a field and a keyword.
    
    :param field_type: The field to search (e.g., 'full_name', 'email', etc.)
    :param keyword: The keyword to search for in the specified field
    :return: List of employee records matching the search criteria
    :raises Exception: If an error occurs during the search
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Execute the SQL query to search for employees based on the field and keyword
        cursor.execute(f"SELECT * FROM ust_aims_db.employee_directory WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()  # Fetch all matching results
        return data  # Return the search results
   
    except Exception as e:
        raise Exception(f"Error: {e}")  # If an error occurs during the search, raise an exception with the error message
   
    finally:
        if conn.open:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()
