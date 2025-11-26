import sys, os
# Add project root path for absolute imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Import validation helpers
from src.helpers.validatios import validate_asset_status,validate_asset_tag,validate_asset_type,validate_serial_number,validate_warrenty_years

# DB connection
from src.config.db_connection import get_connection
import pymysql

def create_asset(asset_tag,asset_type,serial_number,manufacture,model,purchase_date,warrenty_years,assigned_to,asset_status,last_updated):
    try:
        # Validate fields using helper functions
        asset_tag=validate_asset_tag(asset_tag)
        asset_type=validate_asset_type(asset_type)
        serial_number=validate_serial_number(serial_number)
        manufacture=manufacture
        model=model
        purchase_date=purchase_date
        warrenty_years=validate_warrenty_years(warrenty_years)
        asset_status,assigned_to=validate_asset_status(asset_status,assigned_to)
        last_updated=last_updated
       
        # Establish DB connection
        conn=get_connection()
        cursor=conn.cursor()
        
        # Insert query → last_updated handled by NOW()
        cursor.execute("INSERT INTO ust_asset_db.asset_inventory  (asset_tag,asset_type,serial_number,manufacture,model,purchase_date,warrenty_years,assigned_to,asset_status,last_updated)  VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())",(asset_tag,asset_type,serial_number,manufacture,model,purchase_date,warrenty_years,assigned_to,asset_status))
        
        print("hii")  # Debug print
        conn.commit()
        print("---------Inserted sucessfully----------")
    except Exception as e:
        print("Exception",e)

    

# TASK 2: READ ALL ASSET RECORDS
# Function: read_all_assets()
# Reads all assets and prints them in formatted output
def read_all_assets():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("SELECT *FROM ust_asset_db.asset_inventory")
        rows=cursor.fetchall()
        
        # Print each row in readable format
        for emp in rows:
            print(f"ASSET_ID:{emp[0]}, ASSET_TAG:{emp[1]}, ASSET_TYPE:{emp[2]}, SERIAL_NUMBER:{emp[3]}, manufacture:{emp[4]}, MODEL:{emp[5]}, PURCHASE_DATE:{emp[6]}, WARRENTY_YEARS:{emp[7]}, ASSIGNED_TO:{emp[8]}, ASSET_STATUS:{emp[9]}, LAST_UPDATED:{emp[10]}")
    except Exception as e:
        print("Exception:",e)
        

def read_asset_by_id(asset_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        # Fetch row by ID
        cursor.execute("SELECT * FROM ust_asset_db.asset_inventory WHERE ASSET_ID = %s",(asset_id,))
        row=cursor.fetchone()
        
        if row:
            print(row)
            return row
        else:
            print("Asset id is not matched")
    except Exception as e:
        print("Error",e)
    finally:
        # Close DB connection safely
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection closed sucessfully")
            
def update_asset(asset_id,asset_tag,asset_type,serial_number,manufacture,model,purchase_date,warrenty_years,assigned_to,asset_status):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        # Update specific asset record
        cursor.execute("UPDATE ust_asset_db.asset_inventory SET asset_tag=%s,asset_type=%s,serial_number=%s,manufacture=%s,model=%s,purchase_date=%s,warrenty_years=%s,assigned_to=%s,asset_status=%s WHERE asset_id=%s",(asset_tag,asset_type,serial_number,manufacture,model,purchase_date,warrenty_years,assigned_to,asset_status,asset_id))
        conn.commit()
        print("------------Updated sucessfully----------------------")

    except Exception as e:
        print("Exception",e)
    finally:
        # Close DB connection
        if conn.open:
            cursor.close()
            conn.close()
            
            
def delete_asset_by_id(asset_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        # First check if asset exists
        asset_to_be_deleted=read_asset_by_id(asset_id)
        
        if asset_to_be_deleted:
            # Delete if exists
            cursor.execute("DELETE FROM ust_asset_db.asset_inventory WHERE ASSET_ID=%s",(asset_id,))
            conn.commit()
            print("Asset data has been deleted",asset_id)
    except Exception as e:
        print("Exception",e)
    finally:
        # Close DB connection
        if conn.open:
            cursor.close()
            conn.close()
