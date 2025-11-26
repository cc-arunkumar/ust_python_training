import pymysql

def get_connection():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "pass@word1",
        database = "ust_db"
    )
    return conn

def read_all_employees():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM EMP;")
    rows = cursor.fetchall()
    for emp in rows:
        print(f"ID : {emp[0]}, NAME : {emp[1]}, SALARY : {emp[2]}")

def get_data_by_id(emp_id):
    try:
        
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID = %s", (emp_id, ))
        row = cursor.fetchone()
        if row:
            print("Employee with id = ", emp_id)
            print(f"ID : {row[0]}, NAME : {row[1]}, SALARY : {row[2]}")
        else:
            print("Employee details not found.")
    except ValueError as e:
        print("error : ", e)
def add_employee(name, salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO ust_db.emp (EMP_NAME, EMP_SALARY) VALUES (%s, %s)", (name, salary))
        conn.commit()
        print("Added successfully.")
    except Exception as e:
        print("Error is ", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Connection closed.")

def update_employee(emp_id, emp_name, emp_salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME = %s, EMP_SALARY = %s WHERE EMP_ID = %s", (emp_name, emp_salary, emp_id))
        conn.commit()
        print("Employee updated successfully.")
    except Exception as e:
        print("Error : ", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Connection Closed.")

def delete_employee(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        employee_to_be_deleted = input("Employee to be deleted : ")
        get_data_by_id(employee_to_be_deleted)
        if employee_to_be_deleted:
            cursor.execute("delete FROM ust_db.emp WHERE EMP_ID = %s", (employee_to_be_deleted, ))
            conn.commit()
            print("Employee Deleted successfully.")
        else:
            print("Employee record donot exist.")
    except Exception as e:
        print("Error : ", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Connection Closed.")


read_all_employees()
delete_employee(4)

