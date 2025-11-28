from src.models import employee_model
from src.config import db_connection
from typing import Optional

# Function: Create a new employee record in the database
def create_employee(new_employee: employee_model.Employee):
    # Insert a new employee into the employee_directory table
    try: 
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO ust_inventory_db.employee_directory (
                emp_code, full_name, email, phone,
                department, location, join_date, status
            ) VALUES (
                %s, %s, %s, %s,
                %s, %s, %s, %s
            )
        """
        # Prepare employee data for insertion
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
        return True
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection closed successfully")


# Function: Retrieve all employees, optionally filtered by status
def get_all_employees(status: Optional[str] = ""):
    # If status is empty, fetch all employees; otherwise filter by status
    try: 
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if status == "":
            cursor.execute("SELECT * FROM ust_inventory_db.employee_directory")
            data = cursor.fetchall()
            return data
        else:
            cursor.execute("SELECT * FROM ust_inventory_db.employee_directory WHERE status=%s", (status,))
            data = cursor.fetchall()
            return data
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Retrieve a single employee by ID
def get_employee_by_id(emp_id):
    # Query employee_directory table for a specific emp_id
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_inventory_db.employee_directory WHERE emp_id=%s", (emp_id,))
        data = cursor.fetchone()
        if data:
            return data
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()    


# Function: Update an existing employee by ID
def update_employee_by_id(emp_id: int, new_employee: employee_model.Employee):
    # Update employee record if it exists
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_employee_by_id(emp_id):
            query = """
                UPDATE ust_inventory_db.employee_directory
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
            # Prepare updated employee data
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
            return True
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Delete an employee by ID
def delete_employee_by_id(emp_id: int):
    # Remove employee record if it exists
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_employee_by_id(emp_id):
            cursor.execute("DELETE FROM ust_inventory_db.employee_directory WHERE emp_id=%s", (emp_id,))
            conn.commit()
            return True
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Search employees by a given field and value
def search_by_tag_employee(field, value):
    # Perform a LIKE query on the specified field
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        query = f"SELECT * FROM ust_inventory_db.employee_directory WHERE {field} LIKE %s"
        cursor.execute(query, (f"%{value}%",))
        data = cursor.fetchall()
        return data
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            

# Example usage (commented out for production):
# print(get_employee_by_id(8))
# print(get_all_employees())


# Function: Dump employee data from CSV into employee_directory table (commented out for production)
# def dump_employee_data():
#     conn = None
#     cursor = None
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         query = """
#             INSERT INTO ust_inventory_db.employee_directory (
#                 emp_code, full_name, email, phone,
#                 department, location, join_date, status
#             ) VALUES (
#                 %s, %s, %s, %s,
#                 %s, %s, %s, %s
#             )
#         """
#         with open("../database/sample_data/final_employee_directory.csv", "r", encoding="utf-8") as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 data = (
#                     row["emp_code"],
#                     row["full_name"],
#                     row["email"],
#                     row["phone"],
#                     row["department"],
#                     row["location"],
#                     row["join_date"],   
#                     row["status"]
#                 )
#                 cursor.execute(query, data)
#         conn.commit()
#         print("Inserted employee records successfully")
#     except Exception as e:
#         print("Error:", e)
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()
#         print("Connection closed successfully")

# dump_employee_data()
