import mysql.connector

#---------------------Connection established--------------------------#

def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
    )
    return conn

#---------------------Read All--------------------------#

def read_all_employees():
    try:
        conn=get_connection()
        cursor=conn.cursor()

        cursor.execute("SELECT * FROM EMP;")
        rows=cursor.fetchall()
        for emp in rows:
            print(f"ID:{emp[0]} | Name: {emp[1]} |Salary: {emp[2]}")

    except Exception as e:
        print("Error:",e)
    
    finally :
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")
    return rows
#---------------------Read employee by ID--------------------------#

def read_employee_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("select * from EMP where EMP_ID=%s",(emp_id,))
        row=cursor.fetchone()
        
        if row:
            print("Read employee data by id:",end="")
            print(f"ID:{row[0]} | Name: {row[1]} |Salary: {row[2]}")
        else:
            print(f"Employee record not found for:{emp_id}")
    
    except Exception as e:
        print("Error:",e)
    
    finally :
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")
    return row


#---------------------Create employee(Insert)--------------------------#

def create_employee(name,salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("insert into emp (EMP_NAME,EMP_SALARY)values  (%s,%s)",(name,salary))
        conn.commit()
        print("Employee record inserted successfully")
        
    except Exception as e:
        print("Error:",e)
    
    finally :
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")
        
        
        


def update_employee_by_id(emp_id,new_name,new_salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("update emp set EMP_NAME = %s,EMP_SALARY=%s where EMP_ID=%s",(new_name,new_salary,emp_id))
        conn.commit()
        print("Updated successfully")
    
    except Exception as e:
        print("Error",e)
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")


def delete_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("delete from EMP where EMP_ID=%s",(emp_id,))
        conn.commit()
        print("Employee deleted successfully")
    
    except Exception as e:
        print("error",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")
    

    
# read_all_employees()
# read_employee_id(3)
# create_employee("raj",90900)


# read_all_employees()
# update_employee_by_id(4,"Deeps",5000)
# read_employee_id(4)

# read_all_employees()
# delete_by_id(2)
# read_all_employees()

to_be_deleted=read_employee_id(4)
print(to_be_deleted)
if to_be_deleted:
    delete_by_id(to_be_deleted[0])
read_all_employees()