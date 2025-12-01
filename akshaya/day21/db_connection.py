import pymysql

def get_connection():
    try:
        conn=pymysql.connect(
            host="localhost",
            user="root",
            password="pass@word1",
            database="emp_db",
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"Database connection error: {e}")
        return None