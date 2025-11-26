import mysql.connector
from mysql.connector import Error

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"   
    )
    return conn

def read_all_employees():
    try:
        conn = get_connection()
        if conn is None:
            return
        cursor = conn.cursor()
    
        cursor.execute("SELECT * FROM EMP;")
        rows = cursor.fetchall()
        for emp in rows:
            print(f"ID : {emp[0]} | Name: {emp[1]} | Salary : {emp[2]}")
        
        print("Connection established successfully with database:", conn.database)
    except Error as e:
        print("Error:", e)
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection successfully closed")

def get_employee_by_id(emp_id):
    try:
        conn = get_connection()
        if conn is None:
            return
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID = %s", (emp_id,))
        row = cursor.fetchone()
        
        if row:
            print("Read employee data by id:")
            print(f"ID : {row[0]} | Name: {row[1]} | Salary : {row[2]}")
        else:
            print("Employee not found")
    except Error as e:
        print("Error:", e)
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed !!")

def create_employee(emp_id, name, salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO EMP (EMP_ID, EMP_NAME, EMP_SALARY) VALUES (%s, %s, %s)", (emp_id, name, salary))
        conn.commit()
        
        print(f"Employee created successfully: ID={emp_id}, Name={name}, Salary={salary}")
    except Error as e:
        print("Error while inserting employee:", e)
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed after insert !!")
        
def update_employee_by_id(emp_id, new_name, new_salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME = %s, EMP_SALARY = %s WHERE EMP_ID = %s", (new_name, new_salary, emp_id))
        conn.commit()
        
        print("Employee record has been updated successfully")
    except Exception as e:
        print("Exception:", e)
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
        print("Closed successfully")
        
def delete_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        emp_to_be_deleted=get_employee_by_id(emp_id)
        if emp_to_be_deleted!=None:
        
            cursor.execute("DELETE FROM EMP WHERE EMP_ID = %s", (emp_id,))
            conn.commit()

        else:
            print(f"No employee found with ID={emp_id}")
    except Error as e:
        print("Error while deleting employee:", e)
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed after delete !!")

        

read_all_employees()
create_employee(3, "Pihoo Mishra", 45000.9)
update_employee_by_id(3, "Deepu", 5000)
read_all_employees()
