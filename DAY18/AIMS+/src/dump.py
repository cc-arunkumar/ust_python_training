import pymysql
import csv


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="pass@word1",
    database="aims_db"
)

cursor = conn.cursor()

print("Database connected successfully")


asset_query = """
INSERT INTO asset_inventory (
    asset_tag, asset_type, serial_number, manufacturer, model,
    purchase_date, warranty_years, condition_status,
    assigned_to, location, asset_status
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

with open("cleaned\\asset_inventory_validated.csv", "r", encoding="utf-8") as file:
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

        cursor.execute(asset_query, data)

conn.commit()
print("asset_inventory table inserted successfully")



employee_query = """
INSERT INTO employee_directory (
    emp_code, full_name, email, phone,
    department, location, join_date, status
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""

with open("cleaned\\employee_directory_validated.csv", "r", encoding="utf-8") as file:
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
            row["status"]
        )

        cursor.execute(employee_query, data)

conn.commit()
print("employee_directory table inserted successfully")


vendor_query = """
INSERT INTO vendor_master (
    vendor_name, contact_person, contact_phone,
    gst_number, email, address, city, active_status
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""

with open("cleaned\\vendor_master_validated.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data = (
            row["vendor_name"],
            row["contact_person"],
            row["contact_phone"],
            row["gst_number"],
            row["email"],
            row["address"],
            row["city"],
            row["active_status"]
        )

        cursor.execute(vendor_query, data)

conn.commit()
print("vendor_master table inserted successfully")



maintenance_query = """
INSERT INTO maintenance_log (
    asset_tag, maintenance_type, vendor_name,
    description, cost, maintenance_date,
    technician_name, status
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""

with open("cleaned\\maintenance_log_validated.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data = (
            row["asset_tag"],
            row["maintenance_type"],
            row["vendor_name"],
            row["description"],
            row["cost"],
            row["maintenance_date"],
            row["technician_name"],
            row["status"]
        )

        cursor.execute(maintenance_query, data)

conn.commit()
print("maintenance_log done")

cursor.close()
conn.close()
