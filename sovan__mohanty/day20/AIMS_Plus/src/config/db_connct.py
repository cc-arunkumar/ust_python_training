import pymysql

def get_conn():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="aims",
        cursorclass=pymysql.cursors.DictCursor
    )
