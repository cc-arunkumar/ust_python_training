"""
CRUD Operations Module for Asset Inventory Table
------------------------------------------------
This module provides reusable database functions for managing records in the 
`asset_inventory` table. All operations are parameterized to avoid SQL injection 
and ensure proper database transaction handling.

Functions Included:
- create_asset()
- get_all()
- get_by_id()
- update()
- delete()
- set_status()
- find()
- count_records()

Author: (Your Name)
"""

from src.model.model_asset_inventory import AssetInventory
from src.config.db_connection import get_connection
import datetime


def create_asset(asset: AssetInventory):
    """Insert a new asset record into the database."""
    
    conn = get_connection()
    cursor = conn.cursor()
    last_updated = datetime.datetime.now()

    query = """
    INSERT INTO asset_inventory(
        ASSET_TAG, ASSET_TYPE, SERIAL_NUMBER, MANUFACTURER, MODEL, PURCHASE_DATE,
        WARRANTY_YEARS, CONDITION_STATUS, ASSIGNED_TO, LOCATION, ASSET_STATUS, LAST_UPDATED
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    data = (
        asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
        asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
        asset.assigned_to, asset.location, asset.asset_status, last_updated
    )

    cursor.execute(query, data)
    conn.commit()
    conn.close()



def get_all(status=None):
    """
    Retrieve all asset records.
    Optional filter: status (e.g., Active, Retired)
    """
    
    conn = get_connection()
    cursor = conn.cursor()

    if status:
        cursor.execute("SELECT * FROM asset_inventory WHERE ASSET_STATUS=%s", (status,))
    else:
        cursor.execute("SELECT * FROM asset_inventory")

    rows = cursor.fetchall()
    conn.close()
    return rows



def get_by_id(asset_id: int):
    """Fetch a single asset record using its primary key (ASSET_ID)."""

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM asset_inventory WHERE ASSET_ID=%s", (asset_id,))
    
    row = cursor.fetchone()
    conn.close()
    return row



def update(asset_id: int, asset: AssetInventory):
    """Update an existing asset record based on asset ID."""
    
    conn = get_connection()
    cursor = conn.cursor()
    last_updated = datetime.datetime.now()

    query = """
    UPDATE asset_inventory SET 
        ASSET_TAG=%s, ASSET_TYPE=%s, SERIAL_NUMBER=%s, MANUFACTURER=%s, MODEL=%s,
        PURCHASE_DATE=%s, WARRANTY_YEARS=%s, CONDITION_STATUS=%s, ASSIGNED_TO=%s,
        LOCATION=%s, ASSET_STATUS=%s, LAST_UPDATED=%s
    WHERE ASSET_ID=%s
    """

    data = (
        asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
        asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
        asset.assigned_to, asset.location, asset.asset_status, last_updated, asset_id
    )

    cursor.execute(query, data)
    conn.commit()
    conn.close()



def delete(asset_id: int):
    """Delete an asset from the table using its ID."""

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM asset_inventory WHERE ASSET_ID=%s", (asset_id,))
    
    conn.commit()
    conn.close()



def set_status(asset_id: int, status: str):
    """
    Update only the status of an asset (e.g., Active → Retired).
    Automatically updates the `last_updated` timestamp.
    """

    conn = get_connection()
    cursor = conn.cursor()
    last_updated = datetime.datetime.now()

    cursor.execute(
        "UPDATE asset_inventory SET ASSET_STATUS=%s, LAST_UPDATED=%s WHERE ASSET_ID=%s",
        (status, last_updated, asset_id)
    )

    conn.commit()
    conn.close()



def find(column, value):
    """
    Search for asset based on any allowed column.
    Uses wildcard LIKE search for partial matches.
    """

    allowed_columns = [
        "ASSET_TAG", "ASSET_TYPE", "SERIAL_NUMBER", "MANUFACTURER", "MODEL",
        "PURCHASE_DATE", "WARRANTY_YEARS", "CONDITION_STATUS", "ASSIGNED_TO",
        "LOCATION", "ASSET_STATUS"
    ]

    if column not in allowed_columns:
        raise ValueError("Invalid column name!")

    conn = get_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM asset_inventory WHERE {column} LIKE %s"
    cursor.execute(query, (f"%{value}%",))

    rows = cursor.fetchall()
    conn.close()
    return rows



def count_records():
    """Return the total number of asset records stored in the table."""

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM asset_inventory")
    
    total = cursor.fetchone()
    conn.close()
    return total
