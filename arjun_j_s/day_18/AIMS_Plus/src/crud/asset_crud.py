import csv
from ..models.asset_model import AssetInventory
from src.config.db_connection import get_connection
from datetime import datetime
from typing import Optional

path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/final/asset_inventory.csv"

class Asset:
    def create_asset(asset:AssetInventory):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query="""
    Insert into ust_aims_plus.asset_inventory (asset_tag,asset_type,serial_number,manufacturer,model,purchase_date,warranty_years,condition_status,assigned_to,location,asset_status,last_updated)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)
            """
            values = tuple(asset.values()) + (datetime.now(),)
            cursor.execute(query,values)
            conn.commit()
            print("Data added successfully")
            return True
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_all_asset(status="all"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("select column_name from information")
            cursor.execute("select * from ust_aims_plus.asset_inventory")
            rows = cursor.fetchall()
            if status!="all":
                cursor.execute("select * from ust_aims_plus.asset_inventory where asset_status=%s",(status,))
                rows = cursor.fetchall()
            if rows:
                response=[]
                for data in rows:
                    response.append(data)
                return response
            else:
                return None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed")

    def get_asset_by_id(asset_id:int):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("select * from ust_aims_plus.asset_inventory where asset_id=%s",(asset_id,))
            row = cursor.fetchone()
            if row:
                return row
            else:
                return None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_asset_count():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("select * from ust_aims_plus.asset_inventory")
            row = cursor.fetchall()
            if row:
                return len(row)
            else:
                return None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_asset_keyword(keyword:str):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("select %s from ust_aims_plus.asset_inventory",(keyword,))
            row = cursor.fetchall()
            if row:
                return row
            else:
                return None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def bulk_upload(self):
        with open(path, "r") as asset_file:
            asset_data = csv.DictReader(asset_file)
            asset_data = list(asset_data)
        for data in asset_data:
            try:
                self.create_asset(data)
            except Exception as e:
                raise
        return True


    def update_asset_status(asset_id:int,status:str):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("update ust_aims_plus.asset_inventory set asset_status=%s where asset_id=%s",(status,asset_id))
            conn.commit()
            print("Status Updated")
            return True
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")


    def update_asset(asset_id:int,asset:AssetInventory):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query="""
    Update ust_aims_plus.asset_inventory set asset_tag=%s,asset_type=%s,serial_number=%s,
    manufacturer=%s,model=%s,purchase_date=%s,
    warranty_years=%s,condition_status=%s,assigned_to=%s,location=%s,asset_status=%s,last_updated=%s
    where asset_id=%s
            """
            values = tuple(asset.values()) + (datetime.now(),asset_id)
            cursor.execute(query,values)
            conn.commit()
            print("Data updated successfully")
            return True
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def delete_asset(self,asset_id:int):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            if self.get_asset_by_id(asset_id):
                cursor.execute("delete from ust_aims_plus.asset_inventory where asset_id=%s",(asset_id,))
                print("Deleted Successfully")
                conn.commit()
                return True
            else:
                return None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")



    



