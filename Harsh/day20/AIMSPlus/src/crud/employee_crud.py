from typing import List
from src.config.db_connection import get_connection
from src.models.employee_model import EmployeeDirectory
from fastapi import HTTPException

# CREATE a new employee
def create_employee(emp: EmployeeDirectory):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO employee_directory
            (emp_code, full_name, email, phone, department, location, join_date, status)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            emp.emp_code, emp.full_name, emp.email, emp.phone,
            emp.department, emp.location, emp.join_date, emp.status
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Employee created successfully", "employee_id": cursor.lastrowid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# READ all employees (optional status filter)
def get_all_employees(status: str | None = None):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if status:
            cursor.execute("SELECT * FROM employee_directory WHERE status=%s", (status,))
        else:
            cursor.execute("SELECT * FROM employee_directory")
        results = cursor.fetchall()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# READ employee by ID
def get_employee_by_id(emp_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employee_directory WHERE emp_id=%s", (emp_id,))
        result = cursor.fetchone()
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# UPDATE full employee record
def update_employee_by_id(emp_id: int, emp: EmployeeDirectory):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT emp_id FROM employee_directory WHERE emp_id=%s", (emp_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Employee not found")

        query = """
            UPDATE employees
            SET emp_code=%s, full_name=%s, email=%s, phone=%s,
                department=%s, location=%s, join_date=%s, status=%s
            WHERE id=%s
        """
        values = (
            emp.emp_code, emp.full_name, emp.email, emp.phone,
            emp.department, emp.location, emp.join_date, emp.status, emp_id
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Employee updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# UPDATE employee status only
def update_employee_status(emp_id: int, new_status: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE employee_directory SET status=%s WHERE emp_id=%s", (new_status, emp_id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Employee not found")
        return {"message": "Employee status updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# DELETE employee by ID
def delete_employee(emp_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employee_directory WHERE emp_id=%s", (emp_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Employee not found")
        return {"message": "Employee deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# SEARCH employees by column and keyword
def search_employees(column_name: str, keyword: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        allowed_columns = [
            "emp_code", "full_name", "email", "phone",
            "department", "location", "join_date", "status"
        ]

        if column_name not in allowed_columns:
            raise ValueError("Invalid column name")

        query = f"SELECT * FROM employee_directory WHERE {column_name} LIKE %s"
        cursor.execute(query, (f"%{keyword}%",))
        results = cursor.fetchall()
        return results

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# COUNT total employees
def count_employee():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM employee_directory")
        result = cursor.fetchone()
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

