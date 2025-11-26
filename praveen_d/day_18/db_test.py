import pymysql 
from pymysql import Error

def get_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
)
    return conn

def read_all_employee():
    try:
        conn=get_connection()
        print("Connected")
        cursor=conn.cursor()
        
        cursor.execute("SELECT*FROM EMP")
        rows=cursor.fetchall()
        for emp in rows:
            print(f"ID:{emp[0]} | NAME:{emp[1]} | SALARY:{emp[2]}")
    except Error as e:
        print("Error",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection closed sucessfully")



def read_emp_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID = %s",(emp_id,))
        row=cursor.fetchone()
        
        if row:
            print(f"ID:{row[0]} | NAME:{row[1]} | SALARY:{row[2]}")
            return row
        else:
            print("Employee id is not matched")
    except Error as e:
        print("Error",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection closed sucessfully")
            
def insert_employee(name,salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()         
        
        cursor.execute("INSERT INTO ust_db.emp (EMP_NAME,EMP_SALARY) VALUES (%s,%s)",(name,salary))
        conn.commit()
        print("Added sucessfully")
    except Error as e:
        print("Error",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection closed sucessfully")
      
      
      
def update_employee(emp_id,new_name,new_salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("""UPDATE ust_db.emp SET EMP_NAME=%s, EMP_SALARY=%s 
                       WHERE EMP_ID=%s""",(new_name,new_salary,emp_id))
        conn.commit()
        print("------------Updated sucessfully----------------------")

    except Exception as e:
        print("Exception",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()

def delete_employee_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        emp_to_be_deleted=read_emp_by_id(emp_id)
        
        if emp_to_be_deleted:
            cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID=%s",(emp_id,))
            conn.commit()
            print("Employee data has been deleted",emp_id)
    except Exception as e:
        print("Exception",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        
            
            
# read_emp_by_id(1)
        
# read_all_employee()      
# insert_employee("samantha",30000)
# read_all_employee()

read_all_employee()
# update_employee(5,"samantha",3000)
delete_employee_id(2)
read_all_employee()