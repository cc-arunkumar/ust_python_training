import pymysql

def get_db_connection():
    try:
        conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "pass@word1",
        database = "ust_db",
        cursorclass = pymysql.cursors.DictCursor
        )
        return conn
    except Exception as e:
        raise(f"Database connection failed {str(e)}")