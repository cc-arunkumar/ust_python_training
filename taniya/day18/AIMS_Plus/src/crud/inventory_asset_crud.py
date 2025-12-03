import pymysql
import csv
from ..models.asset_model import Asset
from datetime import datetime

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_assets"
    )
class AssetCrud:
    def Create_task(self,data:Asset):
        # asset_id,asset_tag, asset_type, serial_number, manufacturer,
        #             model, purchase_date, warranty_years,
        #             condition_status, assigned_to, location, asset_status
    

        
        # last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            conn = get_connection()
            cursor = conn.cursor()
            sql = """
                INSERT INTO asset_inventory (
                    asset_id,asset_tag, asset_type, serial_number, manufacturer,
                    model, purchase_date, warranty_years, condition_status,
                    assigned_to, location, asset_status, last_updated
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            # values = (asset_id,asset_tag, asset_type, serial_number, manufacturer,
            #         model, purchase_date, warranty_years, condition_status,
            #         assigned_to, location, asset_status, last_updated)
            values = tuple(data.__dict__.values()) + (datetime.now(),)

            cursor.execute(sql, values)
            conn.commit()
            print("Data added successfully")
            # cursor.close()
            # conn.close()
            return data

    # print(" Asset record created successfully!")
        except Exception as e:
            print(e)
            raise
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("connection closed")
    def get_all_asset(self,status):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            if status=="ALL":
                sql="""
                select * from ust_assets.asset_inventory where asset_status=%s
                """
                cursor.execute(sql,(status),)
                conn.commit()
        except Exception as e:
            print("Error:",e)
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("connection closed")

    
    
    
    
    
    
    # with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day18\AIMS_Plus\database\asset_inventory_validated.csv", newline="") as file1:
    #     reader = csv.DictReader(file1)
    #     for row in reader:
    #         Create_task(
    #             asset_id=int(row["asset_id"]),
    #             asset_tag=row["asset_tag"],
    #             asset_type=row["asset_type"],
    #             serial_number=row["serial_number"],
    #             manufacturer=row["manufacturer"],
    #             model=row["model"],
    #             purchase_date=row["purchase_date"],
    #             warranty_years=int(row["warranty_years"]),
    #             condition_status=row["condition_status"],
    #             assigned_to=row["assigned_to"],
    #             location=row["location"],
    #             asset_status=row["asset_status"]
    #         )

# Create_task(
#     asset_id =1001,
#     asset_tag="UST-LTP-0001",
#     asset_type="Laptop",
#     serial_number="SN123456",
#     manufacturer="Dell",
#     model="Latitude 5420",
#     purchase_date="2023-05-15",
#     warranty_years=3,
#     condition_status="Good",
#     assigned_to="John Doe",
#     location="Hyderabad",
#     asset_status="Assigned"
# )