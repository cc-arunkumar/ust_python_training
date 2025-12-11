import pymysql

def get_mysql_connection():
    conn = pymysql.connect(
        host="localhost",       
        user="root",            
        password="1234",     
        database="ust_mysql_db",
        cursorclass=pymysql.cursors.DictCursor  
    )
    return conn
