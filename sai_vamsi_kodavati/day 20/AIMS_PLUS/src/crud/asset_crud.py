import csv
from typing import Optional
from src.models.asset_model import AssetInventory
from src.config.db_connection import get_connection

# query = """
# INSERT INTO ust_aims_db.asset_inventory (
#     asset_tag, asset_type, serial_number, manufacturer, model,
#     purchase_date, warranty_years, condition_status, assigned_to,
#     location, asset_status,last_updated
# ) VALUES (
#     %s, %s, %s, %s, %s,
#     %s, %s, %s, %s,
#     %s, %s,NOW()
# )
# """
# try:
#     conn=get_connection()
#     cursor=conn.cursor()
#     with open("valid_rows.csv", "r", encoding="utf-8") as file:
#         reader = csv.DictReader(file)

#         for row in reader:
#             data = (
#                 row["asset_tag"],
#                 row["asset_type"],
#                 row["serial_number"],
#                 row["manufacturer"],
#                 row["model"],
#                 row["purchase_date"],
#                 row["warranty_years"],
#                 row["condition_status"],
#                 row["assigned_to"],
#                 row["location"],
#                 row["asset_status"]
#             )
#             cursor.execute(query, data)
    
#     conn.commit()

# except Exception as e:
#     print(f"Error",e)

# finally:
    
#     if conn:
#         cursor.close()
#         conn.close()
#         print("Connection closed successfully")
        
def insert_asset_to_db(new_asset: AssetInventory):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the serial_number already exists in the database
        cursor.execute("SELECT COUNT(*) FROM ust_aims_db.asset_inventory WHERE serial_number = %s", (new_asset.serial_number,))
        count = cursor.fetchone()[0]
        
        if count > 0:
            raise ValueError(f"Serial number {new_asset.serial_number} already exists.")
        
        # Proceed with insertion if no duplicate
        cursor.execute(
            """
            INSERT INTO ust_aims_db.asset_inventory(
                asset_tag, asset_type, serial_number, manufacturer, model, 
                purchase_date, warranty_years, condition_status, assigned_to, 
                location, asset_status, last_updated
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
            """, (
                new_asset.asset_tag,          
                new_asset.asset_type,        
                new_asset.serial_number,      
                new_asset.manufacturer,      
                new_asset.model,              
                new_asset.purchase_date,      
                new_asset.warranty_years,    
                new_asset.condition_status,  
                new_asset.assigned_to,      
                new_asset.location,          
                new_asset.asset_status
            )
        )
        conn.commit()
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        if conn.open:
            cursor.close()
            conn.close()


def read_all_assets(status_filter:Optional[str]=""):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if status_filter=="":
            cursor.execute("SELECT * FROM ust_aims_db.asset_inventory")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.asset_inventory WHERE asset_status=%s",(status_filter, ))
        
        row = cursor.fetchall()
        
        return row
    except Exception as e:
        raise ValueError
    
    finally:
        if conn:
            cursor.close()
            conn.close()


def read_asset_by_id(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM ust_aims_db.asset_inventory WHERE asset_id= %s", (asset_id,))
        row = cursor.fetchone()
        
        if row:
            return row
        else:
            return [False, f"Asset not found. {asset_id}"]
    except Exception as e:
        raise ValueError
    finally:
        if conn:
            cursor.close()
            conn.close()
    

def update_asset_by_id(asset_id:int,update_data:AssetInventory):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if read_asset_by_id(asset_id):
            cursor.execute("UPDATE ust_aims_db.asset_inventory SET asset_tag=%s,asset_type=%s,serial_number=%s, manufacturer=%s, model=%s, warranty_years=%s,condition_status=%s, assigned_to=%s,location=%s, asset_status=%s WHERE asset_id=%s", 
                        (update_data.asset_tag,update_data.asset_type,update_data.serial_number,update_data.manufacturer, update_data.model, update_data.warranty_years,update_data.condition_status, update_data.assigned_to,update_data.location, update_data.asset_status, update_data.asset_id))
        
            conn.commit()
            return True
        else:
            raise ValueError
    except Exception as e:
        raise ValueError
    finally:
        if conn:
            cursor.close()
            conn.close()
            
            
def delete_asset(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        
        if read_asset_by_id(asset_id):
            cursor.execute("DELETE FROM ust_aims_db.asset_inventory WHERE asset_id = %s", (asset_id,))
            conn.commit()
            return True
        else:
            # If the asset is not found, print the error message
            raise ValueError
        
    except Exception as e:
        # Catch and print any exceptions
        raise ValueError
    finally:
        # Close the database connection
        if conn:
            cursor.close()
            conn.close()
            # print("Connection closed successfully")

def search_assets(field_type:str,keyword : str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM ust_aims_db.asset_inventory WHERE {field_type} LIKE %s",(f'%{keyword}%',))
        data = cursor.fetchall()
        return data
   
    except Exception as e:
        raise Exception(f"Error: {e}")
   
    finally:
        if conn.open:
            cursor.close()
            conn.close()








# valid_rows_asset = []
# invalid_rows_asset = []

# required_fields_asset = [
#     "asset_tag", "asset_type", "serial_number", "manufacturer", "model", 
#     "purchase_date", "warranty_years", "condition_status", "assigned_to", 
#     "location", "asset_status"
# ]

# with open("asset_inventory.csv", "r") as file:
#     csv_reader = csv.DictReader(file)

#     for row in csv_reader:
        
#         try:
#             valid = AssetInventory(**row)
#             valid_rows_asset.append(valid.model_dump())  
            
#         except Exception as e:
#             row['error'] = str(e)  
#             invalid_rows_asset.append(row)

# fieldnames_asset_invalid = [
#     "asset_id", "asset_tag", "asset_type", "serial_number", "manufacturer", "model", 
#     "purchase_date", "warranty_years", "condition_status", "assigned_to", "location", 
#     "asset_status", "last_updated", "error" 
# ]
# fieldnames_asset_valid = [
#      "asset_tag", "asset_type", "serial_number", "manufacturer", "model", 
#     "purchase_date", "warranty_years", "condition_status", "assigned_to", "location", 
#     "asset_status", "last_updated"
# ]

# with open("valid_rows.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames_asset_valid)
#     writer.writeheader()
    
#     for row in valid_rows_asset:
#         row.pop('asset_id', None)
#         if 'last_updated' in row:
#             row['last_updated'] = row['last_updated'].strftime('%Y-%m-%d %H:%M:%S') 
            
#         writer.writerow(row)

# with open("invalid_rows.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames_asset_invalid)
#     writer.writeheader()
#     for row in invalid_rows_asset:
#         writer.writerow(row)
    

