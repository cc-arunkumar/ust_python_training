#-------------ASSET-DATABASE------------------------

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

checked_file=r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\finaldata\validated_asset.csv"

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


#------------------EMPLOYEE-DATABASE--------------
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

def main():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO employee_directory (
        emp_code, full_name, email,
        phone, department, location, join_date, status
    ) VALUES (
        %s, %s, %s, %s, %s,
        %s, %s, %s
    )
    """

    csv_path = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\finaldata\validated_employee.csv"

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                join_date = datetime.strptime(row["join_date"], "%m/%d/%Y").strftime("%Y-%m-%d")
            except ValueError:
                print(f"Skipping row due to invalid date: {row['join_date']}")
                continue  # s

            data = (
                row["emp_code"],
                row["full_name"],
                row["email"],
                row["phone"],
                row["department"],
                row["location"],
                join_date,
                row["status"],
            )

            try:
                cursor.execute(query, data)
            except Exception as e:
                print(f"Error inserting row {row}: {e}")
                continue

    conn.commit()
    cursor.close()
    conn.close()

    print("All valid CSV records inserted successfully!")

if __name__ == "__main__":
    main()
    
#--------------VENDOR-DATABASE-----------------
import csv
import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )

conn = get_connection()
cursor = conn.cursor()

vendor=r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\finaldata\validated_vendors.csv"



with open(vendor, mode="r", encoding="utf-8") as file1:
    reader = csv.DictReader(file1)

    for row in reader:
        try:
            if not row["vendor_id"].isdigit():
                # print(f"Skipping bad row: {row}")
                continue
            sql = """
            INSERT INTO vendor_valid (
                vendor_id, vendor_name, contact_person, contact_phone,
                gst_number, email, address, city, active_status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
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

            cursor.execute(sql, values)

        except Exception as e:
            print(f"Error inserting vendor_id {row['vendor_id']}: {e}")

    conn.commit()

cursor.close()
conn.close()

print("CSV data successfully dumped into table.")

#------------EMPLOYEE-DATABASE-----
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

def main():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO employee_directory (
        emp_code, full_name, email,
        phone, department, location, join_date, status
    ) VALUES (
        %s, %s, %s, %s, %s,
        %s, %s, %s
    )
    """

    csv_path = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\valid_employee.csv"

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                join_date = datetime.strptime(row["join_date"], "%m/%d/%Y").strftime("%Y-%m-%d")
            except ValueError:
                print(f"Skipping row due to invalid date: {row['join_date']}")
                continue  # s

            data = (
                row["emp_code"],
                row["full_name"],
                row["email"],
                row["phone"],
                row["department"],
                row["location"],
                join_date,
                row["status"],
            )

            try:
                cursor.execute(query, data)
            except Exception as e:
                print(f"Error inserting row {row}: {e}")
                continue

    conn.commit()
    cursor.close()
    conn.close()

    print("All valid CSV records inserted successfully!")

if __name__ == "__main__":
    main()

