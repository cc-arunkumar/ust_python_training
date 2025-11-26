import mysql.connector

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
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM EMP;")
        rows = cursor.fetchall()
        for emp in rows:
            print(f"ID: {emp[0]} | NAME: {emp[1]} | SALARY: {emp[2]}")
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed successfully")
            
def read_employee_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID = %s;",(emp_id,))
        row = cursor.fetchone()
        if row:
            print(f"Read employee data by id: ID: {row[0]} | NAME: {row[1]} | SALARY: {row[2]}")
            return row
        else:
            print("Employee record not found with emp_id ",emp_id)
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
        print("Employee record inserted successfully")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed successfully")
            
def update_employee_by_id(emp_id,new_name,new_salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME = %s,EMP_SALARY = %s WHERE EMP_ID = %s",(new_name,new_salary,emp_id))
        conn.commit()
        print("Employee updated successfully")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed successfully")
            
def delete_employee_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        employee_deleted = read_employee_by_id(emp_id)
        if employee_deleted:
            cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID = %s",(emp_id,))
            conn.commit()
            print("Employee deleted successfully")
        else:
            print("Employee record not found")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed successfully")
    


# read_all_employees()
# read_employee_by_id(2)
# read_all_employees()
# create_employee("Manu",55000)
# read_all_employees()
# read_all_employees()
# update_employee_by_id(5,"Hari",50000)
# read_employee_by_id(5)
delete_employee_by_id(4)
