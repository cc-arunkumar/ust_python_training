import sys
import os
from typing import Optional
# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'src'))

# Now, you can import the models module
from config.db_connection import get_connection
from datetime import datetime
from pydantic import BaseModel
import pymysql

# 1
def get_asset_data():
    conn=get_connection()
    cursor=conn.cursor()
    query="""
    SELECT* FROM aims_db.assets_inventory
    """
    # print(query)
    cursor.execute(query)
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    return rows 
    


# 2 GET /assets/{id} Get by asset_id
def get_asset_data_by_id(id):
    conn=get_connection()
    cursor=conn.cursor()
    
    query="""
    SELECT * FROM aims_db.assets_inventory 
    WHERE ASSET_ID=%s
    """
    cursor.execute(query,(id))
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result


# 3 DELETE /assets/{id} Delete asset
def delete_asset_by_id(id):
    try:
        # Establish connection
        conn = get_connection()
        cursor = conn.cursor()

        # Prepare DELETE query
        query = """
        DELETE FROM aims_db.assets_inventory
        WHERE ASSET_ID = %s
        """
        
        # Execute the query with the provided id
        cursor.execute(query, (id,))
        
        # Commit the changes to the database
        conn.commit()

        # Check if the record was deleted
        if cursor.rowcount == 0:
            print(f"No asset found with ID: {id}")
        else:
            print(f"Asset with ID {id} successfully deleted.")

    except Exception as e:
        # print(f"Error: {e}")
        pass
    
    finally:
        cursor.close()
        conn.close()

# 4
def assets_count_api():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT COUNT(*) FROM aims_db.assets_inventory;
        """

        cursor.execute(query)
        result = cursor.fetchone()
        # result=int(result)
        
        return result

    except Exception as e:
        # print("Exception:", e)
        raise  

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
  
def get_assets_list(status):
    try:
        asset_status_list = ['Available', 'Assigned', 'Repair', 'Retired']
        if status in asset_status_list:
            conn=get_connection()
            cursor=conn.cursor()
            
            query="""
            SELECT * FROM aims_db.assets_inventory 
            WHERE asset_status=%s
            """
            
            cursor.execute(query,(status,))
            result=cursor.fetchall()
            # print(result)
            return result
    except Exception as e:
        # print("Exception:",e)
        pass
    finally:
        cursor.close()
        conn.close()
        
def create_asset(asset_detail):
    try:
        # Get the current time for the 'last_updated' field
        current_time = datetime.now()
        
        # Establish database connection
        conn = get_connection()
        cursor = conn.cursor()
        
        # Define the SQL query
        query = """
            INSERT INTO aims_db.assets_inventory (
                asset_tag, asset_type, serial_number, 
                manufacturer, model, purchase_date, 
                warranty_years, condition_status, assigned_to,
                location, asset_status, last_updated
            )
            VALUES 
            (%s, %s, %s, 
             %s, %s, %s, 
             %s, %s, %s, 
             %s, %s, %s)
        """
        
        # Define parameters for the SQL query
        parameters = (
            asset_detail.asset_tag, asset_detail.asset_type, asset_detail.serial_number,
            asset_detail.manufacturer, asset_detail.model, asset_detail.purchase_date,
            asset_detail.warranty_years, asset_detail.condition_status, asset_detail.assigned_to,
            asset_detail.location, asset_detail.asset_status, current_time
        )
        
        
        cursor.execute(query, parameters)
        
        # Commit the changes to the database
        conn.commit()
        
        # Check if the insert was successful
        if cursor.rowcount > 0:
            print(f"Successfully inserted asset: {asset_detail.asset_tag}")
        else:
            print(f"No rows affected. Check your SQL or table constraints.")
        
        return {"message": "Asset created successfully!", "asset": asset_detail.dict(exclude_unset=True)}

    except Exception as e:
        # print("Exception:", e)
        return {"message": "Error creating asset", "error": str(e)}

    finally:
        try:
            cursor.close()
            conn.close()
        except (NameError, AttributeError):
            pass  # In case cursor or conn were never initialized

def check_duplicate_serial_number(serial_number: str, asset_id: Optional[int] = None):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # If asset_id is provided, we exclude the current asset from the duplicate check
        if asset_id:
            query = """
                SELECT COUNT(*) FROM aims_db.assets_inventory 
                WHERE serial_number = %s AND id != %s
            """
            cursor.execute(query, (serial_number, asset_id))
        else:
            query = "SELECT COUNT(*) FROM aims_db.assets_inventory WHERE serial_number = %s"
            cursor.execute(query, (serial_number,))
        
        result = cursor.fetchone()
        if result[0] > 0:
            return True  # Duplicate found
        return False  # No duplicates

    except Exception as e:
        return {"message": "Error checking for duplicate serial number", "error": str(e)}

    finally:
        cursor.close()
        conn.close()

## 5 PUT /assets/{id} Update full record
def update_asset_by_id(asset_id: int, asset_detail: BaseModel):
    try:
        # Check if the serial_number is being changed, and if it is, check for duplicates
        existing_asset = get_asset_data_by_id(asset_id)
        if existing_asset and asset_detail.serial_number != existing_asset['serial_number']:
            # If serial_number is being updated, check for duplicate serial number
            if check_duplicate_serial_number(asset_detail.serial_number, asset_id):
                return {"message": "Duplicate serial number found"}

        current_time = datetime.now()
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE aims_db.assets_inventory 
            SET 
                asset_tag = %s,
                asset_type = %s,
                serial_number = %s,
                manufacturer = %s,
                model = %s,
                purchase_date = %s,
                warranty_years = %s,
                condition_status = %s,
                assigned_to = %s,
                location = %s,
                asset_status = %s,
                last_updated = %s
            WHERE id = %s
        """
        
        parameters = (
            asset_detail.asset_tag, asset_detail.asset_type, asset_detail.serial_number,
            asset_detail.manufacturer, asset_detail.model, asset_detail.purchase_date,
            asset_detail.warranty_years, asset_detail.condition_status, asset_detail.assigned_to,
            asset_detail.location, asset_detail.asset_status, current_time, asset_id
        )

        cursor.execute(query, parameters)
        conn.commit()

        if cursor.rowcount == 0:
            return {"message": "Asset not found for update"}

        return {"message": "Asset updated successfully!"}

    except Exception as e:
        return {"message": "Error updating asset", "error": str(e)}

    finally:
        cursor.close()
        conn.close()

#  6 PATCH /assets/{id}/status Update only status
def update_asset_status_by_id(asset_id: int, new_status: str):
    try:
        # Define valid asset statuses
        valid_statuses = ['Available', 'Assigned', 'Repair', 'Retired']

        # Check if the new status is valid
        if new_status not in valid_statuses:
            return {"message": f"Invalid asset status. Must be one of {', '.join(valid_statuses)}"}

        # Establish database connection
        conn = get_connection()
        cursor = conn.cursor()

        # Check if the asset exists in the database
        cursor.execute("SELECT * FROM aims_db.assets_inventory WHERE asset_id = %s", (asset_id,))
        existing_asset = cursor.fetchone()

        if not existing_asset:
            return {"message": "Asset not found for update"}

        # Prepare the SQL query to update the asset status
        query = """
            UPDATE aims_db.assets_inventory 
            SET asset_status = %s, last_updated = %s
            WHERE asset_id = %s
        """
        
        # Current time for `last_updated`
        current_time = datetime.now()
        
        # Execute the update query
        cursor.execute(query, (new_status, current_time, asset_id))
        conn.commit()

        if cursor.rowcount == 0:
            return {"message": "No asset status updated. Please check the asset ID."}

        return {"message": "Asset status updated successfully!"}

    except Exception as e:
        return {"message": "Error updating asset status", "error": str(e)}

    finally:
        cursor.close()
        conn.close()
        
        
        
# serach ny keyword
def search_assets(keyword: str):
    try:
        # Establish database connection
        conn = get_connection()
        cursor = conn.cursor()

        # Search query to search asset_tag, model, and manufacturer for the given keyword
        query = """
            SELECT * FROM aims_db.assets_inventory
            WHERE asset_tag LIKE %s OR model LIKE %s OR manufacturer LIKE %s
        """

        # Use '%' to allow partial matches
        like_keyword = f"%{keyword}%"

        cursor.execute(query, (like_keyword, like_keyword, like_keyword))
        results = cursor.fetchall()

        if not results:
            return {"message": "No assets found matching the keyword"}

        # Map the results to a dictionary for easier consumption
        assets = []
        for result in results:
            assets.append({
                "id": result[0],
                "asset_tag": result[1],
                "asset_type": result[2],
                "serial_number": result[3],
                "manufacturer": result[4],
                "model": result[5],
                "purchase_date": result[6],
                "warranty_years": result[7],
                "condition_status": result[8],
                "assigned_to": result[9],
                "location": result[10],
                "asset_status": result[11],
                "last_updated": result[12]
            })

        return {"assets": assets}

    except Exception as e:
        return {"message": "Error searching assets", "error": str(e)}

    finally:
        cursor.close()
        conn.close()
