import pymysql

def get_db_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="pass@word1",
            database="aims_db",
            cursorclass=pymysql.cursors.DictCursor  # 
        )
        return conn
    except Exception as e:
        # simple error, our exception handler will catch if needed
        raise Exception(f"Database connection failed: {str(e)}")
