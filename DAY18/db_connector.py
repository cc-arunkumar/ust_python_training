import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1"
    )
    print("Connected successfully!")
except pymysql.connect.Error as err:
    print("Error:", err)

finally:
    conn.close()
