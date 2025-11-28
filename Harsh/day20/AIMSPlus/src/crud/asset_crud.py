from datetime import datetime
from fastapi import HTTPException
from src.config.db_connection import get_connection
from src.models.asset_model import AssetInventory

def create_asset(new_asset: AssetInventory):
    # Insert a new asset record into the database
    try:
        conn = get_connection(); cursor = conn.cursor()
        query = """INSERT INTO asset_inventory (
            asset_tag, asset_type, serial_number, manufacturer, model,
            purchase_date, warranty_years, condition_status, assigned_to,
            location, asset_status, last_updated) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (new_asset.asset_tag, new_asset.asset_type, new_asset.serial_number,
                  new_asset.manufacturer, new_asset.model, new_asset.purchase_date,
                  new_asset.warranty_years, new_asset.condition_status, new_asset.assigned_to,
                  new_asset.location, new_asset.asset_status, datetime.now())
        cursor.execute(query, values); conn.commit()
        return {"message": "Asset created successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close(); 
        if conn: conn.close()

def get_all_assets(status: str | None = None):
    # Fetch all assets, optionally filtered by status
    try:
        conn = get_connection(); cursor = conn.cursor()
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_status=%s" if status else "SELECT * FROM asset_inventory", (status,) if status else ())
        return cursor.fetchall()
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close(); 
        if conn: conn.close()

def get_asset_by_id(asset_id: int):
    # Fetch a single asset by ID
    try:
        conn = get_connection(); cursor = conn.cursor()
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        result = cursor.fetchone()
        if not result: raise HTTPException(status_code=404, detail="Asset not found")
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close(); 
        if conn: conn.close()

def update_asset_by_id(asset_id: int, new_asset: AssetInventory):
    # Update all fields of an asset by ID
    try:
        conn = get_connection(); cursor = conn.cursor()
        cursor.execute("SELECT asset_id FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        if not cursor.fetchone(): raise HTTPException(status_code=404, detail="Asset not found")
        query = """UPDATE asset_inventory SET asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s,
                   model=%s, purchase_date=%s, warranty_years=%s, condition_status=%s, assigned_to=%s,
                   location=%s, asset_status=%s, last_updated=%s WHERE asset_id=%s"""
        values = (new_asset.asset_tag, new_asset.asset_type, new_asset.serial_number,
                  new_asset.manufacturer, new_asset.model, new_asset.purchase_date,
                  new_asset.warranty_years, new_asset.condition_status, new_asset.assigned_to,
                  new_asset.location, new_asset.asset_status, datetime.now(), asset_id)
        cursor.execute(query, values); conn.commit()
        return {"message": "Asset updated successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close(); 
        if conn: conn.close()

def update_asset_status(asset_id: int, new_status: str):
    # Update only the status of an asset
    try:
        conn = get_connection(); cursor = conn.cursor()
        cursor.execute("UPDATE asset_inventory SET asset_status=%s, last_updated=%s WHERE asset_id=%s",
                       (new_status, datetime.now(), asset_id)); conn.commit()
        if cursor.rowcount == 0: raise HTTPException(status_code=404, detail="Asset not found")
        return {"message": "Asset status updated successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close(); 
        if conn: conn.close()

def delete_asset(asset_id: int):
    # Delete an asset by ID
    try:
        conn = get_connection(); cursor = conn.cursor()
        cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,)); conn.commit()
        if cursor.rowcount == 0: raise HTTPException(status_code=404, detail="Asset not found")
        return {"message": "Asset deleted successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close(); 
        if conn: conn.close()

def search_assets(column_name: str, keyword: str):
    # Search assets by column and keyword
    try:
        conn = get_connection(); cursor = conn.cursor()
        allowed = ["asset_tag","asset_type","serial_number","manufacturer","model","purchase_date",
                   "warranty_years","condition_status","assigned_to","location","asset_status","last_updated"]
        if column_name not in allowed: raise ValueError("Invalid column name")
        cursor.execute(f"SELECT * FROM asset_inventory WHERE {column_name} LIKE %s", (f"%{keyword}%",))
        return cursor.fetchall()
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close(); 
        if conn: conn.close()

def count_assets():
    # Count total assets in the table
    try:
        conn = get_connection(); cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM asset_inventory")
        return cursor.fetchone()
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close(); 
        if conn: conn.close()
