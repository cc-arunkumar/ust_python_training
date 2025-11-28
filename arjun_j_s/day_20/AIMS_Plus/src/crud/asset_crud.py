import csv
from ..models.asset_model import AssetInventory, StatusValidate
from src.config.db_connection import get_connection
from datetime import datetime
from typing import Optional

path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/final/asset_inventory.csv"

class Asset:

    def get_headers(self):  # Get column names of asset_inventory table
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = 'ust_aims_plus'
                  AND table_name = 'asset_inventory'
                ORDER BY ordinal_position;
            """)
            head = cursor.fetchall()
            return [col[0] for col in head]
        except Exception as e:
            raise e
        finally:
            if conn and conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def create_asset(self, asset: AssetInventory):  # Insert new asset record
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO ust_aims_plus.asset_inventory 
                (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, 
                 warranty_years, condition_status, assigned_to, location, asset_status, last_updated)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = tuple(asset.__dict__.values()) + (datetime.now(),)
            cursor.execute(query, values)
            conn.commit()
            print("Data added successfully")
            return True
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_all_asset(self, status="all"):  # Get all assets (optionally filter by status)
        try:
            conn = get_connection()
            cursor = conn.cursor()
            header = self.get_headers()
            if status != "all":
                cursor.execute("SELECT * FROM ust_aims_plus.asset_inventory WHERE asset_status=%s", (status,))
            else:
                cursor.execute("SELECT * FROM ust_aims_plus.asset_inventory")
            rows = cursor.fetchall()
            if rows:
                return [dict(zip(header, data)) for data in rows]
            return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed")

    def get_asset_by_id(self, asset_id: int):  # Get asset by ID
        try:
            conn = get_connection()
            cursor = conn.cursor()
            header = self.get_headers()
            cursor.execute("SELECT * FROM ust_aims_plus.asset_inventory WHERE asset_id=%s", (asset_id,))
            row = cursor.fetchone()
            if row:
                return dict(zip(header, row))
            return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_asset_count(self):  # Get total asset count
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ust_aims_plus.asset_inventory")
            row = cursor.fetchall()
            return len(row) if row else None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_asset_keyword(self, keyword, value):  # Search assets by keyword/value
        try:
            conn = get_connection()
            cursor = conn.cursor()
            header = self.get_headers()
            cursor.execute(f"SELECT * FROM ust_aims_plus.asset_inventory WHERE {keyword}=%s", (value,))
            rows = cursor.fetchall()
            if rows:
                return [dict(zip(header, row)) for row in rows]
            return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def bulk_upload(self):  # Bulk upload assets from CSV file
        with open(path, "r") as asset_file:
            asset_data = csv.DictReader(asset_file)
            asset_data = list(asset_data)
        for data in asset_data:
            try:
                self.create_asset(data)
            except Exception as e:
                raise e
        return True

    def update_asset_status(self, asset_id, status):  # Update asset status by ID
        try:
            conn = get_connection()
            cursor = conn.cursor()
            StatusValidate(asset_status=status)
            cursor.execute("UPDATE ust_aims_plus.asset_inventory SET asset_status=%s WHERE asset_id=%s", (status, asset_id))
            conn.commit()
            print("Status Updated")
            return True
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def update_asset(self, asset_id: int, asset: AssetInventory):  # Update full asset record
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE ust_aims_plus.asset_inventory 
                SET asset_tag=%s, asset_type=%s, serial_number=%s,
                    manufacturer=%s, model=%s, purchase_date=%s,
                    warranty_years=%s, condition_status=%s, assigned_to=%s, 
                    location=%s, asset_status=%s, last_updated=%s
                WHERE asset_id=%s
            """
            values = tuple(asset.__dict__.values()) + (datetime.now(), asset_id)
            cursor.execute(query, values)
            conn.commit()
            print("Data updated successfully")
            return True
        except Exception as e:
            print(str(e))
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def delete_asset(self, asset_id: int):  # Delete asset by ID
        try:
            conn = get_connection()
            cursor = conn.cursor()
            if self.get_asset_by_id(asset_id):
                cursor.execute("DELETE FROM ust_aims_plus.asset_inventory WHERE asset_id=%s", (asset_id,))
                conn.commit()
                print("Deleted Successfully")
                return True
            return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")