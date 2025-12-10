import pymysql  
import json

def get_connection():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="password123",
        database="ust_mysql_db",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

#loading the data from json and uploading to the mysql databse
def load_data():
    with open("employees.json","r") as file:
        data=json.load(file)
        for emp in data:
            insert(emp)

def insert(data):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            '''
            INSERT 
            INTO ust_mysql_db.employees (emp_id,name,department,age,city)
            VALUES(%s,%s,%s,%s,%s)
            ''',
            (data["emp_id"],data["name"],data["department"],data["age"],data["city"])
        )
        conn.commit()
        print("inserted successfully ",data["emp_id"])
    except Exception:
        print("error occured while inserting ",data["emp_id"])
    finally:
        if conn.open:
            cursor.close()
            conn.close()

def read_all():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM ust_mysql_db.employees
            '''
        )
        data=cursor.fetchall()
        return data
    except Exception:
        print("exception occured")
    finally:
        if conn.open:
            cursor.close()
            conn.close
            