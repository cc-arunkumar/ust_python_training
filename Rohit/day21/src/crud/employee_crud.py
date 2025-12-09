from src.config.db_connection import get_connection
from src.models.employee_pydentic import Employee_pydentic

from fastapi import HTTPException
import pymysql


def create_emp(emp: Employee_pydentic):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO employees
        (first_name, last_name, email, position, salary, hire_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            emp.first_name, emp.last_name, emp.email, emp.position,
            emp.salary, emp.hire_date
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Employee created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def get_all_employees():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM employees"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Can't get employees: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def get_employee_by_id(emp_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM employees WHERE emp_id=%s"
        cursor.execute(query, (emp_id,))
        employee = cursor.fetchone()

        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")

        return employee
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def update_employee_by_id(emp_id: int, emp: Employee_pydentic):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Check if employee exists
        cursor.execute("SELECT emp_id FROM employees WHERE emp_id=%s", (emp_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Employee not found")

        query = """
        UPDATE employees 
        SET first_name=%s, last_name=%s, email=%s, position=%s, salary=%s, hire_date=%s
        WHERE emp_id=%s
        """
        values = (
            emp.first_name, emp.last_name, emp.email, emp.position,
            emp.salary, emp.hire_date, emp_id
        )
        cursor.execute(query, values)
        conn.commit()

        return {"message": "Employee updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def delete_employee(emp_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Employee not found")

        return {"message": "Employee deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
