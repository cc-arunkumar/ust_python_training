import mysql.connector
def get_connection():
    
    conn=mysql.connector.connect(
    host="localhost",
    username="root",
    password="pass@word1",
    database="ust_db"
    )
    return conn
def read_all_employees():
    conn=get_connection()
    # print("connection established")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM EMP;")
    rows=cursor.fetchall()
    for emp in rows:
        print(f"ID: {emp[0]} | NAME: {emp[1]} | SALARY: {emp[2]}")
        
        
def read_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM emp WHERE EMP_ID = %s;", (emp_id,))
        row=cursor.fetchone()
        
        if row:
            print("read employees data by id: ",end="")
            print(f"ID: {row[0]} | NAME: {row[1]} | SALARY: {row[2]}")
            return row
            
        else:
            print(f"employee record not found for: {emp_id}")
            
    except Exception as e:
        print("Error: ",e)
        
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("connection closed successfully") 
        
        
def create_employee(name,salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO ust_db.emp (EMP_NAME,EMP_SALARY) VALUES(%s,%s)",(name,salary))
        conn.commit()
        print("Employees record inserted successfully")
        
    except Exception as e:
        print("Error :",e)
        
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            
        print("connection closed")    
        
        
        
        
def update_employee_by_id(emp_id,new_name,new_salary):
    try:
        
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME=%s, EMP_SALARY=%s WHERE EMP_ID=%s",(new_name,new_salary,emp_id))
        conn.commit()
        print("Employees record has been updated successfully")
        
    except Exception as e:
        print("Exception: ",e)
        
    finally:
        conn.is_connected()
        cursor.close()
        conn.close()
        print("connection closed")  
        
        
def delete_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        emp_to_be_deleted=read_employee_by_id(emp_id)
        
        if emp_to_be_deleted != None:
            cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID=%s",(emp_id, ))
            conn.commit()
            print("Employee has been deleted ")
            
    except Exception as e:
        print("Exception",e)
        
    finally:
        conn.is_connected()
        cursor.close()
        conn.close()
        print("connection closed")
        
read_all_employees()
delete_employee_by_id(2)
read_employee_by_id(3)

