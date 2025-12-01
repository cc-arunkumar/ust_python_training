import pymysql
from pymysql.cursors import DictCursor

def get_connection():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db",
        cursorclass=DictCursor
    )
    return conn