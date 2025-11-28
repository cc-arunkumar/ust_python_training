from config.db_connection import get_connection
import csv
from datetime import datetime

def dump_asset_inventory():
    """
    Load asset inventory data from CSV and insert into the asset_inventory table.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO asset_inventory (
                asset_tag, asset_type, serial_number, manufacturer, model,
                purchase_date, warranty_years, condition_status, assigned_to,
                location, asset_status, last_updated
            ) VALUES (
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s
            )
        """
        # Read CSV file containing asset inventory data
        with open("../database/sample_data/final/validated_asset_inventory.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Prepare row data for insertion
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
                    row["asset_status"],
                    datetime.now()  # Track insertion timestamp
                )
                cursor.execute(query, data)

            conn.commit()
            print("Inserted into database successfully")
    except Exception as e:
        print("Error: ", e)
    finally:
        # Ensure resources are closed properly
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection closed successfully")
            
# dump_asset_inventory()


def dump_employee_data():
    """
    Load employee directory data from CSV and insert into the employee_directory table.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO ust_inventory_db.employee_directory (
                emp_code, full_name, email, phone,
                department, location, join_date, status
            ) VALUES (
                %s, %s, %s, %s,
                %s, %s, %s, %s
            )
        """
        # Read CSV file containing employee data
        with open("../database/sample_data/final/validated_employee_directory.csv", "r", encoding="utf-8") as file:
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
                cursor.execute(query, data)

        conn.commit()
        print("Inserted employee records successfully")

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Connection closed successfully")

# dump_employee_data()


def dump_vendor_data():
    """
    Load vendor master data from CSV and insert into the vendor_master table.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO ust_inventory_db.vendor_master (
                vendor_name, contact_person, contact_phone,
                gst_number, email, address, city, active_status
            ) VALUES (
                %s, %s, %s, %s,
                %s, %s, %s, %s
            )
        """
        # Read CSV file containing vendor data
        with open("../database/sample_data/final/validated_vendor_master.csv", "r", encoding="utf-8") as file:
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
                cursor.execute(query, data)

        conn.commit()
        print("Inserted vendor records successfully")

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Connection closed successfully")

# dump_vendor_data()


def dump_maintenance_data():
    """
    Load maintenance log data from CSV and insert into the maintenance_log table.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO ust_inventory_db.maintenance_log (
                asset_tag, maintenance_type, vendor_name,
                description, cost, maintenance_date,
                technician_name, status
            ) VALUES (
                %s, %s, %s, %s,
                %s, %s, %s, %s
            )
        """
        # Read CSV file containing maintenance log data
        with open("../database/sample_data/final/validated_maintenance_log.csv", "r", encoding="utf-8") as file:
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
                cursor.execute(query, data)

        conn.commit()
        print("Inserted maintenance records successfully")

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Connection closed successfully")

# dump_maintenance_data()
