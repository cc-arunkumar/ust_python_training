

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
INSERT INTO vendor_master (
    vendor_id,vendor_name,contact_person,contact_phone,
    gst_number,email,address,city,active_status
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s
)
"""

with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\updated_vendor_master.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data = (
            row["vendor_id"],
            row["vendor_name"],
            row["contact_person"],
            row["contact_phone"],
            row["gst_number"],
            row["email"],
            row["address"],
            row["city"],
            row["active_status"],
        )
        cursor.execute(query, data)

conn.commit()
cursor.close()
conn.close()

print("All CSV records inserted successfully!")

