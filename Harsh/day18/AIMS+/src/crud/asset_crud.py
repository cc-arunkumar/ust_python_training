from src.config.db_connection import get_connection
from src.models.asset_model import AssetInventory

def create_asset(asset: AssetInventory):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO asset_inventory (
            asset_id, asset_tag, asset_type, serial_number, manufacturer, model,
            purchase_date, warranty_years, condition_status, assigned_to,
            location, asset_status, last_updated
        ) VALUES (
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, 
            %s, %s, %s)
        """

        values = (
            asset.asset_id, asset.asset_tag, asset.asset_type, asset.serial_number,
            asset.manufacturer, asset.model, asset.purchase_date, asset.warranty_years,
            asset.condition_status, asset.assigned_to, asset.location,
            asset.asset_status, asset.assigned_to
        )

        cursor.execute(query, values)
        conn.commit()
        return {"status": "success", "message": "Asset created successfully"}

    except Exception as e:
        print ("Error:",e)
    finally:
        cursor.close()
        conn.close()
        
def read_all_asset():
    print("read_all_asset called")
    assets = []
    try:
        conn = get_connection()
        cursor = conn.cursor()   

        query = "SELECT * FROM asset_inventory"
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            asset = AssetInventory(
                asset_id=row[0],
                asset_tag=row[1],
                asset_type=row[2],
                serial_number=row[3],
                manufacturer=row[4],
                model=row[5],
                purchase_date=row[6],
                warranty_years=row[7],
                condition_status=row[8],
                assigned_to=row[9],
                location=row[10],
                asset_status=row[11],
                last_updated=row[12],
            )
            assets.append(asset)

        return assets

    except Exception as e:
        print ("Error:",e)
    finally:
        cursor.close()
        conn.close()
        
def update_asset(asset: AssetInventory):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE asset_inventory
        SET asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s, model=%s,
            purchase_date=%s, warranty_years=%s, condition_status=%s, assigned_to=%s,
            location=%s, asset_status=%s, last_updated=%s
        WHERE asset_id=%s
        """

        values = (
            asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
            asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
            asset.assigned_to, asset.location, asset.asset_status, asset.last_updated,
            asset.asset_id
        )

        cursor.execute(query, values)
        conn.commit()
        return {"status": "success", "message": "Asset updated successfully"}

    except Exception as e:
        print ("Error:",e)
    finally:
        cursor.close()
        conn.close()

def delete_asset(asset_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM asset_inventory WHERE asset_id=%s"
        cursor.execute(query, (asset_id,))
        conn.commit()

        return {"status": "success", "message": "Asset deleted successfully"}

    except Exception as e:
        return {"status": "fail", "message": str(e)}
    finally:
        cursor.close()
        conn.close()   
        
def get_asset_by_id(asset_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """SELECT asset_id, asset_tag, asset_type, serial_number, manufacturer, model,
                          purchase_date, warranty_years, condition_status, assigned_to,
                          location, asset_status, last_updated
                   FROM asset_inventory WHERE asset_id=%s"""
        cursor.execute(query, (asset_id,))
        row = cursor.fetchone()

        if row:
            return AssetInventory(
                asset_id=row[0],
                asset_tag=row[1],
                asset_type=row[2],
                serial_number=row[3],
                manufacturer=row[4],
                model=row[5],
                purchase_date=row[6],
                warranty_years=row[7],
                condition_status=row[8],
                assigned_to=row[9],
                location=row[10],
                asset_status=row[11],
                last_updated=row[12],
            )
        return "Not found"

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
     
