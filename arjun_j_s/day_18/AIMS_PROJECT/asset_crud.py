import mysql.connector
from datetime import datetime
from typing import Optional


def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )
    print("Connection Established")
    return conn


def validation(item):
    try:
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


def create_asset(body):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if validation(body):
            query = """
                INSERT INTO ust_asset_db.asset_inventory 
                (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status, last_updated)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = body[:-1] + (datetime.now(),)
            cursor.execute(query, values)
            conn.commit()
            print("Data added successfully")
        else:
            print("Not a valid data")
    except Exception as e:
        print(str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed")


def read_all_assets(status:Optional[str]="ALL"):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if(status=="ALL"):
            cursor.execute("select * from ust_asset_db.asset_inventory")
        else:
            cursor.execute("select * from ust_asset_db.asset_inventory where asset_status=%s",(status,))
        data = cursor.fetchall()
        if data:
            for no,i in enumerate(data):
                print(f"Record {no+1} : {i}")
        else:
            print("No Record Found")
    except Exception as e:
        print(str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed")

def read_asset_by_id(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("select * from ust_asset_db.asset_inventory where asset_id=%s",(asset_id,))
        data = cursor.fetchone()
        if data:
            print(f"Asset {asset_id} : {data}")
            return data
        else:
            print("Asset Not Found")
            return None
    except Exception as e:
        print(str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed")

def update_asset(asset_id,body):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if validation(body):
            query = """
                Update ust_asset_db.asset_inventory set
                asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s, model=%s, purchase_date=%s, warranty_years=%s, assigned_to=%s, asset_status=%s, last_updated=%s
                where asset_id=%s"""
            values = body[:-1] + (datetime.now(),asset_id) 
            cursor.execute(query, values)
            conn.commit()
            print("Data updated added successfully")
        else:
            print("Not a valid data")
    except Exception as e:
        print(str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed")

def delete_asset(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        data = read_asset_by_id(asset_id)
        if data:
            cursor.execute("delete from ust_asset_db.asset_inventory where asset_id=%s",(asset_id,))
            print("Deleted Successfully")
            conn.commit()
        else:
            print("Asset Not Found")
    except Exception as e:
        print(str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed")
