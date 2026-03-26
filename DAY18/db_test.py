import mysql.connector

def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
    )
    return conn

def read_all_employees():
    try:
        conn=get_connection()
        print("Conection Established")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM EMP;")
        rows=cursor.fetchall()
        print("---------------------------------------")
        for emp in rows:
            print(f"ID :{emp[0]} | NAME :{emp[1]} | SALARY :{emp[2]}")
    except Exception as e:
        print("Error ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed Sucessfully")


def read_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID =%s",(emp_id,))
        row=cursor.fetchone()
        
        if row:
            print("Read Employee By id : ",end="")
            print(f"ID :{row[0]} | NAME :{row[1]} | SALARY :{row[2]}")
            return row
        else:
            print(f"Employee record not found for : {emp_id}")
            return None
    
    except Exception as e:
        print("Error ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed Sucessfully")


def create_employee(name,salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("INSERT INTO ust_db.emp (EMP_NAME,SALARY) VALUES (%s,%s)",(name,salary))
        conn.commit()
        print("Employee Added Sucessfully")
    except Exception as e:
        print("Error ",e )
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed Sucessfulyy")    
        
def update_employee_by_id(emp_id,new_name,new_salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME=%s, SALARY=%s WHERE EMP_ID=%s",(new_name,new_salary,emp_id))
        conn.commit()
        print("Employee Updated Sucessfully")
    except Exception as e:
        print("Exception :",e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed Sucessfully")    
    

def delete_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        emp_to_be_deleted=read_employee_by_id(emp_id)
        
        if emp_to_be_deleted!=None:
            cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID=%s",(emp_id,))
            conn.commit()
            print("Deleted Sucessfully")
        else:
            print("No employee Record found")
    
    except Exception as e:
        print("Exception ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed Sucessfully")

# read_all_employees()
# # read_employee_by_id(2)
# create_employee("Santhosh",50000)
# read_all_employees()


read_all_employees()
delete_employee_by_id(3)
read_employee_by_id(3)
