import pymysql
from pymysql.cursors import DictCursor
# import json
def get_connection():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="employee_db",
        cursorclass=DictCursor
    )
    return conn