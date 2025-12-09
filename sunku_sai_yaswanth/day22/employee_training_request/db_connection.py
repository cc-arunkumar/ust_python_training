import pymysql
def get_connection():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="",
        cursorclass=pymysql.cursors.DictCursor
        
    )
    return conn