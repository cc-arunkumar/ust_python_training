import pymysql 

def get_connection():
    # Return a new pymysql connection to the ust_db database
    conn =pymysql.connect(
        host='localhost',
        user='root',
        password='pass@word1',
        database='ust_db',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn 

