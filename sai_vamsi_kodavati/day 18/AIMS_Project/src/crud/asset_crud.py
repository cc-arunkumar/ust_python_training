from typing import Optional

import pymysql

from tabulate import tabulate

from config.db_connection import get_connection

from helpers.validators import validate_asset

 

 

def create_asset(asset_tag: str, asset_type: str, serial_number: str, manufacturer: str, model: str, purchase_date: str, warranty_years: int, assigned_to:Optional[str], asset_status: str):

    try:

        conn=get_connection()

        validate_asset(conn,asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status)

        cursor=conn.cursor()

        cursor.execute("""

            INSERT INTO ust_asset_db.asset_inventory (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status, last_updated)

            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())

        """, (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status))

        conn.commit()

        asset_id = cursor.lastrowid

        print(f"Asset created successfully : {asset_id}")

    except Exception as e:

        print("Error: ",e)

    finally:

        if conn:

            cursor.close()

            conn.close()

            print("Connection closed successfully")

           

           

def read_all_assets(status_filter="ALL"):

    try:

        conn = get_connection()

        cursor = conn.cursor()

       

        if status_filter == "ALL":

            cursor.execute("SELECT * FROM asset_inventory ORDER BY asset_id ASC")

        else:

            cursor.execute("SELECT * FROM asset_inventory WHERE asset_status = %s ORDER BY asset_id ASC", (status_filter,))

       

        row = cursor.fetchall()

       

        if not row:

            print("No assets found.")

        else:

            print(tabulate(row,headers=["asset_id","asset_tag", "asset_type", "serial_number", "manufacturer", "model", "purchase_date", "warranty_years", "assigned_to", "asset_status","last_updated"]))

   

    except Exception as e:

        print(f"Error: {e}")

   

    finally:

        if conn:

            cursor.close()

            conn.close()

            print("Connection closed successfully")

 

 

def read_asset_by_id(asset_id):

    try:

        conn=get_connection()

        cursor=conn.cursor()

        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id= %s",(asset_id, ))

        row=cursor.fetchone()


        if row:

            print("Read asset by asset_id: ",end=" ")

            return row

 
        else:

            return [False,f"“Asset not found. {asset_id}"]

    except Exception as e:

        print("Error: ",e)

    finally:

        if conn:

            cursor.close()

            conn.close()

            print("Connection closed successfully") 

def update_asset(asset_id,asset_type,manufacturer,model,warranty_years,asset_status,assigned_to):

    try:

        conn=get_connection()

        cursor=conn.cursor()

        cursor.execute("UPDATE ust_asset_db.asset_inventory SET asset_type=%s,manufacturer=%s,model=%s,warranty_years=%s,asset_status=%s,assigned_to=%s WHERE asset_id=%s",(asset_type,manufacturer,model,warranty_years,asset_status,assigned_to,asset_id))

       

        conn.commit()

        print("Employee record updated successfully")

    except Exception as e:

        print("Error: ",e)

    finally:

        if conn:

            cursor.close()

            conn.close()

            print("Connection closed successfully")

           

 

def delete_asset(asset_id):

    try:

        conn=get_connection()

        cursor=conn.cursor()

        to_be_deleted,msg=read_asset_by_id(asset_id)

        if to_be_deleted:

            cursor.execute("DELETE FROM ust_asset_db.asset_inventory WHERE asset_id =%s",(asset_id, ))

            conn.commit()

            print("Asset record deleted successfully!")

        else:

            print(msg)

    except Exception as e:

        print("Error: ",e)

    finally:

        if conn:

            cursor.close()

            conn.close()

            print("Connection closed successfully")


