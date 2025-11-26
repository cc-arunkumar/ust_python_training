import pymysql

def get_connection():
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='pass@word1',
        database='ust_db'
    )
    return conn
def read_all_employees():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM EMP;")
        rows=cursor.fetchall()
        for emp in rows:
            print(f"ID :{emp[0]} | NAME :{emp[1]} | SALARY :{emp[2]}")
    except Error as e:
        print("Error :",e)
    finally:
        # if conn.is_connected():
        cursor.close()
        conn.close()
        print("the connection is closed successfully")

def read_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID= %s",(emp_id, ))
        row=cursor.fetchone()
        
        if row:
            print("read employee data by id",end=" ")
            print(f"ID :{row[0]} | NAME :{row[1]} | SALARY :{row[2]}")
            return row
        else:
            print("the employee is not found for:",{emp_id})
            return None
    except Error as e:
        print("Error :",e)
    finally:
        # if conn.is_connected():
        cursor.close()
        conn.close()
        print("The connection is closed")
        
        
        
        
def create_employee(name,salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO ust_db.emp (EMP_NAME,EMP_SALARY) VALUES (%s,%s)",(name, salary))
        conn.commit()
        print("Employee record inserted successfully")
    except Exception as e:
        print("Error:",e)
    finally:
        cursor.close()
        conn.close()
        print("connection closed")
        
def update_employee_id(emp_id,new_name,new_salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME=%s ,EMP_SALARY=%s WHERE EMP_ID= %s",(new_name, new_salary, emp_id))
        conn.commit()
        print("employee record has been updated successfully")
    except Exception as e:
        print("Error :",e)
    finally:
        cursor.close()
        conn.close()
        print("Connection closed")
        
        
def delete_employee(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        employee_to_be_deleted=read_employee_by_id(emp_id)
        if employee_to_be_deleted:
            cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID=%s",(emp_id, ))
            conn.commit()
            print("Employee record deleted successfully")
        else:
            print("employee not found")
    except Exception as e:
        print("Error:",e)
    finally:
        cursor.close()
        conn.close()
        print("connection closed")
        

        

    
read_all_employees()
# create_employee('pramod',28000)
delete_employee(4)
read_employee_by_id(4)










# conn=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='pass@word1',
#     database='ust_db'
# )
# print("connnection established successfully with MySQL DB",conn)
# conn.close
# print("-----connection closed")