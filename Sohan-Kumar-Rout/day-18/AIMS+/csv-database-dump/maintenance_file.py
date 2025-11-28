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

input_file = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\valid_maintenance.csv"

with open(input_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            # Parse date in MM/DD/YYYY format
            date_val = datetime.strptime(row["maintenance_date"], "%m/%d/%Y")
            formatted_date = date_val.strftime("%Y-%m-%d")

            sql = """
            INSERT INTO maintenance_valid (
                log_id, asset_tag, maintenance_type, vendor_name,
                description, cost, maintenance_date, technician_name, status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                int(row["log_id"]),
                row["asset_tag"],
                row["maintenance_type"],
                row["vendor_name"],
                row["description"],
                row["cost"],
                formatted_date,
                row["technician_name"],
                row["status"],
            )

            cursor.execute(sql, values)

        except Exception as e:
            print(f"Error inserting log_id {row.get('log_id')}: {e}")

    conn.commit()

cursor.close()
conn.close()

print("CSV data successfully dumped into maintenance_log table.")
