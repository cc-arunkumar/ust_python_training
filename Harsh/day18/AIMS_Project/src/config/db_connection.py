import pymysql
def get_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )
    return conn
