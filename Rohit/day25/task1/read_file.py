
import json 
import pymysql
from  db_connection import get_connection

def read_file_from_db():
    
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor) 

        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        for emp in employees:
            print(emp)

    finally:
        if cursor: cursor.close()
        if conn: conn.close()




read_file_from_db()