import pymysql
from typing import Optional
from ..models.assetsinventory import AssetInventory,StatusValidate
from ..config.db_connection import get_connection
from datetime import datetime
import csv

def get_keys():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = 'ust_aims_plus'
    AND TABLE_NAME = 'asset_inventory'
    ORDER BY ORDINAL_POSITION;""")
        col = cursor.fetchall()
        keys = []
        for i in col:
            keys.append(i[0])
        return keys
    except Exception as e:
        raise
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection Closed!")

#Creating asset obj and inserting to db
class AssetCrud:
    def create_asset(self,data:AssetInventory):
        try:
            conn = get_connection()
            cursor =conn.cursor()
            query = """
            insert into ust_aims_plus.asset_inventory (asset_tag,asset_type,serial_number,manufacturer,
            model,purchase_date,warranty_years,condition_status,
            assigned_to,location,asset_status,last_updated) 
            values (%s,%s,%s,%s,
            %s,%s,%s,%s,
            %s,%s,%s,%s)
            """
            values = tuple(data.__dict__.values()) + (datetime.now(),)
            cursor.execute(query,values)
            conn.commit()
            print("Data added successfully!")
            return data
            
                
            
        except Exception as e:
            print(e)
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")


                
    def get_all_asset(self,status):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            keys = get_keys()
            if status=="ALL":
                query = """
                select * 
                from ust_aims_plus.asset_inventory  
                """
                cursor.execute(query)
            else:
                query = """
                select * 
                from ust_aims_plus.asset_inventory 
                where asset_status = %s 
                """
                cursor.execute(query,(status,))
            rows = cursor.fetchall()
            if rows:
                list_rows = []
                for values in rows:
                    list_rows.append(dict(zip(keys,values)))
                return list_rows
            else:
                return None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")
        
                
    def get_asset_by_id(self,asset_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            keys = get_keys()
            query = """
            select * 
            from ust_aims_plus.asset_inventory 
            where asset_id = %s 
            """
            cursor.execute(query,(asset_id,))
            row = cursor.fetchone()
            if row:
                list_rows = []
                list_rows.append(dict(zip(keys,row)))
                return list_rows
            else:
                return False
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")
        
            
    def update_asset(self,id,data:AssetInventory):
        try:
            conn = get_connection()
            cursor =conn.cursor()
            query = """
            update ust_aims_plus.asset_inventory set asset_tag=%s,asset_type=%s,serial_number=%s,manufacturer=%s,
            model=%s,purchase_date=%s,warranty_years=%s,condition_status=%s,
            assigned_to=%s,location=%s,asset_status=%s,last_updated=%s where asset_id=%s
            """
            values =  tuple(data.__dict__.values()) + (datetime.now(),id)
            cursor.execute(query,values)
            conn.commit()
            print("Data updated successfully!")
            return data
            
        except Exception as e:
            print(str(e))
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def update_asset_status(self,id,status):
        try:
            
            conn = get_connection()
            cursor =conn.cursor()
            query = """
            update ust_aims_plus.asset_inventory set asset_status=%s where asset_id=%s
            """
            values =  (status,id)
            cursor.execute(query,values)
            conn.commit()
            print("status updated!")
            return self.get_asset_by_id(id)
            # return True
                
            
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")  
                
    def delete_asset(self,id):
        try:
            conn = get_connection()
            cursor =conn.cursor()
            condition = self.get_asset_by_id(id)
            if condition:
                query = """
                delete from ust_aims_plus.asset_inventory 
                where asset_id=%s
                """
                values =  (id,)
                cursor.execute(query,values)
                conn.commit()
                print("Asset deleted from id = ",id)
                keys = get_keys()
                list_rows = []
                list_rows.append(dict(zip(keys,condition)))
                return list_rows
                
            else:
                return False
                
            
        except Exception as e:
            print(e)
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def get_asset_by_keyword(self,keyword,value):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            keys = get_keys()
            query = f"""
            select  *
            from ust_aims_plus.asset_inventory 
            where {keyword}=%s
            """
            cursor.execute(query,(value,))
            rows = cursor.fetchall()
            if rows:
                list_rows = []
                for values in rows:
                    list_rows.append(dict(zip(keys,values)))
                return list_rows
            else:
                return False
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")
                
    def get_all_asset_count(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
            select * 
            from ust_aims_plus.asset_inventory
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                return len(rows)
            else:
                return None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")
                
    def bluk_upload(self):
        try:
            with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/final/asset_inventory.csv","r") as asset_file:
                csv_file = csv.DictReader(asset_file)
                
                for data in csv_file:
                    self.create_asset(data)
        except Exception as e:
            return e

# get_all_asset()
# obj =AssetCrud()
# obj.get_all_asset()
# get_asset_by_id(1)
# update_asset(1,data)



