import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
    )

    print("Connection established successully with MySQL DB")
    return conn

def read_all():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select * from emp")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID : {row[0]} | Name : {row[1]} | Salary : {row[2]}")
    conn.commit()


def read_emp_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("select * from emp where EMP_ID=%s",(emp_id,))
        # cursor.execute(f"select * from emp where EMP_ID={emp_id}")
        row=cursor.fetchone()
        print(row)
        return row
    except Exception as e:
        print(str(e))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")

def create_emp(emp_name,salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("insert into ust_db.emp (EMP_NAME,EMP_SALARY) VALUES (%s,%s)",(emp_name,salary))
        conn.commit()
        print("Added Successfully")
    except Exception as e:
        print(str(e))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")

def update_emp_by_id(emp_id,name,salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("update ust_db.emp set EMP_NAME =%s,EMP_SALARY=%s where EMP_ID=%s",(name,salary,emp_id))
        conn.commit()
        print("Updated Successfully")
    except Exception as e:
        print(str(e))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")

def delete_emp_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        to_del = read_emp_by_id(emp_id)
        if(to_del):
            cursor.execute("delete from ust_db.emp where EMP_ID = %s",(emp_id,))    
            conn.commit()
            print("Deleted Successfully")
        else:
            print("Record not found")
    except Exception as e:
        print(str(e))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")


# read_emp_by_id(3)
# read_all()
# create_emp("Sung JinWoo",400000)
# read_all()
# update_emp_by_id(4,"Sung JinWoo",450000000000000.876)
read_emp_by_id(4)
delete_emp_by_id(3)
read_all()
