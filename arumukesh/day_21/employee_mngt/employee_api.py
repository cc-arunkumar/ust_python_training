from fastapi import FastAPI, APIRouter, HTTPException
from model import Employee
from db_connection import get_connection
from typing import List

# Creating router with base URL prefix
router = APIRouter(prefix="/employees")


# ----------- GET EMPLOYEE BY ID -----------
@router.get("/{id}")
def get_by_id(id: int):
    """
    Fetch a single employee record by ID from the database.
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # returns a dictionary instead of tuple
    cursor.execute("SELECT * FROM employee_table WHERE emp_id=%s", (id,))
    row = cursor.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return row


# ----------- CREATE EMPLOYEE -----------
@router.post("/")
def create_employee(emp: Employee):
    """
    Insert a new employee record into the database.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # SQL Query to insert data
        query = """
        INSERT INTO employee_db.employee_table
        (first_name, last_name, email, position, salary, hire_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        # emp.__dict__.values() extracts all values from the Pydantic model
        cursor.execute(query, tuple(emp.__dict__.values()))
        conn.commit()

        return {"message": "Employee details added successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while inserting: {str(e)}")


# ----------- UPDATE EMPLOYEE -----------
@router.put("/{id}")
def update_emp(id: int, emp: Employee):
    """
    Update an existing employee record by ID.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE employee_table
        SET first_name=%s, last_name=%s, email=%s, position=%s, salary=%s, hire_date=%s
        WHERE emp_id=%s
        """

        cursor.execute(query, tuple(emp.__dict__.values()) + (id,))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Employee not found")

        return {"message": "Employee details updated successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while updating: {str(e)}")


# ----------- DELETE EMPLOYEE -----------
@router.delete("/{id}")
def delete_router(id: int):
    """
    Delete an employee record by ID.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM employee_table WHERE emp_id=%s", (id,))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Employee not found")

        return {"message": "Employee deleted successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while deleting: {str(e)}")
