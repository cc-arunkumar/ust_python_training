from typing import List  # Import List type hint for function signatures
import pymysql  # Import pymysql to connect and interact with MySQL databases
from fastapi import FastAPI, HTTPException  # Import FastAPI framework and HTTPException for API error handling
from src.config.db_connection import get_connection # Import custom function to establish DB connection
from src.models.employee_pydentic import EmployeeDirectory  # Import Pydantic model for employee validation

from fastapi import HTTPException  # Redundant import (already imported above, but harmless)

# -----------------------------
# CREATE EMPLOYEE
# -----------------------------
def create_employee(emp: EmployeeDirectory):
    """
    Insert a new employee record into the employee_directory table.
    Accepts a validated EmployeeDirectory object from Pydantic.
    """
    try:
        conn = get_connection()  # Establish DB connection
        cursor = conn.cursor()   # Create cursor object for executing SQL queries

        # SQL query for inserting new employee record
        query = """
            INSERT INTO employee_directory
            (emp_code, full_name, email, phone, department, location, join_date, status)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        # Values tuple extracted from Pydantic model
        values = (
            emp.emp_code, emp.full_name, emp.email, emp.phone,
            emp.department, emp.location, emp.join_date, emp.status
        )

        cursor.execute(query, values)  # Execute insert query
        conn.commit()  # Commit transaction to save changes

        # Return success message with newly created employee ID
        return {"message": "Employee created successfully", "employee_id": cursor.lastrowid}

    except Exception as e:
        # Raise HTTP 500 error if database operation fails
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()  # Close cursor
        conn.close()    # Close connection
def get_all_employee():
    try:
        conn = get_connection()
        cursor=conn.cursor
        sql="""
        SELECT * FROM ust_aims.asset_inventory"""
        cursor.execute(sql)
        cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500,detail="")
    finally:
        if conn:
            cursor.close()
            conn.close()
# -----------------------------
# READ ALL EMPLOYEES (with optional status filter)
# -----------------------------
def get_all_employees_status(status: str | None = None):
    """
    Fetch all employees from employee_directory.
    If status is provided, filter employees by status.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # DictCursor returns rows as dictionaries

        if status:
            # Query employees filtered by status
            cursor.execute("SELECT * FROM employee_directory WHERE status=%s", (status,))
        else:
            # Query all employees
            cursor.execute("SELECT * FROM employee_directory")

        results = cursor.fetchall()  # Fetch all rows
        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()


# -----------------------------
# READ EMPLOYEE BY ID
# -----------------------------
def get_employee_by_id(emp_id: int):
    """
    Fetch a single employee record by emp_id.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        # Query employee by ID
        cursor.execute("SELECT * FROM employee_directory WHERE emp_id=%s", (emp_id,))
        result = cursor.fetchone()  # Fetch single row

        if not result:  # If no employee found
            raise HTTPException(status_code=404, detail="Employee not found")

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()


# -----------------------------
# UPDATE FULL EMPLOYEE RECORD
# -----------------------------
def update_employee_by_id(emp_id: int, emp: EmployeeDirectory):
    """
    Update all fields of an employee record by emp_id.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Check if employee exists
        cursor.execute("SELECT id FROM employee_directory WHERE emp_id=%s", (emp_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Employee not found")

        # SQL query to update employee record
        query = """
            UPDATE employees
            SET emp_code=%s, full_name=%s, email=%s, phone=%s,
                department=%s, location=%s, join_date=%s, status=%s
            WHERE id=%s
        """

        # Values tuple for update query
        values = (
            emp.emp_code, emp.full_name, emp.email, emp.phone,
            emp.department, emp.location, emp.join_date, emp.status, emp_id
        )

        cursor.execute(query, values)  # Execute update query
        conn.commit()  # Commit changes

        return {"message": "Employee updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()


# -----------------------------
# UPDATE EMPLOYEE STATUS ONLY
# -----------------------------
def update_employee_status(emp_id: int, new_status: str):
    """
    Update only the status field of an employee record.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Update query for status
        cursor.execute("UPDATE employee_directory SET status=%s WHERE emp_id=%s", (new_status, emp_id))
        conn.commit()

        if cursor.rowcount == 0:  # If no rows updated
            raise HTTPException(status_code=404, detail="Employee not found")

        return {"message": "Employee status updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()


# -----------------------------
# DELETE EMPLOYEE
# -----------------------------
def delete_employee(emp_id: int):
    """
    Delete an employee record by emp_id.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Delete query
        cursor.execute("DELETE FROM employee_directory WHERE emp_id=%s", (emp_id,))
        conn.commit()

        if cursor.rowcount == 0:  # If no rows deleted
            raise HTTPException(status_code=404, detail="Employee not found")

        return {"message": "Employee deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()


# -----------------------------
# SEARCH EMPLOYEES BY COLUMN
# -----------------------------
def search_employees(column_name: str, keyword: str):
    """
    Search employees by keyword in a specific column.
    Only allowed columns can be searched to prevent SQL injection.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Allowed columns for search
        allowed_columns = [
            "emp_code", "full_name", "email", "phone",
            "department", "location", "join_date", "status"
        ]

        if column_name not in allowed_columns:  # Validate column name
            raise ValueError("Invalid column name")

        # Build query dynamically with safe column name
        query = f"SELECT * FROM employee_directory WHERE {column_name} LIKE %s"
        cursor.execute(query, (f"%{keyword}%",))  # Use LIKE for partial match
        results = cursor.fetchall()
        return results

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# -----------------------------
# COUNT EMPLOYEES
# -----------------------------
def count_employees():
    """
    Count total number of employees in employee_directory.
    """
    return len(get_all_employee())  # Reuse get_all_employees function and return length
