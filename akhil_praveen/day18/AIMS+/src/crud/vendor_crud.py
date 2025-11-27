import pymysql
from typing import Optional
from ..models.vendormaster import VendorMaster
from ..config.db_connection import get_connection
from datetime import datetime
import csv

#Creating asset obj and inserting to db
def create_vendor(data:VendorMaster):
    try:
        conn = get_connection()
        cursor =conn.cursor()
        query = "insert into ust_aims_plus.vendor_master (vendor_name,contact_person,contact_phone,gst_number,email,address,city,active_status) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = tuple(data.values())
        cursor.execute(query,values)
        conn.commit()
            
        
    except Exception as e:
        print("Exception : ",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            
# with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/final/vendor_master.csv","r") as vendor_file:
#     csv_file = csv.DictReader(vendor_file)
    
#     for data in csv_file:
#         create_vendor(data)