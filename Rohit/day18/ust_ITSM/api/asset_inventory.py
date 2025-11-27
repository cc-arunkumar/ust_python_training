import pymysql
from db_connection.db import get_connection
import datetime
from fastapi import HTTPException
# def create_task( asset_tag, asset_type, serial_number, manufacturer, model,
#                 purchase_date, warranty_years, condition_status,
#                 assigned_to, location, asset_status):
#     conn = None
#     cursor = None
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         sql = """
#         INSERT INTO ust_asset_inventory.asset_inventory (
#              asset_tag, asset_type, serial_number, manufacturer,
#             model, purchase_date, warranty_years, condition_status,
#             assigned_to, location, asset_status, last_updated
#         )
#         VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """

#         values = ( asset_tag, asset_type, serial_number, manufacturer,
#                   model, purchase_date, warranty_years, condition_status,
#                   assigned_to, location, asset_status, last_updated)

#         cursor.execute(sql, values)
#         conn.commit()

#         # return {"message": "Asset inserted successfully", "asset_id": asset_id}

#     except Exception as e:
#         if conn: conn.rollback()
#         raise HTTPException(status_code=500, detail=f"Error inserting asset: {str(e)}")

#     finally:
#         if cursor: cursor.close()
#         if conn: conn.close()
            
def get_task():
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # <-- DictCursor
        sql = "SELECT * FROM ust_asset_inventory.asset_inventory"
        cursor.execute(sql)
        ans = cursor.fetchall()   # returns list of dicts
        return ans
    except Exception as e:
        print("Error fetching tasks:", e)
        return []
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def get_task_by_id(asset_id: int):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor) 

        sql = "SELECT * FROM ust_asset_inventory.asset_inventory WHERE asset_id = %s"
        cursor.execute(sql, (asset_id,))
        row = cursor.fetchone()

        if not row:
            raise HTTPException(status_code=404, detail=f"Asset with id {asset_id} not found")

        return row

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching asset: {str(e)}")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def get_assets_by_status(status: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)  

        sql = "SELECT * FROM ust_asset_inventory.asset_inventory WHERE asset_status = %s"
        cursor.execute(sql, (status,))
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail=f"No assets found with status '{status}'")

        return rows

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching assets: {str(e)}")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()
def search_assets_by_column(column_name: str, value: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        allowed_columns = [
            "asset_tag", "asset_type", "serial_number", "manufacturer",
            "model", "purchase_date", "warranty_years", "condition_status",
            "assigned_to", "location", "asset_status"
        ]

        if column_name not in allowed_columns:
            raise HTTPException(status_code=400, detail=f"Invalid column name: {column_name}")

        # Build query dynamically with safe column name
        sql = f"SELECT * FROM ust_asset_inventory.asset_inventory WHERE {column_name} = %s"
        cursor.execute(sql, (value,))
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail=f"No assets found where {column_name} = '{value}'")

        return rows

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching assets: {str(e)}")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def count_assets():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM ust_asset_inventory.asset_inventory"
        cursor.execute(sql)
        total = cursor.fetchone()[0]
        return total

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error counting assets: {str(e)}")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def update_asset(asset_id, asset_tag, asset_type, serial_number, manufacturer, model,
                 purchase_date, warranty_years, condition_status,
                 assigned_to, location, asset_status):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE ust_asset_inventory.asset_inventory
        SET asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s,
            model=%s, purchase_date=%s, warranty_years=%s, condition_status=%s,
            assigned_to=%s, location=%s, asset_status=%s
        WHERE asset_id=%s
        """

        values = (
            asset_tag,
            str(asset_type),
            serial_number,
            str(manufacturer),
            model,
            purchase_date.strftime("%Y-%m-%d"),
            warranty_years,
            str(condition_status),
            assigned_to,
            str(location),
            str(asset_status),
            asset_id,
        )

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Asset with id {asset_id} not found")

        return {"message": "Asset updated successfully", "asset_id": asset_id}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating asset: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def update_asset_status(asset_id, asset_status):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "UPDATE ust_asset_inventory.asset_inventory SET asset_status=%s WHERE asset_id=%s"
        cursor.execute(sql, (str(asset_status), asset_id))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Asset with id {asset_id} not found")

        return {"message": "Asset status updated successfully", "asset_id": asset_id, "asset_status": asset_status}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating asset status: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def delete_asset(asset_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "DELETE FROM ust_asset_inventory.asset_inventory WHERE asset_id=%s"
        cursor.execute(sql, (asset_id,))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Asset with id {asset_id} not found")

        return {"message": "Asset deleted successfully", "asset_id": asset_id}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting asset: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()