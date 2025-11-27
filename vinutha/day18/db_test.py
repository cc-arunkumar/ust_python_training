# import mysql.connector

# conn=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='pass@word1',
#     database='ust_db'
    
# )

# print("Connection established successfully with MySql DB:",conn)

# conn.close()
# print("-->Connection closed <---")


import mysql.connector
from mysql.connector import Error
def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
    )
    return conn

def read_all_employees():
    conn=get_connection()
    cursor=conn.cursor()
    
    cursor.execute("SELECT * FROM EMP;")
    rows=cursor.fetchall()
    for emp in rows:
        print(f"ID:{emp[0]} | Name:{emp[1]} | SALARY:{emp[2]}")

# read_all_employees() 

def read_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID=%s",(emp_id, ))
        row=cursor.fetchone()
        
        if row:
            print("Read employee data by id:",end="")
            print(f"ID:{row[0]} | Name:{row[1]} | SALARY:{row[2]}")
        else:
            print(f"Employee record not found for:{emp_id}")
    except Error as e:
        print("Error:",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed succuss!")
read_employee_by_id(2)


def create_employee(name,salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("INSERT INTO ust_db.emp(EMP_NAME,EMP_SALARY) VALUES(%s,%s)",(name,salary))
        conn.commit()
        print("Employee record inserted successfully!")
    except Error as e:
        print("Error:",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection close")

# read_all_employees()         
# create_employee("siri",50000.5)
# read_all_employees() 

def update_employee_by_id(emp_id,new_name,new_salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME=%s, EMP_SALARY=%s WHERE EMP_ID=%s",(new_name,new_salary,emp_id))
        conn.commit()
        print("EMployee record has been updated successfully")
    except Error as e:
        print("Error:",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed!")
# update_employee_by_id(4,"chakitha",30500.0)
# read_all_employees() 

def delete_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID=%s",(emp_id,))
        conn.commit()
        print("EMployee record has been delete successfully")
    except Error as e:
        print("Error:",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed!")
deleted=delete_employee_by_id(4)
print(deleted)
read_all_employees()


