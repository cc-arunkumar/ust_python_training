import csv
from pydantic import ValidationError
from src.config.db_connection import get_connection
from models.asset_model import AssetInventory
from models.vendor_model import VendorMaster
from models.maintainance_model import MaintenanceLog

def load_csv_to_db(model, table_name, csv_file, insert_sql):
    conn = get_connection()
    cursor = conn.cursor()
    with open(csv_file, newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            try:
                obj = model(**row)  
                cursor.execute(insert_sql, tuple(obj.dict().values()))
            except ValidationError as e:
                print(f"Row failed validation: {row}\nErrors: {e.errors()}")
    conn.commit()
    cursor.close()
    conn.close()

asset_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS+PROJECT\database\asset_inventory.csv"
vendor_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS+PROJECT\database\vendor_master.csv"
maintenance_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS+PROJECT\database\maintenance_log.csv"

def load_assets():
    sql = """INSERT INTO asset_inventory
        (asset_id, asset_tag, asset_type, serial_number, manufacturer, model,
         purchase_date, warranty_years, condition_status, assigned_to,
         location, asset_status, last_updated)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    load_csv_to_db(AssetInventory, "asset_inventory",
                   asset_file, sql)

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
