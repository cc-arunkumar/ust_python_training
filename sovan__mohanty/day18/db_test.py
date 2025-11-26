import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",          
    password="pass@word1",
    database="ust_db"
)

print("Connection established successfully with MySql database:", conn)

conn.close()