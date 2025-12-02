import pymysql 

def get_connection():
    # Return a new pymysql connection to the ust_db database
    conn =pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='ust_db1',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn 

