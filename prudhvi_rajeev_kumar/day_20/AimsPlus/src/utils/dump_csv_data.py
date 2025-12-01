import csv
import pymysql

# --- DB connection ---
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )

# --- Generic loader ---
def load_csv_to_db(csv_file, insert_sql, fields):
    conn = get_connection()
    cursor = conn.cursor()
    success, fail = 0, 0

    with open(csv_file, newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            values = tuple(row[f] for f in fields)
            try:
                cursor.execute(insert_sql, values)
                success += 1
            except Exception as e:
                print(f"Skipping row due to DB error: {row}\nError: {e}")
                fail += 1

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Inserted {success} rows, skipped {fail} rows.")

# --- File paths (adjust to your actual folder) ---
asset_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_20\AIMS\database\sample_data\final_data\validated_asset_inventory.csv"
employee_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_20\AIMS\database\sample_data\final_data\validated_employee_directory.csv"
vendor_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_20\AIMS\database\sample_data\final_data\validated_vendor_master.csv"
maintenance_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_20\AIMS\database\sample_data\final_data\validated_maintenance_log.csv"

# --- Loaders ---
def load_assets():
    sql = """INSERT INTO asset_inventory
       (asset_tag, asset_type, serial_number, manufacturer, model,
        purchase_date, warranty_years, condition_status, assigned_to,
        location, asset_status)
       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    fields = ["asset_tag","asset_type","serial_number","manufacturer","model",
              "purchase_date","warranty_years","condition_status","assigned_to",
              "location","asset_status"]
    load_csv_to_db(asset_file, sql, fields)

def load_employees():
    sql = """INSERT INTO employee_master
             (emp_code, full_name, email, phone, department, location, join_date, status)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    fields = ["emp_code","full_name","email","phone","department","location","join_date","status"]
    load_csv_to_db(employee_file, sql, fields)

def load_vendors():
    sql = """INSERT INTO vendor_master
        (vendor_id, vendor_name, contact_person, contact_phone, gst_number,
         email, address, city, active_status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    fields = ["vendor_id","vendor_name","contact_person","contact_phone","gst_number",
              "email","address","city","active_status"]
    load_csv_to_db(vendor_file, sql, fields)

def load_maintenance():
    sql = """INSERT INTO maintenance_log
        (log_id, asset_tag, maintenance_type, vendor_name, description,
         cost, maintenance_date, technician_name, status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    fields = ["log_id","asset_tag","maintenance_type","vendor_name","description",
              "cost","maintenance_date","technician_name","status"]
    load_csv_to_db(maintenance_file, sql, fields)

# --- Run loaders ---
if __name__ == "__main__":
    load_assets()
    # load_employees()
    # load_vendors()
    # load_maintenance()
