from src.config.db_connection import get_connection
from typing import Optional
from src.helpers.validators import (
    validate_asset_tag,
    validate_asset_type,
    validate_serial_number,
    validate_warranty_years,
    validate_asset_status
)

# -----------------------------
# Function: create_asset
# Purpose: Insert a new asset record into the asset_inventory table
# -----------------------------
def create_asset(asset_tag, asset_type, serial_number,
                 manufacturer, model, purchase_date,
                 warranty_years, asset_status, assigned_to):
    conn = None
    cursor = None
    try:
        # Validate input fields before inserting
        validate_asset_tag(asset_tag)
        validate_asset_type(asset_type)
        validate_serial_number(serial_number)
        validate_warranty_years(warranty_years)
        validate_asset_status(asset_status, assigned_to)

        # Establish DB connection
        conn = get_connection()
        cursor = conn.cursor()

        # Insert new asset record
        cursor.execute(
            """INSERT INTO asset_inventory
               (asset_tag, asset_type, serial_number, manufacturer, model,
                purchase_date, warranty_years, assigned_to, asset_status, last_updated)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())""",
            (asset_tag, asset_type, serial_number, manufacturer, model,
             purchase_date, warranty_years, assigned_to, asset_status)
        )

        conn.commit()
        print("Asset created successfully.")

    except Exception as e:
        print("Error creating asset:", e)
    finally:
        # Always close cursor and connection
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# Function: read_all_assets
# Purpose: Retrieve all assets or filter by status
# -----------------------------
def read_all_assets(status_filter: str):
    conn = None
    cursor = None
    try:
        # Allowed status filters
        allowed = {"ALL", "Available", "Assigned", "Repair", "Retired"}
        if status_filter not in allowed:
            raise ValueError(f"status_filter must be one of {allowed}")

        conn = get_connection()
        cursor = conn.cursor()

        # Query based on filter
        if status_filter == "ALL":
            cursor.execute("SELECT * FROM asset_inventory ORDER BY asset_id ASC")
        else:
            cursor.execute(
                "SELECT * FROM asset_inventory WHERE asset_status = %s ORDER BY asset_id ASC",
                (status_filter,)
            )

        rows = cursor.fetchall()
        if not rows:
            print("No assets found")
            return

        # Print each asset record
        for el in rows:
            print(f"ASSET ID:{el[0]} | ASSET TAG:{el[1]} | ASSET TYPE:{el[2]} | SERIAL NUMBER:{el[3]} | "
                  f"MANUFACTURER:{el[4]} | MODEL:{el[5]} | PURCHASE DATE:{el[6]} | WARRANTY YEARS:{el[7]} | "
                  f"ASSIGNED TO:{el[8]} | ASSET STATUS:{el[9]} | LAST UPDATED:{el[10]}")

    except Exception as e:
        print("Error reading assets:", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# Function: read_asset_by_id
# Purpose: Retrieve a single asset by its ID
# -----------------------------
def read_asset_by_id(asset_id: int):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Query asset by ID
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        row = cursor.fetchone()

        if not row:
            print("Asset not found.")
            return
        
        # Print asset details
        print(f"ASSET ID:{row[0]} | ASSET TAG:{row[1]} | ASSET TYPE:{row[2]} | SERIAL NUMBER:{row[3]} | "
              f"MANUFACTURER:{row[4]} | MODEL:{row[5]} | PURCHASE DATE:{row[6]} | WARRANTY YEARS:{row[7]} | "
              f"ASSIGNED TO:{row[8]} | ASSET STATUS:{row[9]} | LAST UPDATED:{row[10]}")

    except Exception as e:
        print("Error reading asset:", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# Function: update_asset
# Purpose: Update an existing asset record
# -----------------------------
def update_asset(asset_id: int, asset_type: Optional[str] = None,
                 manufacturer: Optional[str] = None,
                 model: Optional[str] = None,
                 warranty_years: Optional[int] = None,
                 asset_status: Optional[str] = None,
                 assigned_to: Optional[str] = None):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Fetch current asset details
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        current = cursor.fetchone()
        
        if not current:
            print("Asset not found.")
            return

        # Use new values if provided, otherwise keep existing
        new_asset_type = asset_type if asset_type else current[2]
        new_manufacturer = manufacturer if manufacturer else current[4]
        new_model = model if model else current[5]
        new_warranty = warranty_years if warranty_years else current[7]
        new_status = asset_status if asset_status else current[9]
        new_assigned_to = assigned_to if assigned_to is not None else current[8]

        # Validate updated values
        validate_asset_type(new_asset_type)
        validate_warranty_years(new_warranty)
        validate_asset_status(new_status, new_assigned_to)

        # Update record
        cursor.execute(
            """UPDATE asset_inventory
               SET asset_type=%s, manufacturer=%s, model=%s, warranty_years=%s,
                   asset_status=%s, assigned_to=%s, last_updated=NOW()
               WHERE asset_id=%s""",
            (new_asset_type, new_manufacturer, new_model,
             new_warranty, new_status, new_assigned_to, asset_id)
        )

        conn.commit()
        print(f"Asset {asset_id} updated successfully.")

    except Exception as e:
        print("Error updating asset:", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# Function: delete_asset
# Purpose: Delete an asset record by ID
# -----------------------------
def delete_asset(asset_id: int):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Delete record
        cursor.execute("DELETE FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        conn.commit()

        # Check if deletion happened
        if cursor.rowcount == 0:
            print("Asset not found.")
        else:
            print(f"Asset {asset_id} deleted successfully.")

    except Exception as e:
        print("Error deleting asset:", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
