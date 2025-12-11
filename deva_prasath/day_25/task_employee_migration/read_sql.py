import mysql.connector
def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",        
        password="pass@word1",  
        database="ust_mysql_db"
    )
    return conn

def read_all_emp():
    try:
        conn=get_connection()
        cursor=conn.cursor()    
        cursor.execute("select * from employees;")
        rows=cursor.fetchall()
        # for emp in rows:
        #     print(f"emp_id:{emp[0]} | Name:{emp[1]} | Department:{emp[2]} | Age:{emp[3]} | City:{emp[4]}")
        
        return rows
    except Exception as e:
        print("Error:",e)       
        
    finally :
        if conn.is_connected():
            cursor.close()
            conn.close()
        # print("Connection closed")


records=read_all_emp()