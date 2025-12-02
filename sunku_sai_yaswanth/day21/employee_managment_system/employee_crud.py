from db_connection import get_connection
from employee_model import Employee


# Retrieve all employee records from the database
def read_all_employees():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("Select * from ust_db.employees")
        data = cursor.fetchall()
        return data
    
    except Exception as e:
        raise ValueError(f"Error: {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()

# Retrieve a single employee record by its ID
def read_emp_by_id(employee_id : int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_db.employees WHERE employee_id = %s", (employee_id,))
        row = cursor.fetchone()
        if row:
            return row
        else:
            raise ValueError("Employee ID Not Found")
        
    except Exception as e:
        raise ValueError(f"Error: {e}")
        
    finally:
        if conn:
            cursor.close()
            conn.close()

# Insert a new employee record into the database
def create_employee_crud(new_employee : Employee):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO ust_db.employees
                (first_name, last_name, email, position, salary, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                new_employee.first_name,
                new_employee.last_name,
                new_employee.email,
                new_employee.position,
                new_employee.salary,
                new_employee.hire_date,
            ),
        )
        conn.commit()
    except Exception as e:
        raise ValueError(f"Error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

# Update an existing employee record identified by ID
def update_employee_crud(employee_id,updated_emp : Employee):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE ust_db.employees
               SET first_name = %s,
                   last_name = %s,
                   email = %s,
                   position = %s,
                   salary = %s,
                   hire_date = %s
               WHERE employee_id = %s
            """,
            (
                updated_emp.first_name,
                updated_emp.last_name,
                updated_emp.email,
                updated_emp.position,
                updated_emp.salary,
                updated_emp.hire_date,
                employee_id,
            ),
        )
        conn.commit()

    except Exception as e:
        raise ValueError(f"Error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
    
# Delete an employee record by its ID
def delete_employee_by_id(emp_id: int):

    try:
        conn = get_connection()
        cursor = conn.cursor()
        if read_emp_by_id(emp_id):
            cursor.execute(
                "DELETE FROM ust_db.employees WHERE employee_id=%s",
                (emp_id,)
            )
            conn.commit()
            return True
        else:
            raise ValueError("Employee not found")
    except Exception as e:
        raise ValueError(f"ERROR: {e}")
    finally:
        if conn:
            try:
                cursor.close()
            except Exception:
                pass
            try:
                conn.close()
            except Exception:
                pass
    
