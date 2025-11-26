import pymysql
from datetime import datetime
from typing import Optional
 
 
def get_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )
    print("Connection Established")
    return conn
 
 
def validation(item):
    try:
        # print(item)
        if not str(item[0]).startswith("UST-"):
            return False
        if item[1] not in ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]:
            return False
        if item[6] <= 0:
            return False
        if item[8] == "Assigned" and item[7] is None:
            return False
        if item[8] in ["Available", "Retired"] and item[7] is not None:
            return False
    except Exception as e:
        print(str(e))
        return False
    else:
        return True
 
 
def create_asset(asset_data):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if validation(asset_data):
            query = """
                INSERT INTO ust_asset_db.asset_inventory
                (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status, last_updated)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = asset_data + (datetime.now(),)
            cursor.execute(query, values)
            conn.commit()
            print("Data added successfully")
        else:
            print("Not a valid data")
    except Exception as e:
        print(str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()
 
def read_all_asset(status:Optional[str]="ALL"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            if status=="ALL":
                cursor.execute("select * from ust_asset_db.asset_inventory")
            else:
                cursor.execute("select * from ust_asset_db.asset_inventory where asset_status = %s",(status,))
                
            rows = cursor.fetchall()
            if rows:
                print(rows)
            else:
                print("No record found!")
        except Exception as e:
            print("Error: ",e)
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection closed successfully!")

def read_asset_by_id(asset_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("select * from ust_asset_db.asset_inventory where asset_id = %s",(asset_id,))
            row = cursor.fetchone()
            if row:
                print(row)
                return row
            else:
                print("No record found!")
                return None
        except Exception as e:
            print("Error: ",e)
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection closed successfully!")
                
def update_employee_by_id(asset_id,asset_data):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        if validation(asset_data):
            query = """
                UPDATE ust_asset_db.asset_inventory SET asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s, model=%s, purchase_date=%s, warranty_years=%s, assigned_to=%s, asset_status=%s, last_updated=%s
                WHERE asset_id = %s
            """
            values = asset_data + (datetime.now(),) + (asset_id,)
            cursor.execute(query, values)
            conn.commit()
            print("Data added successfully")
        else:
            print("Not a valid data")
    except Exception as e:
        print(str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection closed!")
 
def delete_asset_by_id(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        data = read_asset_by_id(asset_id)
        if data:
            cursor.execute("delete from ust_asset_db.asset_inventory where asset_id = %s",(asset_id,))
            conn.commit()
            print("Asset deleted successfully!")
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection closed successfully!")

data = ('UST-LTP-1001','Laptop','SN-DL-9988123','Dell','Latitude 5520','2023-01-15',3,
    None,  
    'Available'
)
 
# create_asset(data)
       
# read_all_asset("Retired")
 
# read_asset_by_id(1)

# update_employee_by_id(1,data)

# delete_asset_by_id(1)