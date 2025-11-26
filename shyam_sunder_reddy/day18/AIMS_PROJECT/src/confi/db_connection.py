import pymysql

def get_connection():
    conn = pymysql.connect(
        host="localhost",       # Database server
        user="root",            # Username
        password="pass@word1",  # Password
        database="ust_asset_db" # Target database
    )
    return conn
