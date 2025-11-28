# src/crud/employee_crud.py
from src.config.db_connection import get_connection

def create_employee(emp_code, full_name, email, phone, department, location, join_date, status="Active"):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Check duplicate emp_code
        cursor.execute("SELECT 1 FROM employee_directory WHERE emp_code = %s", (emp_code,))
        if cursor.fetchone():
            return {"error": "Employee code already exists!"}

        # Check duplicate email
        cursor.execute("SELECT 1 FROM employee_directory WHERE email = %s", (email,))
        if cursor.fetchone():
            return {"error": "Email already exists!"}

        query = """
        INSERT INTO employee_directory
        (emp_code, full_name, email, phone, department, location, join_date, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (emp_code, full_name, email, phone, department, location, join_date, status))
        conn.commit()
        return {"message": f"Employee created successfully! Code: {emp_code}"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()


def get_all_employees(status_filter="ALL"):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if status_filter == "ALL":
            cursor.execute("SELECT * FROM employee_directory ORDER BY emp_id")
        else:
            cursor.execute("SELECT * FROM employee_directory WHERE status = %s ORDER BY emp_id", (status_filter,))
        rows = cursor.fetchall()
        if rows:
            return {"employees": rows}
        else:
            return {"message": "No employees found"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()


def get_employee_by_id(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM employee_directory WHERE emp_id = %s", (emp_id,))
        row = cursor.fetchone()
        if row:
            return {"employee": row}
        else:
            return {"message": "Employee not found"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()


def update_employee(emp_id, emp_code, full_name, email, phone, department, location, join_date, status):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
        UPDATE employee_directory SET
        emp_code=%s, full_name=%s, email=%s, phone=%s,
        department=%s, location=%s, join_date=%s, status=%s
        WHERE emp_id=%s
        """
        cursor.execute(query, (emp_code, full_name, email, phone, department, location, join_date, status, emp_id))
        conn.commit()
        if cursor.rowcount > 0:
            return {"message": "Employee updated successfully!"}
        else:
            return {"message": "Employee not found"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()


def update_status_only(emp_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE employee_directory SET status=%s WHERE emp_id=%s", (new_status, emp_id))
        conn.commit()
        if cursor.rowcount > 0:
            return {"message": f"Status updated to '{new_status}'"}
        else:
            return {"message": "Employee not found"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()


def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM employee_directory WHERE emp_id=%s", (emp_id,))
        conn.commit()
        if cursor.rowcount > 0:
            return {"message": "Employee deleted successfully!"}
        else:
            return {"message": "Employee not found"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()


def search_employees(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        like = f"%{keyword}%"
        query = """
        SELECT * FROM employee_directory
        WHERE full_name LIKE %s OR emp_code LIKE %s OR email LIKE %s OR phone LIKE %s
        """
        cursor.execute(query, (like, like, like, like))
        rows = cursor.fetchall()
        if rows:
            return {"search_results": rows}
        else:
            return {"message": f"No employees found for keyword: {keyword}"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()


def count_employees():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM employee_directory")
        count = cursor.fetchone()[0]
        return {"total_employees": count}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()