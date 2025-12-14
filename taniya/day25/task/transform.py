import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_mysql_db"
    )

conn = get_connection()
cursor= conn.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM employees"
cursor.execute(sql)
employees = cursor.fetchall()
transform_employees=[]
for emp in employees:
    if emp["age"]<=25:
        emp["category"] = "Fresher"
    else:
        emp["category"] = "Experienced"
    transform_employees.append(emp)
    
for emp in transform_employees:
    print(emp)
cursor.close()
conn.close()