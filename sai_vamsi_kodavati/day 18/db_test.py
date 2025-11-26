import pymysql

def get_connection():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "pass@word1",
        database = "ust_db"
    )
    
    return conn

def read_all_employees():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM EMP;")
    rows = cursor.fetchall()
    for emp in rows:
        print(f"ID: {emp[0]} | NAME: {emp[1]} | SALARY: {emp[2]}")
    


def read_employee_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID = %s",(emp_id, ))
        rows = cursor.fetchone()
        
        if rows:
            print("Read employee data by id : ",end = "")
            print(f"ID: {rows[0]} | NAME: {rows[1]} | SALARY: {rows[2]}")
        else:
            print(f"Employee record not found for: {emp_id}")
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")
           
# read_employee_by_id(2)


def create_employee(name,salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO ust_db.emp(EMP_NAME,EMP_SALARY) VALUES (%s,%s)",(name,salary))
        conn.commit()
        print("Employee record inserted successfully !")
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully!")
    
    
def update_employee_by_id(emp_id,new_name,new_salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME = %s,EMP_SALARY = %s WHERE EMP_ID = %s",(new_name,new_salary,emp_id))
        conn.commit()
        
        print("Employee record has been updated successfully")
    except Exception as e:
        print("Exception: ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")


def delete_employee_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        emp_to_be_deleted = read_employee_by_id(emp_id)
        
        if emp_to_be_deleted != None:
            cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID = %s",(emp_id))
            conn.commit()
            
            print("Employee id deleted successfully")
        else:
            print("Employee has been deleted successfully")
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully!")
    
read_all_employees()
delete_employee_by_id(2)
read_all_employees()
    
# read_all_employees()
# # create_employee("Yashwanth",35000)
# update_employee_by_id(3,"Yashu",32000)
# read_employee_by_id(3)








































# conn = pymysql.connect(
# host = "localhost",
# user = "root",
# password = "pass@word1",
# database = "ust_db"
# )

# print("Connection established successfully with MySQl DB:",conn)
# conn.close()
# print("---> Connection Closed<---")


