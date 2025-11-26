import pymysql
from src.config.db_connection import get_connection
from src.helpers.validators import validate_asset

def create_asset(asset_tag, asset_type, serial_number, manufacturer, model,
                 purchase_date, warranty_years, assigned_to, asset_status):
    conn = None
    cursor = None
    try:
        validate_asset(asset_tag, asset_type, warranty_years, assigned_to, asset_status)
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO asset_inventory
        (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date,
         warranty_years, assigned_to, asset_status, last_updated)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())
        """
        cursor.execute(sql, (asset_tag, asset_type, serial_number, manufacturer, model,
                             purchase_date, warranty_years, assigned_to, asset_status))
        conn.commit()
        print("Asset created successfully with ID:", cursor.lastrowid)

    except pymysql.MySQLError as e:
        print("Database Error:", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def read_all_assets(status_filter="ALL"):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        if(status_filter=="ALL"):
            sql="SELECT * FROM asset_inventory ORDER BY asset_id ASC"
            cursor.execute(sql)
        else:
            sql="SELECT * FROM asset_inventory where asset_status=%s ORDER BY asset_id ASC"
            cursor.execute(sql)
        rows=cursor.fetchall()
        if not rows:
            print("No asset found")
        else:
            for asset in rows:
                print(f"ID: {asset[0]} | TAG: {asset[1]} | TYPE: {asset[2]} | SERIAL: {asset[3]} | "
                  f"MANUFACTURER: {asset[4]} | MODEL: {asset[5]} | PURCHASE_DATE: {asset[6]} | "
                  f"WARRANTY: {asset[7]} | ASSIGNED_TO: {asset[8]} | STATUS: {asset[9]} | "
                  f"LAST_UPDATED: {asset[10]}")
    except Exception as e:
         print("Error: ",e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Connection closed successfully !")
def read_asset_by_id(asset_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * from asset_inventory where asset_id=%s",(asset_id, ))
        row=cursor.fetchone()
        
        if not row:
            print("Asset not found.")
        else:
            for asset in row:
                 print(f"ID: {asset[0]} | TAG: {asset[1]} | TYPE: {asset[2]} | SERIAL: {asset[3]} | "
                  f"MANUFACTURER: {asset[4]} | MODEL: {asset[5]} | PURCHASE_DATE: {asset[6]} | "
                  f"WARRANTY: {asset[7]} | ASSIGNED_TO: {asset[8]} | STATUS: {asset[9]} | "
                  f"LAST_UPDATED: {asset[10]}")
    except Exception as e:
        print("Error: ",e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
def update_asset(asset_id, asset_type=None, manufacturer=None, model=None,warranty_years=None, asset_status=None, assigned_to=None):
    try:
        
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE asset_inventory SET asset_type=%s , manufacturer=%s , model=%s , warranty_years=%s , asset_status=%s , assigned_to=%s where asset_id=%s",(asset_type, manufacturer, model,warranty_years, asset_status, assigned_to,asset_id))
        conn.commit()
    except Exception as e:
        print("Error: ",e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
def delete_by_id(asset_id, asset_type=None, manufacturer=None, model=None,warranty_years=None, asset_status=None, assigned_to=None):
    try:
        conn= get_connection()
        cursor=conn.cursor()
        asset_to_be_deleted=read_asset_by_id(asset_id)
        if asset_to_be_deleted!=None:          
            cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
            conn.commit()
            
        else:
            print("Asset_id not found")
            
    except Exception as e:
        print("Exception while deleting the asset", e)
        
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        
