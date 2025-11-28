from src.config.db_connection import get_connection   # Import function to establish DB connection
from src.models.employee_model import EmployeeModel   # Import EmployeeModel definition


# ------------------- CREATE -------------------
def create_employee_db(employee: EmployeeModel):
    """
    Insert a new employee record into the database.
    - Accepts an EmployeeModel object.
    - Returns True if insertion is successful, False if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return False
    with conn.cursor() as cursor:
        sql = """INSERT INTO employee_directory 
                 (emp_code, full_name, email, phone, department, location, join_date, status)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        # Execute SQL insert with employee details
        cursor.execute(sql, (
            employee.emp_code,
            employee.full_name,
            employee.email,
            employee.phone,
            employee.department,
            employee.location,
            employee.join_date,
            employee.status
        ))
        conn.commit()  # Commit transaction
    conn.close()
    return True


# ------------------- SEARCH -------------------
def search_employees_db(keyword: str, value: str):
    """
    Search employees dynamically by a given column (keyword) and value.
    - Uses LIKE for partial matches.
    - Only allows specific safe columns to prevent SQL injection.
    - Returns list of matching employees or empty list if keyword invalid.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        like = f"%{value}%"
        allowed_columns = ["emp_id", "emp_code", "full_name", "email", "phone",
                           "department", "location", "join_date", "status"]
        # Validate keyword to prevent SQL injection
        if keyword not in allowed_columns:
            return []
        sql = f"SELECT * FROM employee_directory WHERE {keyword} LIKE %s"
        cursor.execute(sql, (like,))
        result = cursor.fetchall()
    conn.close()
    return result


# ------------------- READ ALL -------------------
def get_all_employees_db():
    """
    Retrieve all employees from the database.
    - Returns list of employees or None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM employee_directory")
        result = cursor.fetchall()
    conn.close()
    return result


# ------------------- LIST BY STATUS -------------------
def list_employees_by_status_db(status: str):
    """
    Retrieve all employees filtered by status (case-insensitive).
    - Returns list of employees or None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        sql = "SELECT * FROM employee_directory WHERE LOWER(status) = LOWER(%s)"
        cursor.execute(sql, (status,))
        result = cursor.fetchall()
    conn.close()
    return result


# ------------------- READ BY ID -------------------
def get_employee_by_id_db(emp_id: int):
    """
    Retrieve a single employee by ID.
    - Returns employee record or None if not found/DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM employee_directory WHERE emp_id = %s", (emp_id,))
        result = cursor.fetchone()
    conn.close()
    return result


# ------------------- UPDATE -------------------
def update_employee_db(emp_id: int, employee: EmployeeModel):
    """
    Update an existing employee record by ID.
    - Accepts EmployeeModel object with updated fields.
    - Returns True if update is successful, False if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return False
    with conn.cursor() as cursor:
        sql = """UPDATE employee_directory 
                 SET emp_code=%s, full_name=%s, email=%s, phone=%s, 
                     department=%s, location=%s, join_date=%s, status=%s
                 WHERE emp_id=%s"""
        cursor.execute(sql, (
            employee.emp_code,
            employee.full_name,
            employee.email,
            employee.phone,
            employee.department,
            employee.location,
            employee.join_date,
            employee.status,
            emp_id
        ))
        conn.commit()
    conn.close()
    return True


# ------------------- UPDATE STATUS -------------------
def update_employee_status_db(emp_id: int, status: str):
    """
    Update only the status of an employee by ID.
    - Returns True if update is successful, False if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return False
    with conn.cursor() as cursor:
        cursor.execute("UPDATE employee_directory SET status = %s WHERE emp_id = %s",
                       (status, emp_id))
        conn.commit()
        updated = cursor.rowcount  # Check number of rows updated
    conn.close()
    return updated > 0


# ------------------- DELETE -------------------
def delete_employee_db(emp_id: int):
    """
    Delete an employee record by ID.
    - Returns True if deletion is successful, False if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return False
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM employee_directory WHERE emp_id = %s", (emp_id,))
        conn.commit()
    conn.close()
    return True


# ------------------- COUNT -------------------
def count_employees_db():
    """
    Count total number of employees in the database.
    - Returns integer count or None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM employee_directory")
        result = cursor.fetchone()
    conn.close()
    return result
