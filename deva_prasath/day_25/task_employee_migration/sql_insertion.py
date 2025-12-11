import mysql.connector
import json


with open(r"D:\training\ust_python_training\deva_prasath\day_25\employees.json",'r') as file:
    data=json.load(file)


def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_mysql_db"
    )
    return conn


def insert_data(data):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        for row in data:
            emp_id=row['emp_id']
            name=row['name']
            department=row['department']
            age=row['age']
            city=row['city']
            cursor.execute('''insert into employees(emp_id,name,department,age,city)
                           values(%s,%s,%s,%s,%s)''',(emp_id,name,department,age,city))
            conn.commit()
        print("Data inserted successfully")
    except Exception as e:
        print("Error:",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")

insert_data(data)
