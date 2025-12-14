import pymysql
import json


def get_connection():
    return pymysql.connect(
        host="localhost",       
        user="root",            
        password="pass@word1", 
        database="ust_mysql_db"
    )
    
conn = get_connection()
cursor = conn.cursor()

query = """
INSERT INTO employees(emp_id,name,department,age,city)
        VALUES(%s,%s,%s,%s,%s)
"""


with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day25\task\employees.json") as file:
        employees = json.load(file)
            
        for emp in employees:
            data = (
                emp["emp_id"],
                emp["name"],
                emp["department"],
                emp["age"],
                emp["city"]
            )
            cursor.execute(query,data)
conn.commit()
cursor.close()
conn.close()
print("All json file inserted successfully")
        