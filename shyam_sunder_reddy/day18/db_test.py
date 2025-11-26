import pymysql

def get_connection():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
    )
    return conn

def read_all_employees():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM emp")
        data=cursor.fetchall()
        print("--------------ALL EMPLOYEES DATA----------------")
        for row in data:
            print(f"ID: {row[0]} | NAME: {row[1]} | SALARY: {row[2]}")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Connection closed Successfully!")
    
def read_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID= %s ",(emp_id,))
        row=cursor.fetchone()
        if row:
            print( f"ID: {row[0]} | NAME: {row[1]} | SALARY: {row[2]}")
            return True
        else:
            print("ID Not found")
            return False
    except Exception as e:
        print("ERROR: ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Connection closed Successfully!")
               
def create_employee(name,salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO ust_db.emp (EMP_NAME,SALARY) VALUES(%s,%s)",(name,salary))
        conn.commit()
        print("Employee record inserted successfully!")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Conection closed successfully!")
        
def  update_employee_by_id(emp_id,new_name,new_salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME=%s,SALARY=%s WHERE EMP_ID=%s",(new_name,new_salary,emp_id))
        conn.commit()
        print("EMployee record updated successfully!")
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Connection closed successfully")

def delete_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        if read_employee_by_id(emp_id):
            cursor.execute(" DELETE FROM ust_db.emp WHERE EMP_ID=%s",(emp_id,))
            conn.commit()
            print("Employee Record Deleted succesfully")
        else :
            print("ID NOT Exists to delete")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        if conn.open: #conn.is_connected
            cursor.close()
            conn.close()
       
        print("Connection closed successfully")

# read_all_employees()

# read_employee_by_id(2)

# read_all_employees()
# create_employee("ram",80000)
# read_all_employees()

# read_all_employees()
# update_employee_by_id(4,"VAMSHI",78000)
# read_employee_by_id(4)

read_all_employees()
delete_employee_by_id(5)
read_employee_by_id(5)