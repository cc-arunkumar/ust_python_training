from src.config import db_connection
from src.models import employee_model
from typing import Optional

# Create a new employee record
def create_employee(new_employee: employee_model.EmployeeDirectory):

    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO ust_asset_db.employee_directory (
                emp_code, full_name, email, phone,
                department, location, join_date, status
            ) VALUES (
                %s, %s, %s, %s,
                %s, %s, %s, %s
            )
        """
        data = (
            new_employee.emp_code,
            new_employee.full_name,
            new_employee.email,
            new_employee.phone,
            new_employee.department,
            new_employee.location,
            new_employee.join_date,
            new_employee.status
        )
        cursor.execute(query, data)
        conn.commit()
    except Exception as e:
        raise ValueError("Error: ", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Retrieve all employees (optionally filter by status)
def get_all_employees(status: Optional[str] = ""):

    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if status == "":
            cursor.execute("SELECT * FROM ust_asset_db.employee_directory")
            data = cursor.fetchall()
            return data
        else:
            cursor.execute(
                "SELECT * FROM ust_asset_db.employee_directory WHERE status = %s",
                (status,)
            )
            data = cursor.fetchall()
            return data
    except Exception as e:
        raise Exception(f"Error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Search employees by field and keyword
def search_employee(field_type: str, keyword: str):

    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM ust_asset_db.employee_directory WHERE {field_type} LIKE %s",
            (f'%{keyword}%',)
        )
        data = cursor.fetchall()
        return data
    except Exception as e:
        raise Exception(f"Error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Get employee by ID
def get_employee_by_id(emp_id):
    """
    Retrieve a single employee by their ID.
    Parameters:
        emp_id (int): Unique identifier of the employee.
    Returns:
        Single employee record or None if not found.
    Raises:
        Exception: If query fails.
    """
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM ust_asset_db.employee_directory WHERE emp_id=%s",
            (emp_id,)
        )
        data = cursor.fetchone()
        return data
    except Exception as e:
        raise Exception(f"Error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Update employee by ID
def update_asset_by_id(emp_id: int, new_employee: employee_model.EmployeeDirectory):

    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_employee_by_id(emp_id):
            query = """
                UPDATE ust_asset_db.employee_directory
                SET emp_code = %s,
                    full_name = %s,
                    email = %s,
                    phone = %s,
                    department = %s,
                    location = %s,
                    join_date = %s,
                    status = %s
                WHERE emp_id = %s
            """
            data = (
                new_employee.emp_code,
                new_employee.full_name,
                new_employee.email,
                new_employee.phone,
                new_employee.department,
                new_employee.location,
                new_employee.join_date,
                new_employee.status,
                emp_id
            )
            cursor.execute(query, data)
            conn.commit()
        else:
            raise ValueError("Employee not found")
    except Exception as e:
        raise ValueError("Error:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Delete employee by ID
def delete_employee_by_id(emp_id: int):

    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_employee_by_id(emp_id):
            cursor.execute(
                "DELETE FROM ust_asset_db.employee_directory WHERE emp_id=%s",
                (emp_id,)
            )
            conn.commit()
            return True
        else:
            raise ValueError("Employee not found")
    except Exception as e:
        raise ValueError("ERROR:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
