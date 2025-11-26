import pymysql

def get_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="pass@word1",  # change this
            database="ust_asset_db",
            # autocommit=True,           # ensures data is saved
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except Exception as e:
        print(f"[DB ERROR] {e}")
        return None
