import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",       
        user="root",            
        password="pass@word1", 
        database="ust_mysql_db"
    )
    
conn = get_connection()
cursor = conn.cursor(pymysql.cursors.DictCursor)

sql="SELECT * FROM employees"
cursor.execute(sql)
employees=cursor.fetchall()

for emp in employees:
    print(emp)
    
cursor.close()
conn.close()