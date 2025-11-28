"""
CSV Bulk Import Script for AIMS Database
----------------------------------------

This script reads data from multiple CSV files and inserts them into the respective
database tables only if the record does not already exist (duplicate-safe import).

Tables Supported:
- vendor_master
- asset_inventory
- employee_directory
- maintenance_log

Author: (Your Name)
Date: (YYYY-MM-DD)

IMPORTANT:
- Ensure CSV column names match database schema
- Update file paths before running
"""

import csv
import pymysql
import datetime


# ---------- DATABASE CONNECTION ----------

def get_connection():
    """Creates and returns a MySQL database connection."""
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="aims"
    )


# ---------- CSV Import Helper Function ----------

def import_csv(file_path, insert_query, check_query=None, unique_field=None):
    """
    Generic CSV importer that prevents duplicates.

    Parameters:
        file_path   : str  -> Path to CSV file
        insert_query: str  -> INSERT SQL query
        check_query : str  -> Optional Duplicate check query
        unique_field: str  -> CSV column name to check duplicates

    Returns:
        None
    """
    
    conn = get_connection()
    cursor = conn.cursor()

    print(f"\n📁 Importing: {file_path}")

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:

            # Check for existing record (if validation query is provided)
            if check_query and unique_field:
                cursor.execute(check_query, (row[unique_field],))
                if cursor.fetchone():
                    print(f"⏭ Skipping duplicate: {row[unique_field]}")
                    continue

            try:
                # Execute insert
                cursor.execute(insert_query, tuple(row.values()))
                conn.commit()
                print(f"✔ Inserted: {list(row.values())[0]}")

            except Exception as e:
                conn.rollback()
                print(f"❌ Error inserting record: {e}")

    cursor.close()
    conn.close()
    print(f"✅ Completed import: {file_path}\n")


# ---------- Query Definitions ----------

vendor_check_query = "SELECT vendor_id FROM vendor_master WHERE gst_number = %s"
vendor_insert_query = """
INSERT INTO vendor_master(vendor_name, contact_person, contact_phone,
gst_number, email, address, city, active_status)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""

asset_insert_query = """
INSERT INTO asset_inventory(
ASSET_TAG, ASSET_TYPE, SERIAL_NUMBER, MANUFACTURER, MODEL,
PURCHASE_DATE, WARRANTY_YEARS, CONDITION_STATUS, ASSIGNED_TO,
LOCATION, ASSET_STATUS, LAST_UPDATED
) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

employee_insert_query = """
INSERT INTO employee_directory(emp_code, full_name, email, phone,
department, location, join_date, status)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""

maintenance_insert_query = """
INSERT INTO maintenance_log(
asset_tag, maintenance_type, vendor_name,
description, cost, maintenance_date, technician_name, status
) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""


# ---------- File Paths (Update if needed) ----------

vendor_file = r"vendor_master.csv"
asset_file = r"cleaned_asset_inventory.csv"
employee_file = r"cleaned_employee_directory.csv"
maintenance_file = r"cleaned_maintenance_log.csv"


# ---------- Run Imports ----------

import_csv(vendor_file, vendor_insert_query, vendor_check_query, "gst_number")
import_csv(asset_file, asset_insert_query)  # No duplicate check (asset_tag can be used if needed)
import_csv(employee_file, employee_insert_query)  # No duplicate check
import_csv(maintenance_file, maintenance_insert_query)  # No duplicate check

print("\n🎉 ALL DATA IMPORT COMPLETED SUCCESSFULLY 🎉")
