from config import db_connection
from helpers import validators
from pymysql import Error
from tabulate import tabulate

# CRUD operations for the asset_inventory table (short comments)

# Create a new asset record after validations
def create_asset_records(asset_tag,asset_type,serial_number,manufacturer,model,purchase_date,warranty_years,asset_status,assigned_to=""):
    validations = validators.table_validations(asset_tag,asset_type,warranty_years,asset_status,assigned_to)
    if validations == "Data is Valid":
        try:
            conn = db_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO ust_asset_db.asset_inventory (asset_tag,asset_type,serial_number,manufacturer,model,purchase_date,warranty_years,assigned_to,asset_status,last_updated) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())",(asset_tag,asset_type,serial_number,manufacturer,model,purchase_date,warranty_years,assigned_to,asset_status))
            conn.commit()
        except Exception as e:
            print('Error:',e)
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed Successfully!")
    else:
        print(validations)

# Read and print all asset records in a table format
def read_all_assets():
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute("select * from ust_asset_db.asset_inventory")
        data = cursor.fetchall()
        print(tabulate(data, headers=['asset_id','asset_tag','asset_type','serial_number','manufacturer','model','purchase_date','warranty_years','assigned_to','asset_status','last_updated']))
        
    except Error as e:
        print("Error:",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection Closed Successfully!")

# Read a single asset by id; returns True if found else False
def read_asset_by_id(asset_id):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s",(asset_id))
        row = cursor.fetchone()
        if row:
            print(row)
            return True

        else:
            print("Employee ID Not Found")
            return False
        
    except Error as e:
        print("Error:",e)
        
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection Closed Successfully!")


# Update an existing asset after validations
def update_asset(asset_id,asset_tag,asset_type,serial_number,manufacturer,model,purchase_date,warranty_years,asset_status,assigned_to=""):
    validations = validators.table_validations(asset_tag,asset_type,warranty_years,asset_status,assigned_to)
    if validations == "Data is Valid":
        try:
            conn = db_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
        UPDATE ust_asset_db.asset_inventory
        SET asset_tag = %s,
            asset_type = %s,
            serial_number = %s,
            manufacturer = %s,
            model = %s,
            purchase_date = %s,
            warranty_years = %s,
            assigned_to = %s,
            asset_status = %s,
            last_updated = NOW()
        WHERE asset_id = %s
    """, (asset_tag, asset_type, serial_number, manufacturer, model,
        purchase_date, warranty_years, assigned_to, asset_status, asset_id))

            conn.commit()
            print("Record Updated Successfully!")
        except Error as e:
            print('Error:',e)
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Connection Closed Successfully!")
    else:
        print(validations)

# Delete an asset by id if it exists
def delete_asset_by_id(asset_id:int):
    try:
        conn=db_connection.get_connection()
        cursor=conn.cursor()
        if read_asset_by_id(asset_id):
            cursor.execute(" DELETE FROM ust_asset_db.asset_inventory WHERE asset_id=%s",(asset_id,))
            conn.commit()
            print("Asset Record Deleted succesfully")
        else :
            print("ID NOT Exists to delete")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        if conn.open: #conn.is_connected
            cursor.close()
            conn.close()
