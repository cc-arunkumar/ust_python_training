import csv
import pymysql
from datetime import datetime

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )


conn = get_connection()
cursor = conn.cursor()

checked_file=r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\asset_inventory_checked.csv"

with open(checked_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        purchase_date = row["purchase_date"]
        if purchase_date:
            try:
            
                parsed_date = datetime.strptime(purchase_date, "%d/%m/%Y").date()
            except ValueError:
                try:
                
                    parsed_date = datetime.strptime(purchase_date, "%m/%d/%Y").date()
                except ValueError:
                    parsed_date = None  
            purchase_date = parsed_date.strftime("%Y-%m-%d") if parsed_date else None
        else:
            purchase_date = None

        cursor.execute("""
        INSERT INTO asset_inventory (
            asset_tag, asset_type, serial_number, manufacturer, model,
            purchase_date, warranty_years, condition_status, assigned_to,
            location, asset_status
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["asset_tag"],
            row["asset_type"],
            row["serial_number"],
            row["manufacturer"],
            row["model"],
            purchase_date,
            int(row["warranty_years"]) if row["warranty_years"] else None,
            row["condition_status"],
            row["assigned_to"],
            row["location"],
            row["asset_status"],
        ))


conn.commit()
cursor.close()
conn.close()

print("CSV data successfully dumped into MySQL database!")