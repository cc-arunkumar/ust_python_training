
import pymysql
import csv

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="pass@word1",
    database="ust_aims_db"
)

cursor = conn.cursor()

query = """
INSERT INTO employee_directory (
    emp_code,full_name,email,
    phone,department,location,join_date,status
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s
)
"""

with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\validated_employee_directory.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data = (
            row["emp_code"],
            row["full_name"],
            row["email"],
            row["phone"],
            row["department"],
            row["location"],
            row["join_date"],
            row["status"],
        )
        cursor.execute(query, data)

conn.commit()
cursor.close()
conn.close()

print("All CSV records inserted successfully!")

