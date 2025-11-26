
import pymysql

def get_connection():
    conn = pymysql.connect(
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
        print(f"ID:{emp[0]} | NAME:{emp[1]} |SALARY{emp[2]}")
    
read_all_employees()

def read_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID =%s",(emp_id,))
        row=cursor.fetchone()
        
        if row:
            print("read employee by id:",end="")
            print(f"ID:{row[0]} |NAME:{row[1]} | SALARY:{row[2]}")
            return row
        else:
            print(f"employee record not found for:{emp_id}")
            return None
    except Error as e:
        print("Error:",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("connection closed successfully")
        
read_employee_by_id(2)

def create_employee(name,salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("INSERT INTO ust_db.emp(EMP_NAME, EMP_SALARY)VALUES(%s,%s)",(name,salary))
        conn.commit()
        print("employee record inserted")
        
    except Exception as e:
        print("Error:",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("connection closed")
create_employee("rash",2000000)
read_all_employees()

def update_employee_by_id(emp_id,new_name,new_salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME =%s,EMP_SALARY=%s WHERE EMP_ID= %s",(new_name,new_salary,emp_id))
        conn.commit()
        
        print("employee record updated")
    except Exception as e:
        print("Exception",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("connection closed")
        
read_all_employees()
update_employee_by_id(2,"rashiii",6000000)
read_employee_by_id(2)

def delete_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        to_del = read_employee_by_id(emp_id)
        if to_del:
        
            cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID =%s",(emp_id))
            conn.commit()
            
            print("employee record deleted")
        else:
            print("employee not found")
    except Exception as e:
        print("Exception",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("connection closed")
        
read_all_employees()
delete_employee_by_id(4)




# sample output
# ID:1 | NAME:AKSHHH |SALARY25000.0
# ID:2 | NAME:rashiii |SALARY6000000.0
# ID:3 | NAME:rash |SALARY2000000.0
# read employee by id:ID:2 |NAME:rashiii | SALARY:6000000.0
# connection closed successfully
# employee record inserted
# connection closed
# ID:1 | NAME:AKSHHH |SALARY25000.0
# ID:2 | NAME:rashiii |SALARY6000000.0
# ID:3 | NAME:rash |SALARY2000000.0
# ID:5 | NAME:rash |SALARY2000000.0
# ID:1 | NAME:AKSHHH |SALARY25000.0
# ID:2 | NAME:rashiii |SALARY6000000.0
# ID:3 | NAME:rash |SALARY2000000.0
# ID:5 | NAME:rash |SALARY2000000.0
# employee record updated
# connection closed
# read employee by id:ID:2 |NAME:rashiii | SALARY:6000000.0
# connection closed successfully
# ID:1 | NAME:AKSHHH |SALARY25000.0
# ID:2 | NAME:rashiii |SALARY6000000.0
# ID:3 | NAME:rash |SALARY2000000.0
# ID:5 | NAME:rash |SALARY2000000.0
# employee record not found for:4
# connection closed successfully
# employee not found
# connection closed