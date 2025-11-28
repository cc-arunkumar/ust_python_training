import mysql.connector
from mysql.connector import Error

def get_Connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
    )
    return conn

def get_all_employees():
    try:
        conn = get_Connection()
        print("Connection established")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM EMP")
        rows = cursor.fetchall()
        for emp in rows:
            print(f"ID: {emp[0]} | Name: {emp[1]} | Salary: {emp[2]}")
    except Error as e:
        print("Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed Successfully")

def read_employee_by_id(emp_id):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID = %s", (emp_id,))
        row = cursor.fetchone()
        if row:
            return f"ID: {row[0]} | Name: {row[1]} | Salary: {row[2]}"
        else:
            return f"Employee record not found for: {emp_id}"
    except Error as e:
        print("Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed Successfully")


def create_employee(name,salary):
    try:
        conn=get_Connection()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO ust_db.emp(EMP_NAME,EMP_SALARY) VALUES (%s,%s)",(name,salary))
        conn.commit()
        print("Employee record inserted successfully:")
    except Error as e:
        print("Error",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")
        
        
def update_employee_by_id(empid,new_name,new_salary):
    try:
        conn=get_Connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME=%s,EMP_SALARY=%s WHERE EMP_ID=%s",(new_name,new_salary,empid))
        conn.commit()
        print("Employee record updated successfully")
    except Error as e:
        print("Error",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")
        
        
        
def delete_employee_by_id(empid):
    try:
        conn=get_Connection()
        cursor=conn.cursor()    
        employee_to_be_deleted=read_employee_by_id(empid)
        print(employee_to_be_deleted)
        cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID=%s",(empid,))
        conn.commit()
        print("Employee record deleeted successfully")
    except Error as e:
        print("Error",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()        

# Run functions
get_all_employees()
# read_employee_by_id(2)
# create_employee("RITIKANAYAK","500000")
# get_all_employees()
# update_employee_by_id(3,"RITIKA","89000")
delete_employee_by_id(4)
get_all_employees()

