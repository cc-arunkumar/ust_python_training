import csv
from pydantic import ValidationError
from config.db_connection import get_connection
from models.asset_model import AssetInventory
from models.vendor_model import VendorMaster
from models.employee_model import EmployeeMaster
from models.maintainance_model import MaintenanceLog

import csv
from config.db_connection import get_connection

def load_csv_to_db(csv_file, insert_sql, fields):
    conn = get_connection()
    cursor = conn.cursor()
    with open(csv_file, newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            values = tuple(row[f] for f in fields)
            cursor.execute(insert_sql, values)
    conn.commit()
    cursor.close()
    conn.close()


asset_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS\database\asset_inventory.csv"
vendor_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS\database\vendor_master.csv"
maintenance_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS\database\maintenance_log.csv"


load_csv_to_db(
    asset_file,
    """INSERT INTO asset_inventory
       (asset_tag, asset_type, serial_number, manufacturer, model,
        purchase_date, warranty_years, condition_status, assigned_to,
        location, asset_status, last_updated)
       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
    ["asset_tag","asset_type","serial_number","manufacturer","model",
     "purchase_date","warranty_years","condition_status","assigned_to",
     "location","asset_status","last_updated"]
)


employee_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS\database\employee_directory.csv"

def load_employees():
    sql = """INSERT INTO employee_master
             (emp_code, full_name, email, phone, department, location, join_date, status)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    conn = get_connection()
    cursor = conn.cursor()
    with open(employee_file, newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            values = (
                row["emp_code"],
                row["full_name"],
                row["email"],
                row["phone"],
                row["department"],
                row["location"],
                row["join_date"],
                row["status"]
            )
            print("Inserting:", values)
            cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    
def load_vendors():
    sql = """INSERT INTO vendor_master
        (vendor_id, vendor_name, contact_person, contact_phone, gst_number,
         email, address, city, active_status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    load_csv_to_db(VendorMaster, "vendor_master", vendor_file, sql)

def load_maintenance():
    sql = """INSERT INTO maintenance_log
        (log_id, asset_tag, maintenance_type, vendor_name, description,
         cost, maintenance_date, technician_name, status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    load_csv_to_db(MaintenanceLog, "maintenance_log", maintenance_file, sql)
