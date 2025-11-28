import pymysql
from pymysql.cursors import DictCursor

def get_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="pass@word1",
            database="ust_aims_db",
            port=3306,
            cursorclass=DictCursor
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise
