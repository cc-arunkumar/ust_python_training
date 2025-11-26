import pymysql

# conn=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='pass@word1',
#     database='ust_db'
    
# )

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
            print(f"ID:{emp[0]} | NAME:{emp[1]} | SALARY:{emp[2]}")
    except Exception as e:
        print("Rows not found")
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection closed successfully")
 
def read_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID = %s",(emp_id,))
        row=cursor.fetchone()
        
        if row:
            print("Read employee data by id : ",end="")
            print(f"ID:{row[0]} | NAME:{row[1]} | SALARY:{row[2]}")
            return row #for delete operation
        else:
            print(f"Employee record not found for: {emp_id}")
            return None #for delete operation
        
    except Exception as e:
        print("Error:",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection closed successfully")
        
def create_employee(name,salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("INSERT INTO ust_db.emp(EMP_NAME,EMP_SALARY) VALUES (%s,%s)",(name,salary))
        conn.commit()
        print("Employee record inserted successfully!")
    except Exception as e:
        print("Error: ",e)
        
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Conection closed!")
        
def update_employee_by_id(emp_id,new_name,new_salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME=%s,EMP_SALARY=%s WHERE EMP_ID=%s",(new_name,new_salary,emp_id))
        conn.commit()
        
        print("Employee record has been updated successfully!")
    except Exception as e:
        print("Exception: ",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection closed successfully!")
            
def delete_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        to_be_deleted=read_employee_by_id(emp_id)
        if to_be_deleted:
            cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID=%s",(emp_id))
            conn.commit()
        
        print("Employee record deleted successfully")
    except Exception as e:
        print("Error:",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection closed successfully!")

        

    
       
# read_all_employees()
# # create_employee("Deepika","3400.35")
# read_all_employees()
# read_all_employees()
# update_employee_by_id(4,"Raahul","45000")
read_employee_by_id(3)
delete_employee_by_id(3)
read_all_employees()
