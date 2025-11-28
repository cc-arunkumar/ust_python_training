

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
INSERT INTO maintenance_log (
    log_id,asset_tag,maintenance_type,vendor_name,
    description,cost,maintenance_date,technician_name,status
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s
)
"""

with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\updated_maintenance_valid.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data = (
            row["log_id"],
            row["asset_tag"],
            row["maintenance_type"],
            row["vendor_name"],
            row["description"],
            row["cost"],
            row["maintenance_date"],
            row["technician_name"],
            row["status"],
        )
        cursor.execute(query, data)

conn.commit()
cursor.close()
conn.close()

print("All CSV records inserted successfully!")

