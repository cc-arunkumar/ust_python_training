import csv
from ..models.maintenance_model import MaintenanceLog
from src.config.db_connection import get_connection

path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/final/maintenance_log.csv"

with open(path, "r") as maintenance_file:
    maintenance_data = csv.DictReader(maintenance_file)
    maintenance_data = list(maintenance_data)

def create_maintenance(maintenance:MaintenanceLog):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query="""
Insert into ust_aims_plus.maintenance_log (asset_tag,maintenance_type,vendor_name,description,cost,maintenance_date,technician_name,status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = tuple(maintenance.values())
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

# for data in maintenance_data:
#     try:
#         create_maintenance(data)
#     except Exception as e:
#         print(str(e))
    



