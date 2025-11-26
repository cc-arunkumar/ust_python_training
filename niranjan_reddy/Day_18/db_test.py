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
        
        cursor.execute("SELECT * FROM EMP;")
        rows=cursor.fetchall()
        print("--------Employee record--------")
        for emp in rows:
            print(f"ID: {emp[0]} | NAME:{emp[1]} | SALARY: {emp[2]}")
    
    except Error as e:
        print("Error: ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")

def read_employees_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID= %s",(emp_id, ))
        row=cursor.fetchone()
        
        if row:
            print("Read Employee date by Id: ",end=" ")
            # print(f"ID: {row[0]} | NAME:{row[1]} | SALARY: {row[2]}")
            return [True,f"ID: {row[0]} | NAME:{row[1]} | SALARY: {row[2]}"]
        else:
            # print(f" Employee record not found: ",emp_id)
            return [False,f"Employee not found : {emp_id}"]
    except Error as e:
        print("Error: ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")

def create_employee(name,salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO ust_db.emp (EMP_NAME,EMP_SALARY) VALUES(%s,%s)",(name,salary))
        conn.commit()
        print("Employee record inserted successfully")
    except Error as e:
        print("Error: ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")

def update_employee_by_id(emp_id, new_name,new_salary):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME= %s, EMP_SALARY=%s WHERE EMP_ID=%s", (new_name,new_salary,emp_id))
        conn.commit()
        
        print("Employee record updated successfully")
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
        to_be_deleted,msg=read_employees_by_id(emp_id)
        if to_be_deleted:
            cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID =%s",(emp_id, ))
            conn.commit()
            print("Employee record deleted successfully!")
        else:
            print(msg)
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")
            
read_all_employees()
# read_employees_by_id(2)
# create_employee('Abhi',31000)
# read_all_employees()

# update_employee_by_id(2,"Sai Yaswanth",24550.23)
# read_employees_by_id(2)
delete_employee_by_id(4)
read_employees_by_id(4)

# conn=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="pass@word1",
#     database="ust_db"
# )

# print("connection established successfully with MYSQL DB: ",conn)

# conn.close()
# print("--->Connection close<-----")

