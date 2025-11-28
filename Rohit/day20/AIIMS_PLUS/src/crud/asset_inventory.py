import pymysql  # Import pymysql to connect and interact with MySQL databases
from src.config.db_connection import get_connection # Import custom function to get DB connection
import datetime  # Import datetime for handling date values
from fastapi import HTTPException  # Import HTTPException for API error handling in FastAPI
            
# Function to fetch all tasks (all assets from asset_inventory table)

def create_task(asset_id, asset_tag, asset_type, serial_number, manufacturer, model,
                purchase_date, warranty_years, condition_status,
                assigned_to, location, asset_status):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO ust_asset_inventory.asset_inventory (
            asset_id, asset_tag, asset_type, serial_number, manufacturer,
            model, purchase_date, warranty_years, condition_status,
            assigned_to, location, asset_status
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            asset_id,
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
        )

        cursor.execute(sql, values)
        conn.commit()
        return {"message": "Asset inserted successfully", "asset_tag": asset_tag}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error inserting asset: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def get_task():
    try:
        conn = get_connection()  # Establish database connection
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # Use DictCursor to return rows as dictionaries
        sql = "SELECT * FROM ust_asset_inventory.asset_inventory"  # SQL query to fetch all assets
        cursor.execute(sql)  # Execute query
        ans = cursor.fetchall()   # Fetch all rows as list of dicts
        return ans  # Return result
    except Exception as e:
        print("Error fetching tasks:", e)  # Print error for debugging
        return []  # Return empty list if error occurs
    finally:
        if cursor: cursor.close()  # Close cursor if it exists
        if conn: conn.close()  # Close connection if it exists

# Function to fetch a single asset by its ID
def get_task_by_id(asset_id: int):
    conn = None
    cursor = None
    try:
        conn = get_connection()  # Establish connection
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # DictCursor for dict results

        sql = "SELECT * FROM ust_asset_inventory.asset_inventory WHERE asset_id = %s"  # Query with placeholder
        cursor.execute(sql, (asset_id,))  # Execute query with asset_id parameter
        row = cursor.fetchone()  # Fetch single row

        if not row:  # If no asset found
            raise HTTPException(status_code=404, detail=f"Asset with id {asset_id} not found")

        return row  # Return asset row

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching asset: {str(e)}")  # Raise server error

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Function to fetch assets by their status (e.g., Available, Assigned)
def get_assets_by_status(status: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)  

        sql = "SELECT * FROM ust_asset_inventory.asset_inventory WHERE asset_status = %s"
        cursor.execute(sql, (status,))
        rows = cursor.fetchall()

        if not rows:  # If no assets found
            raise HTTPException(status_code=404, detail=f"No assets found with status '{status}'")

        return rows

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching assets: {str(e)}")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Function to search assets by a specific column and value
def search_assets_by_column(column_name: str, value: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        # Allowed columns to prevent SQL injection
        allowed_columns = [
            "asset_tag", "asset_type", "serial_number", "manufacturer",
            "model", "purchase_date", "warranty_years", "condition_status",
            "assigned_to", "location", "asset_status"
        ]

        if column_name not in allowed_columns:  # Validate column name
            raise HTTPException(status_code=400, detail=f"Invalid column name: {column_name}")

        # Build query dynamically with safe column name
        sql = f"SELECT * FROM ust_asset_inventory.asset_inventory WHERE {column_name} = %s"
        cursor.execute(sql, (value,))
        rows = cursor.fetchall()

        if not rows:  # If no results found
            raise HTTPException(status_code=404, detail=f"No assets found where {column_name} = '{value}'")

        return rows

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching assets: {str(e)}")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Function to count total number of assets
def count_assets():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM ust_asset_inventory.asset_inventory"  # Count query
        cursor.execute(sql)
        total = cursor.fetchone()[0]  # Fetch count value
        return total

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error counting assets: {str(e)}")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Function to update an asset record by ID
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

        # Prepare values tuple
        values = (
            asset_tag,
            str(asset_type),
            serial_number,
            str(manufacturer),
            model,
            purchase_date.strftime("%Y-%m-%d"),  # Format date to YYYY-MM-DD
            warranty_years,
            str(condition_status),
            assigned_to,
            str(location),
            str(asset_status),
            asset_id,
        )

        cursor.execute(sql, values)  # Execute update query
        conn.commit()  # Commit changes

        if cursor.rowcount == 0:  # If no rows updated
            raise HTTPException(status_code=404, detail=f"Asset with id {asset_id} not found")

        return {"message": "Asset updated successfully", "asset_id": asset_id}

    except Exception as e:
        if conn: conn.rollback()  # Rollback if error occurs
        raise HTTPException(status_code=500, detail=f"Error updating asset: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Function to update only the asset status
def update_asset_status(asset_id, asset_status):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "UPDATE ust_asset_inventory.asset_inventory SET asset_status=%s WHERE asset_id=%s"
        cursor.execute(sql, (str(asset_status), asset_id))
        conn.commit()

        if cursor.rowcount == 0:  # If no rows updated
            raise HTTPException(status_code=404, detail=f"Asset with id {asset_id} not found")

        return {"message": "Asset status updated successfully", "asset_id": asset_id, "asset_status": asset_status}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating asset status: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Function to delete an asset by ID
def delete_asset(asset_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "DELETE FROM ust_asset_inventory.asset_inventory WHERE asset_id=%s"
        cursor.execute(sql, (asset_id,))
        conn.commit()

        if cursor.rowcount == 0:  # If no rows deleted
            raise HTTPException(status_code=404, detail=f"Asset with id {asset_id} not found")

        return {"message": "Asset deleted successfully", "asset_id": asset_id}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting asset: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
