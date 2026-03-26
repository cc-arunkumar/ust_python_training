import pymysql

def get_connection():
    try:
        conn=pymysql.connect(
            host="localhost",
            user="root",
            password="pass@word1",
            database="aims_db"
        )
    
        return conn
    except Exception as e:
        print("Exception: ", e)
conn = get_connection()

print("Conneciton = ", conn)

