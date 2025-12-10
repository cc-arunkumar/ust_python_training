# mysql_read.py
import pymysql
from pymysql.cursors import DictCursor
from config import MYSQL_CONFIG

def read_employees_from_mysql():
    conn = pymysql.connect(**MYSQL_CONFIG, cursorclass=DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    print(" Employees read from MySQL:")
    for emp in rows:
        print(emp)
    return rows