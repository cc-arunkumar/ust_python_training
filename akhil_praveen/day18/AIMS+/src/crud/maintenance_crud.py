import pymysql
from typing import Optional
from ..models.maintainancelog import MaintenanceLog
from ..config.db_connection import get_connection
from datetime import datetime
import csv

#Creating asset obj and inserting to db
def create_maintenance_log(data:MaintenanceLog):
    try:
        conn = get_connection()
        cursor =conn.cursor()
        query = "insert into ust_aims_plus.maintenance_log (asset_tag,maintenance_type,vendor_name,description,cost,maintenance_date,technician_name,status) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = tuple(data.values())
        cursor.execute(query,values)
        conn.commit()
            
        
    except Exception as e:
        print("Exception : ",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            
# with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/final/maintenance_log.csv","r") as maintenance_file:
#     csv_file = csv.DictReader(maintenance_file)
    
#     for data in csv_file:
#         create_maintenance_log(data)