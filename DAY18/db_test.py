import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "pass@word1",
        database = "ust_db"
    )
    return conn

def read_all_employee():
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM EMP;")
    rows = cursor.fetchall()
    print("----------")
    for emp in rows:
        print(f"ID : {emp[0]} | Name : {emp[1]} | salary : {emp[2]}")
        
# read_all_employee()

def read_employee_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID = %s",(emp_id, ))
        
        row = cursor.fetchone()
        
        if row:
            print("Read Employee Data by ID:",end="")
            print(f"ID : {row[0]} | Name : {row[1]} | salary : {row[2]}")
            return row
        else:
            print(f"Employee record not found for{emp_id}")
            return None
            
    except Exception as e:
        print("ERROR :",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection added successfully !")
            
            
def create_employee(name,salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO ust_db.emp (EMP_NAME,salary) VALUES (%s,%s) ",(name,salary))
        conn.commit()
        print("Employee Record Inserted Successfully")
    except Exception as e:
        print("Error",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed successfully")
        
def update_employee_by_id(emp_id,new_name,new_salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME = %s ,salary = %s WHERE EMP_ID = %s", (new_name,new_salary,emp_id))
        conn.commit()
        print("Employee Record Updated Successfully")
    except Exception as e:
        print("Error",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed successfully")
        

def delete_emp_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        emp_to_be_deleted = read_employee_id(emp_id)
        
        if emp_to_be_deleted != None:
            cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID = %s",(emp_id, ))
            conn.commit()
            print("Employee Record Deleted Successfully")
        else:
            print("Employee record not found!")
            
    except Exception as e:
        print("Error",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed successfully")
        
                
            
# read_employee_id(28)  
# read_all_employee()
# create_employee("pooja edge",25)

# read_all_employee()
# update_employee_by_id(32,"Monica",20)
# read_all_employee()

read_all_employee()
delete_emp_by_id(31)
read_employee_id(31)

  

        