import csv
import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",   
        database="aims_db",
        
    )

# def dump_asset_inventory(csv_file):
#     conn = get_connection()
#     with conn.cursor() as cursor:
#         with open(csv_file, "r") as f:
#             reader = csv.DictReader(f)
#             for row in reader:
#                 sql = """INSERT INTO asset_inventory 
#                          (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, 
#                           warranty_years, condition_status, assigned_to, location, asset_status, last_updated)
#                          VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())"""
#                 cursor.execute(sql, (
#                     row["asset_tag"], row["asset_type"], row["serial_number"], row["manufacturer"],
#                     row["model"], row["purchase_date"], row["warranty_years"], row["condition_status"],
#                     row.get("assigned_to"), row["location"], row["asset_status"]
#                 ))
#         conn.commit()
#     conn.close()
#     print("Data dumped successfully into asset_inventory")
    

# def dump_employee_directory(csv_file):
#     conn = get_connection()
#     sql = """INSERT INTO employee_directory 
#                 (emp_code, full_name, email, phone, department, location, join_date, status)
#             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
#     with conn.cursor() as cursor:
#         with open(csv_file, "r") as f:
#             reader = csv.DictReader(f)
#             for row in reader:
#                 try:
#                     cursor.execute(sql, (
#                     row["emp_code"], row["full_name"], row["email"],
#                     row["phone"], row["department"], row["location"],
#                     row["join_date"], row["status"]
#                     ))
#                 except Exception as e:
#                     print(str(e))
                
#         conn.commit()
#     conn.close()
#     print("Data dumped into employee_directory")


# def dump_maintenance(csv_file):
#     conn = get_connection()
#     with conn.cursor() as cursor:
#         with open(csv_file, "r") as f:
#             reader = csv.DictReader(f)
#             for row in reader:
#                 sql = """INSERT INTO maintenance_log 
#                          (asset_tag, maintenance_type, vendor_name, description, cost, maintenance_date, technician_name, status)
#                          VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
#                 cursor.execute(sql, (
#                     row["asset_tag"], row["maintenance_type"], row["vendor_name"],
#                     row["description"], row["cost"], row["maintenance_date"], row["technician_name"], row["status"]
#                 ))
#         conn.commit()
#     conn.close()
#     print("Data dumped into maintenance_log")

# def dump_vendor(csv_file):
#     conn = get_connection()
#     with conn.cursor() as cursor:
#         with open(csv_file, "r") as f:
#             reader = csv.DictReader(f)
#             for row in reader:
                
#                 if not row["vendor_name"]:
#                     continue
#                 sql = """INSERT INTO vendor_master 
#                          (vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status)
#                          VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
#                 cursor.execute(sql, (
#                     row["vendor_name"], row["contact_person"], row["contact_phone"], row["gst_number"],
#                     row["email"], row["address"], row["city"], row["active_status"]
#                 ))
#         conn.commit()
#     conn.close()
#     print("Data dumped into vendor_master")




# if __name__ == "__main__":
    # dump_asset_inventory("C:/Users/Administrator/Desktop/ust_python_training/raswanthi/day19/aims_plus/database/sample_data/final_data/validated_assets.csv")
    # dump_employee_directory("C:/Users/Administrator/Desktop/ust_python_training/raswanthi/day19/aims_plus/database/sample_data/final_data/validated_employees.csv")
    # dump_maintenance("C:/Users/Administrator/Desktop/ust_python_training/raswanthi/day19/aims_plus/database/sample_data/final_data/validated_maintenance.csv")
    # dump_vendor("C:/Users/Administrator/Desktop/ust_python_training/raswanthi/day19/aims_plus/database/sample_data/final_data/validated_vendors.csv")