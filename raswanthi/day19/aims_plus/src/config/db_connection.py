import pymysql

#get_connection function
def get_connection():
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='pass@word1',
        database='aims_db'
    )
    return conn