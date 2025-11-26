# from db_connection import get_connection
from datetime import datetime
import json
import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )
    return conn

allowed_assert_status = ["Available","Assigned","Repair","Repair"]
allowed_assert_type = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]

def get_all_assets():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("select * from ust_asset_db.asset_inventory")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print("ERROR: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            
def validation(data):
    try:
        if "asset_tag" in data:
            if data["asset_tag"].split("-")[0] != "UST":
                raise Exception("asset tag must be start with UST-")
            
        if data["asset_type"] not in allowed_assert_type:
            raise Exception("given asset type is not allowed")
        
        if data["warranty_years"]<=0:
            raise Exception("Warrenty year should be greater than zero")
        
        if data["asset_status"] == "Assigned" and data["assigned_to"] == None:
            raise Exception("assigned to must not be null")
        
        if (data["asset_status"] == "Available" or data["asset_status"] == "Retired") and data["assigned_to"] != None:
            raise Exception("assigned to must be null")
        
        rows = get_all_assets()
        if "serial_number" in data:
            for row in rows:
                if row[3] == data["serial_number"]:
                    raise Exception("serial_number must be unique")
        if "asset_tag" in data:
            for row in rows:
                if row[1] == data["asset_tag"]:
                    raise Exception("asset_tag must be unique")
    except Exception as e:
        print("ERROR: ",e)
    else:
        return True
        
def create_asset():
    try:
        data = {
    "asset_tag" : "UST-LTP-0001",
    "asset_type" : "Laptop",
    "serial_number" : "1234",
    "manufacturer" : "",
    "model" : "",
    "purchase_date" : "2025-10-12",
    "warranty_years" : 2025,
    "assigned_to" : None,
    "asset_status" : "Available"
}
        
        asset_tag = data["asset_tag"]
        asset_type = data["asset_type"]
        serial_number = data["serial_number"]
        manufacturer = data["manufacturer"]
        model = data["model"]
        purchase_date = data["purchase_date"]
        warranty_years = data["warranty_years"]
        assigned_to  = data["assigned_to"]
        asset_status  = data["asset_status"]  
        last_updated = datetime.now()
        
        conn = get_connection()
        cursor = conn.cursor()
        if validation(data) != True:
            raise Exception
        cursor.execute("insert into ust_asset_db.asset_inventory (asset_tag,asset_type,serial_number,manufacturer,model,purchase_date,warranty_years,assigned_to,asset_status,last_updated) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(asset_tag,asset_type,serial_number,manufacturer,model,purchase_date,warranty_years,assigned_to,asset_status,last_updated))
        conn.commit()
        print("Asset inserted successfully: ")
        
        
    except Exception as e:
        print("ERROR: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed successfully")
        
def filter_rows(rows,filter):
    for row in rows:
        if row[9] == filter:
            print(f"Asset ID: {row[0]} | Asset Tag: {row[1]} | Asset Type: {row[2]} | Serial Number: {row[3]} | Manufacturer: {row[4]} | Model: {row[5]} | Purchase Date: {row[6]} | Warrenty_year {row[7]} | Assigned To: {row[8]} | Asset Status: {row[9]} | Last Updated {row[10]}")

def read_all_assets():
    rows = get_all_assets()
    print("Select filter\n1.Available\n2.Assigned\n3.Repair\n4.Retired\n5.ALL")
    choice = int(input("Enter choice:"))
    match choice:
        case 1:
            filter_rows(rows,"Available")
        case 2:
            filter_rows(rows,"Assigned")
        case 3:
            filter_rows(rows,"Repair")
        case 4:
            filter_rows(rows,"Retired")
        case 5:
            for row in rows:
                print(f"Asset ID: {row[0]} | Asset Tag: {row[1]} | Asset Type: {row[2]} | Serial Number: {row[3]} | Manufacturer: {row[4]} | Model: {row[5]} | Purchase Date: {row[6]} | Warrenty_year {row[7]} | Assigned To: {row[8]} | Asset Status: {row[9]} | Last Updated {row[10]}")

def read_asset_by_id(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM ust_asset_db.asset_inventory WHERE asset_id = %s;",(asset_id,))
        row = cursor.fetchone()
        if row:
            print(f"Asset ID: {row[0]} | Asset Tag: {row[1]} | Asset Type: {row[2]} | Serial Number: {row[3]} | Manufacturer: {row[4]} | Model: {row[5]} | Purchase Date: {row[6]} | Warrenty_year {row[7]} | Assigned To: {row[8]} | Asset Status: {row[9]} | Last Updated {row[10]}")            
            return row
        else:
            print("Employee record not found with emp_id ",asset_id)
    except Exception as e:
        print("Error: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed successfully")
       
def update_asset(asset_id):  
    try:
        data = {
    "asset_type" : "Laptop",
    "manufacturer" : "",
    "model" : "F15",
    "warranty_years" : 2025,
    "assigned_to" : None,
    "asset_status" : "Available"
    }
            
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM ust_asset_db.asset_inventory WHERE asset_id = %s;",(asset_id,))
        row = cursor.fetchone()
        if row:
            if validation(data) != True:
                raise Exception
            cursor.execute("UPDATE ust_asset_db.asset_inventory SET asset_type = %s,manufacturer = %s,model = %s,warranty_years = %s,assigned_to = %s,asset_status = %s WHERE asset_id = %s",(data["asset_type"],data["manufacturer"],data["model"],data["warranty_years"],data["assigned_to"],data["asset_status"],asset_id))
            conn.commit()
        else:
            print("Asset id does not exist")
        print("Asset updated successfully")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed successfully")  
            
def delete_asset(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        asset_to_be_deleted = read_asset_by_id(asset_id)
        if asset_to_be_deleted:
            cursor.execute("DELETE FROM ust_asset_db.asset_inventory WHERE asset_id = %s",(asset_id,))
            conn.commit()
            print("Employee deleted successfully")
        else:
            print("Employee record not found")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed successfully")
            
# create_asset()
# read_all_assets()
# read_asset_by_id(10)
# update_asset(10)
# delete_asset(10)

# output

# create asset
# Asset inserted successfully:
# Connection closed successfully

# read all assets
# Select filter
# 1.Available
# 3.Repair
# 4.Retired
# 5.ALL
# Enter choice:1
# ear 2025 | Assigned To: None | Asset Status: Available | Last Updated 2025-11-26 17:50:42

# reset asset by id
# ear 2025 | Assigned To: None | Asset Status: Available | Last Updated 2025-11-26 17:50:42
# Connection closed successfully

# update asset
# Asset updated successfully
# Connection closed successfully

# delete asset
# Asset ID: 10 | Asset Tag: UST-LTP-0001 | Asset Type: Laptop | Serial Number: 1234 | Manufacturer:  | Model: F15 | Purchase Date: 2025-10-12 | Warrenty_year 2025 | Assigned To: None | Asset Status: Available | Last Updated 2025-11-26 17:50:42
# Connection closed successfully
# Employee deleted successfully
# Connection closed successfully