import json
import pymysql

path = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_25\employees.json"

with open(path) as f:
    employees = json.load(f)  

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="pass@word1",
    database="ust_mysql_db"
)
cursor = conn.cursor()

for emp in employees:
    cursor.execute("""
        INSERT IGNORE INTO employees (emp_id, name, department, age, city)
        VALUES (%s, %s, %s, %s, %s)
    """, (emp["emp_id"], emp["name"], emp["department"], emp["age"], emp["city"]))

conn.commit()
cursor.close()
conn.close()

