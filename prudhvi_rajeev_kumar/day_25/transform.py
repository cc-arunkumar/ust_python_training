import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="pass@word1",
    database="ust_mysql_db"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]

employees = [dict(zip(columns, row)) for row in rows]

for emp in employees:
    emp["category"] = "Fresher" if emp["age"] <= 25 else "Experienced"

print(employees)

cursor.close()
conn.close()

