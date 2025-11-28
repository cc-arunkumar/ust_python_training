import pymysql
from datetime import datetime
from fastapi import HTTPException, status
from src.config.db_connection import get_Connection
from ..exceptions.custom_exceptions import DatabaseConnectionException

# Define headers for asset fields
headers = [
    "asset_tag", "asset_type", "serial_number", "manufacturer", "model", "purchase_date",
    "warranty_years", "condition_status", "assigned_to", "location", "asset_status", "last_updated"
]
def get_all_assets(status):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_aims_plus.asset_inventory")
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No assets found")

        response = []
        if status == "":
            for row in rows:
                response.append(dict(zip(headers, row)))
            return response
        if status == "count":
            return {"count": len(rows)}
        else:
            for row in rows:
                if row[11] == status:
                    response.append(dict(zip(headers, row)))
            return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to get asset by ID
def get_by_id(asset_id):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM asset_inventory WHERE ASSET_ID=%s", (asset_id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found")
        return dict(zip(headers, row))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to create a single asset record
def create_asset(row):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO ust_aims_plus.asset_inventory(
            asset_tag, asset_type, serial_number,
            manufacturer, model, purchase_date, 
            warranty_years, condition_status, assigned_to,
            location, asset_status, last_updated
        ) VALUES (%s,%s,%s,
        %s,%s,%s,
        %s,%s,%s,
        %s,%s,%s)
        """
        data = (
            row.asset_tag, row.asset_type, row.serial_number, row.manufacturer,
            row.model, row.purchase_date, int(row.warranty_years), row.condition_status,
            row.assigned_to, row.location, row.asset_status, datetime.now()
        )
        cursor.execute(query, data)
        conn.commit()
        return {"message": "Asset record inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to update asset by ID
def update_by_id(asset_id, asset):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        query = """ 
        UPDATE asset_inventory SET asset_tag=%s, asset_type=%s, serial_number=%s,
            manufacturer=%s, model=%s, purchase_date=%s, 
            warranty_years=%s, condition_status=%s, assigned_to=%s,
            location=%s, asset_status=%s, last_updated=%s
        WHERE ASSET_ID=%s"""
        asset.last_updated = datetime.now()
        data = (
            asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
            asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
            asset.assigned_to, asset.location, asset.asset_status, asset.last_updated, asset_id
        )
        cursor.execute(query, data)
        conn.commit()
        return {"message": "Asset updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to update asset status by ID
def update_by_status(asset_id, status):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        query = "UPDATE asset_inventory SET asset_status=%s WHERE ASSET_ID=%s"
        cursor.execute(query, (status, asset_id))
        conn.commit()
        return get_by_id(asset_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to delete asset by ID
def delete_by_id(asset_id):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        query = "DELETE FROM asset_inventory WHERE ASSET_ID=%s"
        cursor.execute(query, (asset_id,))
        conn.commit()
        return {"message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to search assets by field and keyword
def get_by_search(field_type, keyword):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM asset_inventory WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No matching assets found")
        return [dict(zip(headers, row)) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to get count of all assets
def get_by_count():
    try:
        return {"count": len(get_all_assets(""))}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Function to get assets filtered by status
def get_assets_by_status(status):
    return get_all_assets(status)
