import pymysql
 
def get_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
    )
    return conn
 
def read_all_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EMP;")
    rows = cursor.fetchall()
    print("\n--- All Employees ---")
    if rows:
        for emp in rows:
            print(f"ID: {emp[0]} | NAME: {emp[1]} | SALARY: {emp[2]}")
    else:
        print("No employees found.")
    print("\n--- End of Employee List ---")
 
def read_employee_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID = %s", (emp_id,))
        row = cursor.fetchone()
 
        if row:
            print(f"\n--- Employee Record (ID: {emp_id}) ---")
            print(f"ID: {row[0]} | NAME: {row[1]} | SALARY: {row[2]}")
            print("--- End of Employee Record ---")
        else:
            print(f"\nEmployee with ID {emp_id} not found.")
    except Exception as e:
        print("Error: ", e)
    finally:
        cursor.close()
        conn.close()
        print("\nConnection closed successfully.")
 
def create_employee(name, salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ust_db.emp(EMP_NAME, EMP_SALARY) VALUES (%s, %s)", (name, salary))
        conn.commit()
        print(f"\nEmployee '{name}' with salary {salary} has been added successfully.")
    except Exception as e:
        print("Error: ", e)
    finally:
        cursor.close()
        conn.close()
        print("\nConnection closed successfully!")
 
def update_employee_by_id(emp_id, new_name, new_salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME = %s, EMP_SALARY = %s WHERE EMP_ID = %s", (new_name, new_salary, emp_id))
        conn.commit()
 
        if cursor.rowcount > 0:
            print(f"\nEmployee with ID {emp_id} has been updated successfully to Name: {new_name}, Salary: {new_salary}.")
        else:
            print(f"\nNo employee found with ID {emp_id}.")
    except Exception as e:
        print("Exception: ", e)
    finally:
        cursor.close()
        conn.close()
        print("\nConnection closed successfully.")
 
def delete_employee_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID = %s", (emp_id,))
        conn.commit()
 
        if cursor.rowcount > 0:
            print(f"\nEmployee with ID {emp_id} has been deleted successfully.")
        else:
            print(f"\nNo employee found with ID {emp_id}.")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        cursor.close()
        conn.close()
        print("\nConnection closed successfully.")
 
# Example function calls to demonstrate sequence
print("\n=== Initial Employee List ===")
read_all_employees()
 
# create_employee("Yashwanth", 35000)
update_employee_by_id(2, "Deepu", 320000)
delete_employee_by_id(3)
read_employee_by_id(1)
 
print("\n=== Final Employee List ===")
read_all_employees()
 