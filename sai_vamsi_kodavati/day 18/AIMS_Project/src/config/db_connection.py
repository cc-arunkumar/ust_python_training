import pymysql

def get_connection():
    
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="pass@word1",
            database="ust_asset_db"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None