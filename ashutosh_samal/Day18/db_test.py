import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "pass@word1",
        database = "ust_db"
    )
    return conn

def read_all_employees():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM EMP;")
        rows = cursor.fetchall()
        for emp in rows:
            print(f"ID: {emp[0]} | Name: {emp[1]} | Salary: {emp[2]}")
    
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed successfully")


def read_emp_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID = %s",(emp_id, ))
        row = cursor.fetchone()
        
        if row:
            print(f"ID: {row[0]} | Name: {row[1]} | Salary: {row[2]}")
        else:
            print(f"Employee record not found for: {emp_id}")
        
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed successfully")
        
def create_employee(name,salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO ust_db.emp (EMP_NAME,EMP_SALARY) VALUES (%s,%s)",(name,salary))
        conn.commit()
        print("Employee  inserted successfully")
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")

def update_emp_by_id(emp_id,new_name,new_salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME = %s, EMP_SALARY = %s WHERE EMP_ID = %s",(new_name,new_salary,emp_id))
        conn.commit()
        print("Employee details updated")
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed successfully")

def delete_emp_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID = %s",(emp_id, ))
        conn.commit()
        print("Employee id deleted")
    except Exception as e:
        print("Exception: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection is closed")

# read_all_employees()
# read_emp_by_id(2)
# create_employee("Sohan",32000)
# update_emp_by_id(3,"Deepu",5000)
# read_emp_by_id(3)
delete_emp_by_id(3)
read_all_employees()
