import pymysql
def get_connnection():
        
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="pass@word1",
            database="ust_db"
        )
        print("Connected successfully to MySQL using PyMySQL!",conn)
        return conn
    except Exception as e:
        print("Connection Error:", e)


def read_all_employees():
    conn=get_connnection()
    print("connected succesf")
    cursor=conn.cursor()
    cursor.execute("select * from emp;")
    rows=cursor.fetchall()
    for (id,name,salary) in rows:
        print(f"ID:{id}|NAME:{name}|SALARY:{salary}")
# read_all_employees()
def read_by_id(id):
    try:
        conn=get_connnection()
        cursor=conn.cursor()
        cursor.execute("select * from emp where EMP_ID=%s; ",(id,))
        emp=cursor.fetchone()
        if emp:
            print(f"ID:{emp[0]}|NAME:{emp[1]}|SALARY:{emp[2]}")
            return True
        else:
            print("record not found")
            return False
    except Exception as e:
        print(e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("connection closed succesfully")
# read_by_id(2)


def add_emp(name,salary):
    conn=get_connnection()
    cursor=conn.cursor()
    cursor.execute("insert into emp(EMP_NAME,EMP_SALARY) values (%s,%s)",(name,salary))
    conn.commit()
    print("employeeadded")
        
# add_emp("arun",40000)
read_by_id(3)

def update_emp(id,new_name,new_sal):
    conn=get_connnection()
    cursor=conn.cursor()
    cursor.execute("update emp set EMP_NAME=%s,EMP_SALARY=%s where EMP_ID=%s",(new_name,new_sal,id))
    conn.commit()
    print("updated successfully")


update_emp(3,"akash",30000)
read_by_id(3)

def delete_emp(id):
    conn=get_connnection()
    cursor=conn.cursor()
    
    emp_to_be_deleted=read_by_id(id)
    if emp_to_be_deleted:
        cursor.execute("delete from emp where EMP_ID=%s",(id,))
        conn.commit()
        print("emp deleted ")
        
read_all_employees()
delete_emp(3)
read_all_employees()