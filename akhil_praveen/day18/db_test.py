import pymysql

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
        cursor.execute("select * from emp")
        rows = cursor.fetchall()
        for emp in rows:
            print(f"id: {emp[0]}|Name: {emp[1]} | Salary: {emp[2]}")
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection closed successfully!")
        
        
def read_employee_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("select * from emp where emp_id = %s",(emp_id,))
        row = cursor.fetchone()
        
        if row:
            print("Read employee data by id:", end="")
            print(f"id: {row[0]}|Name: {row[1]} | Salary: {row[2]}")
            return row
            
        else:
            print(f"Employee record not found for : {emp_id}")
            return None
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection closed successfully!")
            
def create_employee(name,salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO ust_db.emp (EMP_NAME,EMP_SALARY) VALUES (%s,%s)",(name,salary))
        conn.commit()
        print("Employee record inserted successfully!")
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection closed successfully!")
            
def update_employee_by_id(emp_id,name,salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME=%s,EMP_SALARY=%s WHERE EMP_ID=%s",(name,salary,emp_id))
        conn.commit()
        print("Employee record updated successfully!")
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection closed successfully!")
            
def delete_employee_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        record = read_employee_by_id(emp_id)
        if record:
            cursor.execute("delete from ust_db.emp WHERE EMP_ID=%s",(emp_id,))
            conn.commit()
            print("Employee record deleted successfully!")
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection closed successfully!")

# read_all_employees()
# read_employee_by_id(3)
# create_employee("Mr. Arjun",1281234.124)
# read_all_employees()
delete_employee_by_id(8)
read_all_employees()