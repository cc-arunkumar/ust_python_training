import pymysql
from pymysql import Error

def get_connection():
    conn = pymysql.connect(
        host="localhost",
        user = "root",
        password = "pass@word1",
        database = "ust_db"
    )
    return conn

def read_all_employees():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("Select * from emp")
        data = cursor.fetchall()
        for emp in data:
            print(f'ID: {emp[0]} | Name: {emp[1]} | Salary: {emp[2]}')
        
    except Error as e:
        print("Error:",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection Closed Successfully!")

def read_emp_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID = %s",(emp_id))
        row = cursor.fetchone()
        if row:
            print(row)
        else:
            return "Employee ID Not Found"
        
    except Error as e:
        print("Error:",e)
        
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection Closed Successfully!")

def create_employee(name,salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ust_db.emp (EMP_NAME,EMP_SALARY) VALUES (%s,%s)",(name,salary))
        conn.commit()
    except Error as e:
        print('Error:',e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection Closed Successfully!")    

def update_employee(id,name,salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME= %s, EMP_SALARY = %s WHERE EMP_ID = %s",(name,salary,id))
        conn.commit()
        print("Employee Record Updated Successfully!")
    except Error as e:
        print('Error:',e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection Closed Successfully!")
    
def delete_employee(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if not read_emp_by_id(emp_id):
            print("Employee ID Not Exist")
        else:
            cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID = %s",(emp_id))
            conn.commit()
            print("Employee Record Deleted Successfully!")
    except Error as e:
        print('Error:',e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection Closed Successfully!")
    

# read_all_employees()
# read_emp_by_id(1)
# create_employee('Yeshwanth',45000000)
# read_all_employees()
# update_employee(4,'Yeshwanth',30000)
delete_employee(4)
# read_emp_by_id(4)