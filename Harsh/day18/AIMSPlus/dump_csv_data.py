

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
INSERT INTO asset_inventory (
    asset_tag, asset_type, serial_number, manufacturer, model,
    purchase_date, warranty_years, condition_status, assigned_to,
    location, asset_status
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s
)
"""

with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\validated_asset_inventory.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data = (
            row["asset_tag"],
            row["asset_type"],
            row["serial_number"],
            row["manufacturer"],
            row["model"],
            row["purchase_date"],
            row["warranty_years"],
            row["condition_status"],
            row["assigned_to"],
            row["location"],
            row["asset_status"]
        )
        cursor.execute(query, data)

conn.commit()
cursor.close()
conn.close()

print("All CSV records inserted successfully!")

