import csv
from typing import Optional

from src.models.employee_model import EmployeeDirectory
from src.config.db_connection import get_connection


# Function to fetch all employees, optionally filtered by status
def get_all(status_filter: Optional[str] = ""):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()

        # If no status filter is provided, fetch all employees
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.employee_directory")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.employee_directory WHERE status = %s", (status_filter,))
        
        # Fetch all rows matching the query
        row = cursor.fetchall()
        
        return row if row else None  # Return the rows or None if no data is found
    except Exception as e:
        # Raise an error if the query execution fails
        raise ValueError
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Function to fetch a specific employee by their ID
def get_by_id(emp_id):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute a query to fetch the employee by ID
        cursor.execute("SELECT * FROM ust_aims_db.employee_directory WHERE emp_id = %s", (emp_id,))
        row = cursor.fetchone()
        
        return row if row else None  # Return the employee data if found, or None if not
    except Exception as e:
        # Raise an error if the query execution fails
        raise ValueError
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Function to insert a new employee into the database
def insert_emp(new_emp: EmployeeDirectory):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Insert the new employee's data into the employee directory table
        cursor.execute(
            """
            INSERT INTO ust_aims_db.employee_directory (
                emp_code, full_name, email, phone, department, location, join_date, status
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
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
        # Commit the transaction to save the new employee record in the database
        conn.commit()
        
    except Exception as e:
        # Print an error message if something goes wrong during insertion
        print(f"Error: {e}")
        
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Function to update an employee's details by their ID
from fastapi import HTTPException

def update_emp_by_id(emp_id: int, update_emp: EmployeeDirectory):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the employee exists before attempting to update
        existing_emp = get_by_id(emp_id)
        if not existing_emp:
            raise HTTPException(status_code=404, detail=f"Employee with ID {emp_id} not found.")
        
        # Update the employee's data in the database
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
        
        # Commit the transaction to save the updated employee record
        conn.commit()
        return update_emp  # Return the updated employee data
    except Exception as e:
        # Raise an HTTP exception if an error occurs during the update
        raise HTTPException(status_code=500, detail=f"Error updating employee: {str(e)}")
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Function to delete an employee by their ID
def delete_emp(emp_id):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the employee exists before attempting to delete
        if get_by_id(emp_id):
            # Execute a query to delete the employee from the database
            cursor.execute("DELETE FROM ust_aims_db.employee_directory WHERE emp_id = %s", (emp_id,))
            # Commit the transaction to delete the employee
            conn.commit()
            return True  # Return True if deletion was successful
        else:
            raise ValueError  # Raise an error if the employee is not found
        
    except Exception as e:
        # Raise an error if deletion fails
        raise ValueError
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Function to search for employees by a specific field and keyword
def search_emp(field_type: str, keyword: str):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute a query to search employees based on the field and keyword
        cursor.execute(f"SELECT * FROM ust_aims_db.employee_directory WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()  # Fetch all matching records
        
        return data  # Return the search results
    except Exception as e:
        # Raise an error if the query execution fails
        raise Exception(f"Error: {e}")
    finally:
        # Close the database connection and cursor
        if conn.open:
            cursor.close()
            conn.close()

# The following code is commented out, as it's for handling CSV data
# for bulk employee import. It processes the input CSV file, validates the rows,
# and writes valid and invalid rows to separate CSV files.

# valid_rows_emp = []
# invalid_rows_emp = []

# required_fields_emp = [
#     "emp_code",
#     "full_name",
#     "email",
#     "phone",
#     "department",
#     "location",
#     "join_date",
#     "status"
# ]

# with open("employee_directory.csv", "r") as file:
#     csv_reader = csv.DictReader(file)
#     header = csv_reader.fieldnames

#     for row in csv_reader:
#         try:
#             # Validate each row against the EmployeeDirectory model
#             valid = EmployeeDirectory(**row)
#             valid_rows_emp.append(valid.model_dump())  
#         except Exception as e:
#             # Store invalid rows and the associated error
#             row['error'] = str(e)  
#             invalid_rows_emp.append(row)

# fieldnames_emp = required_fields_emp + ['error']  

# with open("validated_employee_inventory.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=required_fields_emp)
#     writer.writeheader()
#     for row in valid_rows_emp:
#         row.pop('emp_id', None)  # Remove the emp_id before saving
#         writer.writerow(row) 

# with open("invalid_rows_emp.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames_emp)
#     writer.writeheader()
#     for row in invalid_rows_emp:
#         row.pop('emp_id', None)  # Remove the emp_id before saving
#         writer.writerow(row)
