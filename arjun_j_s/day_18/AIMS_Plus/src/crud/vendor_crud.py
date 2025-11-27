import csv
from ..models.vendor_model import VendorMaster
from src.config.db_connection import get_connection

path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/final/vendor_master.csv"

with open(path, "r") as vendor_file:
    vendor_data = csv.DictReader(vendor_file)
    vendor_data = list(vendor_data)

def create_vendor(vendor:VendorMaster):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query="""
Insert into ust_aims_plus.vendor_master (vendor_name,contact_person,contact_phone,gst_number,email,address,city,active_status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = tuple(vendor.values())
        cursor.execute(query,values)
        conn.commit()
        print("Data added successfully")
    except Exception as e:
        print(str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection Closed")

# for data in vendor_data:
#     try:
#         create_vendor(data)
#     except Exception as e:
#         print(str(e))
    



