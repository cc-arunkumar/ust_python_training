import csv
import datetime
import pymysql

# --- Simple validators ---
def validate_date(date_str):
    """Check if date is in YYYY-MM-DD format and valid."""
    try:
        datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_email(email_str):
    """Check if email contains '@' and ends with ust.com."""
    return email_str and "@" in email_str and email_str.strip().endswith("ust.com")

# --- DB connection ---
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )

# --- Generic loader ---
def load_csv_to_db(csv_file, insert_sql, fields, validators=None):
    conn = get_connection()
    cursor = conn.cursor()
    success, fail = 0, 0

    with open(csv_file, newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            values = tuple(row[f] for f in fields)

            # --- Run validators if provided ---
            if validators:
                valid = True
                for field, func in validators.items():
                    if not func(row[field]):
                        print(f"Skipping invalid {field}: {row[field]} for row {row}")
                        fail += 1
                        valid = False
                        break
                if not valid:
                    continue

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

# --- File paths ---
asset_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS\database\asset_inventory.csv"
vendor_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS\database\vendor_master.csv"
maintenance_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS\database\maintenance_log.csv"
employee_file = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS\database\employee_directory.csv"

# --- Loaders ---
def load_assets():
    sql = """INSERT INTO asset_inventory
       (asset_tag, asset_type, serial_number, manufacturer, model,
        purchase_date, warranty_years, condition_status, assigned_to,
        location, asset_status, last_updated)
       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    fields = ["asset_tag","asset_type","serial_number","manufacturer","model",
              "purchase_date","warranty_years","condition_status","assigned_to",
              "location","asset_status","last_updated"]
    load_csv_to_db(asset_file, sql, fields, validators={"purchase_date": validate_date})

def load_employees():
    sql = """INSERT INTO employee_master
             (emp_code, full_name, email, phone, department, location, join_date, status)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    fields = ["emp_code","full_name","email","phone","department","location","join_date","status"]
    load_csv_to_db(employee_file, sql, fields, validators={"join_date": validate_date, "email": validate_email})

def load_vendors():
    sql = """INSERT INTO vendor_master
        (vendor_id, vendor_name, contact_person, contact_phone, gst_number,
         email, address, city, active_status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    fields = ["vendor_id","vendor_name","contact_person","contact_phone","gst_number",
              "email","address","city","active_status"]
    load_csv_to_db(vendor_file, sql, fields, validators={"email": validate_email})

def load_maintenance():
    sql = """INSERT INTO maintenance_log
        (log_id, asset_tag, maintenance_type, vendor_name, description,
         cost, maintenance_date, technician_name, status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    fields = ["log_id","asset_tag","maintenance_type","vendor_name","description",
              "cost","maintenance_date","technician_name","status"]
    load_csv_to_db(maintenance_file, sql, fields, validators={"maintenance_date": validate_date})

# --- Run loaders ---
if __name__ == "__main__":
    load_assets()
    load_employees()
    load_vendors()
    load_maintenance()
