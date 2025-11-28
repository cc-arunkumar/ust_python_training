import pymysql
from typing import Optional
from ..models.assetsinventory import AssetInventory, StatusValidate
from ..config.db_connection import get_connection
from datetime import datetime
import csv

def get_keys():
    """
    Retrieve column names (keys) from the asset_inventory table in the database.

    Returns:
        list[str]: A list of column names ordered by their position in the table.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = 'ust_aims_plus'
            AND TABLE_NAME = 'asset_inventory'
            ORDER BY ORDINAL_POSITION;
        """)
        col = cursor.fetchall()
        keys = [i[0] for i in col]  # Extract column names
        return keys
    except Exception as e:
        raise
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection Closed!")


# CRUD operations for Asset Inventory
class AssetCrud:
    def create_asset(self, data: AssetInventory):
        """
        Insert a new asset record into the asset_inventory table.

        Args:
            data (AssetInventory): Asset details provided as a Pydantic model.

        Returns:
            AssetInventory: The inserted asset data.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO ust_aims_plus.asset_inventory (
                    asset_tag, asset_type, serial_number, manufacturer,
                    model, purchase_date, warranty_years, condition_status,
                    assigned_to, location, asset_status, last_updated
                )
                VALUES (%s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s)
            """
            # Append current timestamp to values
            values = tuple(data.__dict__.values()) + (datetime.now(),)
            cursor.execute(query, values)
            conn.commit()
            print("Data added successfully!")
            return data
        except Exception as e:
            print(e)
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def get_all_asset(self, status):
        """
        Retrieve all assets or filter by status.

        Args:
            status (str): 'ALL' to fetch all assets, or a specific status value.

        Returns:
            list[dict] | None: List of assets as dictionaries, or None if no records found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            keys = get_keys()

            if status == "ALL":
                query = "SELECT * FROM ust_aims_plus.asset_inventory"
                cursor.execute(query)
            else:
                query = "SELECT * FROM ust_aims_plus.asset_inventory WHERE asset_status = %s"
                cursor.execute(query, (status,))

            rows = cursor.fetchall()
            if rows:
                return [dict(zip(keys, values)) for values in rows]
            return None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def get_asset_by_id(self, asset_id):
        """
        Retrieve a single asset by its ID.

        Args:
            asset_id (int): Unique identifier of the asset.

        Returns:
            list[dict] | bool: Asset details as a dictionary inside a list, or False if not found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            keys = get_keys()

            query = "SELECT * FROM ust_aims_plus.asset_inventory WHERE asset_id = %s"
            cursor.execute(query, (asset_id,))
            row = cursor.fetchone()

            if row:
                return [dict(zip(keys, row))]
            return False
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def update_asset(self, id, data: AssetInventory):
        """
        Update an existing asset record by ID.

        Args:
            id (int): Asset ID to update.
            data (AssetInventory): Updated asset details.

        Returns:
            AssetInventory: Updated asset data.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE ust_aims_plus.asset_inventory
                SET asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s,
                    model=%s, purchase_date=%s, warranty_years=%s, condition_status=%s,
                    assigned_to=%s, location=%s, asset_status=%s, last_updated=%s
                WHERE asset_id=%s
            """
            values = tuple(data.__dict__.values()) + (datetime.now(), id)
            cursor.execute(query, values)
            conn.commit()
            print("Data updated successfully!")
            return data
        except Exception as e:
            print(str(e))
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def update_asset_status(self, id, status):
        """
        Update only the status of an asset.

        Args:
            id (int): Asset ID.
            status (str): New status value.

        Returns:
            list[dict]: Updated asset details.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "UPDATE ust_aims_plus.asset_inventory SET asset_status=%s WHERE asset_id=%s"
            cursor.execute(query, (status, id))
            conn.commit()
            print("Status updated!")
            return self.get_asset_by_id(id)
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def delete_asset(self, id):
        """
        Delete an asset by ID.

        Args:
            id (int): Asset ID.

        Returns:
            list[dict] | bool: Deleted asset details, or False if not found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            condition = self.get_asset_by_id(id)

            if condition:
                query = "DELETE FROM ust_aims_plus.asset_inventory WHERE asset_id=%s"
                cursor.execute(query, (id,))
                conn.commit()
                print("Asset deleted from id =", id)

                keys = get_keys()
                return [dict(zip(keys, condition))]
            return False
        except Exception as e:
            print(e)
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def get_asset_by_keyword(self, keyword, value):
        """
        Search assets dynamically by a given column (keyword) and value.

        Args:
            keyword (str): Column name to filter by.
            value (str): Value to match.

        Returns:
            list[dict] | bool: Matching assets, or False if none found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            keys = get_keys()

            query = f"SELECT * FROM ust_aims_plus.asset_inventory WHERE {keyword}=%s"
            cursor.execute(query, (value,))
            rows = cursor.fetchall()

            if rows:
                return [dict(zip(keys, values)) for values in rows]
            return False
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def get_all_asset_count(self):
        """
        Count total number of assets in the inventory.

        Returns:
            int | None: Number of assets, or None if no records exist.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM ust_aims_plus.asset_inventory"
            cursor.execute(query)
            rows = cursor.fetchall()
            return len(rows) if rows else None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")
