import csv
from typing import Optional
from src.models.employee_model import EmployeeDirectory
from src.config.db_connection import get_connection



# Function to fetch all employees from the database, with an optional status filter
def get_all(status_filter: Optional[str] = ""):
    try:
        conn = get_connection()  # Establish database connection
        cursor = conn.cursor()
        
        # If no status filter is provided, fetch all employees
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.employee_directory")
        else:
            # If a status filter is provided, fetch employees with that status
            cursor.execute("SELECT * FROM ust_aims_db.employee_directory WHERE status=%s", (status_filter,))
        
        row = cursor.fetchall()  # Fetch all the rows from the query
        
        return row if row else None  # Return the result if data is found, else None
    except Exception as e:
        raise ValueError  # Raise an exception if an error occurs during the process
    finally:
        if conn:
            cursor.close()
            conn.close()  # Close the connection when done


# Function to fetch a specific employee by ID
def get_by_id(emp_id):
    try:
        conn = get_connection()  # Establish database connection
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM ust_aims_db.employee_directory WHERE emp_id= %s", (emp_id,))
        row = cursor.fetchone()  # Fetch the single row by employee ID
        
        return row if row else None  # Return the row if found, else None
    except Exception as e:
        raise ValueError  # Raise an exception if an error occurs
    finally:
        if conn:
            cursor.close()
            conn.close()  # Close the connection when done


# Function to insert a new employee into the database
def insert_emp(new_emp: EmployeeDirectory):
    try:
        conn = get_connection()  # Establish database connection
        cursor = conn.cursor()
        
        # Proceed with insertion of new employee
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
        conn.commit()  # Commit the transaction
        
    except Exception as e:
        print(f"Error: {e}")  # Print error if insertion fails
        
    finally:
        if conn:
            cursor.close()
            conn.close()  # Close the connection when done


# Function to update an existing employee's details by their ID
from fastapi import HTTPException
def update_emp_by_id(emp_id: int, update_emp: EmployeeDirectory):
    try:
        conn = get_connection()  # Establish database connection
        cursor = conn.cursor()
        
        # Check if the employee exists before updating
        existing_emp = get_by_id(emp_id)
        if not existing_emp:
            raise HTTPException(status_code=404, detail=f"Employee with ID {emp_id} not found.")
        
        # Proceed with the update query
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
        
        conn.commit()  # Commit the transaction
        return update_emp  # Return the updated employee data  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating employee: {str(e)}")  # Raise error if update fails
    finally:
        if conn:
            cursor.close()
            conn.close()  # Close the connection when done


# Function to delete an employee from the database by ID
def delete_emp(emp_id):
    try:
        conn = get_connection()  # Establish database connection
        cursor = conn.cursor()
        
        # Check if the employee exists before deleting
        if get_by_id(emp_id):
            cursor.execute("DELETE FROM ust_aims_db.employee_directory WHERE emp_id = %s", (emp_id,))
            conn.commit()  # Commit the deletion
            return True  # Return True if the deletion is successful
        else:
            raise ValueError  # Raise error if employee is not found
        
    except Exception as e:
        raise ValueError  # Raise error if deletion fails
    finally:
        if conn:
            cursor.close()
            conn.close()  # Close the connection when done


# Function to search employees based on a specific field and keyword
def search_emp(field_type: str, keyword: str):
    try:
        conn = get_connection()  # Establish database connection
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM ust_aims_db.employee_directory WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()  # Fetch all the matching rows
        
        return data  # Return the search results if found
    except Exception as e:
        raise Exception(f"Error: {e}")  # Raise an error if the search fails
    finally:
        if conn.open:
            cursor.close()
            conn.close()  # Close the connection when done

