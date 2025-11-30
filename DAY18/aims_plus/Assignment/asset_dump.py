import pymysql
import csv
import os

print("🔥 Starting FULL data dump (assets + employees + vendors + maintenance)...")

conn = None
cursor = None

try:
    # 1) CONNECT TO DB
    print("👉 Connecting to DB...")
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="aims_db",
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    print("✅ DB Connected")

    # base directory = folder where this script is located
    base_dir = os.path.dirname(__file__)
    cleaned_dir = os.path.join(base_dir, "cleaned")

    # -------------------- ASSETS --------------------
    # assets_csv = os.path.join(cleaned_dir, "asset_inventory_validated.csv")
    # print(f"\n📂 Loading ASSETS from: {assets_csv}")

    # asset_query = """
    #     INSERT INTO asset_inventory (
    #         asset_tag, asset_type, serial_number, manufacturer, model,
    #         purchase_date, warranty_years, condition_status, assigned_to,
    #         location, asset_status
    #     )
    #     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    # """

    # asset_count = 0
    # with open(assets_csv, mode="r", encoding="utf-8") as f:
    #     reader = csv.DictReader(f)
    #     for row in reader:
    #         cursor.execute(
    #             asset_query,
    #             (
    #                 row["asset_tag"],
    #                 row["asset_type"],
    #                 row["serial_number"],
    #                 row["manufacturer"],
    #                 row["model"],
    #                 row["purchase_date"],
    #                 int(row["warranty_years"]),
    #                 row["condition_status"],
    #                 row["assigned_to"],
    #                 row["location"],
    #                 row["asset_status"],
    #             ),
    #         )
    #         asset_count += 1
    # conn.commit()
    # print(f"✅ {asset_count} asset records inserted.")

    # -------------------- EMPLOYEES --------------------
    emp_csv = os.path.join(cleaned_dir, "employee_directory_validated.csv")
    print(f"\n📂 Loading EMPLOYEES from: {emp_csv}")

    emp_query = """
        INSERT INTO employee_directory (
            emp_code, full_name, email, phone,
            department, location, join_date, status
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    emp_count = 0
    with open(emp_csv, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute(
                emp_query,
                (
                    row["emp_code"],
                    row["full_name"],
                    row["email"],
                    row["phone"],
                    row["department"],
                    row["location"],
                    row["join_date"],
                    row["status"],
                ),
            )
            emp_count += 1
    conn.commit()
    print(f"✅ {emp_count} employee records inserted.")

    # -------------------- VENDORS --------------------
    vendor_csv = os.path.join(cleaned_dir, "vendor_master_validated.csv")
    print(f"\n📂 Loading VENDORS from: {vendor_csv}")

    vendor_query = """
        INSERT INTO vendor_master (
            vendor_name, contact_person, contact_phone, gst_number,
            email, address, city, active_status
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    vendor_count = 0
    with open(vendor_csv, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute(
                vendor_query,
                (
                    row["vendor_name"],
                    row["contact_person"],
                    row["contact_phone"],
                    row["gst_number"],
                    row["email"],
                    row["address"],
                    row["city"],
                    row["active_status"],
                ),
            )
            vendor_count += 1
    conn.commit()
    print(f"✅ {vendor_count} vendor records inserted.")

    # -------------------- MAINTENANCE --------------------
    maint_csv = os.path.join(cleaned_dir, "maintenance_log_validated.csv")
    print(f"\n📂 Loading MAINTENANCE from: {maint_csv}")

    maint_query = """
        INSERT INTO maintenance_log (
            asset_tag, maintenance_type, vendor_name, description,
            cost, maintenance_date, technician_name, status
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    maint_count = 0
    with open(maint_csv, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute(
                maint_query,
                (
                    row["asset_tag"],
                    row["maintenance_type"],
                    row["vendor_name"],
                    row["description"],
                    float(row["cost"]),
                    row["maintenance_date"],
                    row["technician_name"],
                    row["status"],
                ),
            )
            maint_count += 1
    conn.commit()
    print(f"✅ {maint_count} maintenance records inserted.")

except Exception as e:
    print("❌ Error occurred in full dump:")
    print(repr(e))

finally:
    if cursor is not None:
        cursor.close()
        print("\n🔻 Cursor closed")
    if conn is not None:
        conn.close()
        print("🔻 DB connection closed")

print("\n🎉 FULL DATA DUMP DONE (assets + employees + vendors + maintenance) ✅")
