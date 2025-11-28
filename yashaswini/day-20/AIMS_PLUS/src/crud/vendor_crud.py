import pymysql
from typing import Optional
from ..models.vendor_master import VendorMaster, StatusValidate
from ..config.db_connection import get_connection
from datetime import datetime
import csv


def get_keys():
    """
    Retrieve column names (keys) from the vendor_master table in the database.

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
            AND TABLE_NAME = 'vendor_master'
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


# CRUD operations for Vendor Master
class VendorCrud:
    def create_vendor(self, data: VendorMaster):
        """
        Insert a new vendor record into the vendor_master table.

        Args:
            data (VendorMaster): Vendor details provided as a Pydantic model.

        Returns:
            VendorMaster: The inserted vendor data.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO ust_aims_plus.vendor_master (
                    vendor_name, contact_person, contact_phone,
                    gst_number, email, address, city,
                    active_status
                )
                VALUES (%s, %s, %s, %s,
                        %s, %s, %s, %s)
            """
            values = tuple(data.__dict__.values())
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

    def get_all_vendor(self, status):
        """
        Retrieve all vendors or filter by status.

        Args:
            status (str): 'ALL' to fetch all vendors, or a specific status value.

        Returns:
            list[dict] | None: List of vendors as dictionaries, or None if no records found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            keys = get_keys()

            if status == "ALL":
                query = "SELECT * FROM ust_aims_plus.vendor_master"
                cursor.execute(query)
            else:
                query = "SELECT * FROM ust_aims_plus.vendor_master WHERE status = %s"
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

    def get_vendor_by_id(self, vendor_id):
        """
        Retrieve a single vendor by their ID.

        Args:
            vendor_id (int): Unique identifier of the vendor.

        Returns:
            list[dict] | bool: Vendor details as a dictionary inside a list, or False if not found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            keys = get_keys()

            query = "SELECT * FROM ust_aims_plus.vendor_master WHERE vendor_id = %s"
            cursor.execute(query, (vendor_id,))
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

    def update_vendor(self, id, data: VendorMaster):
        """
        Update an existing vendor record by ID.

        Args:
            id (int): Vendor ID to update.
            data (VendorMaster): Updated vendor details.

        Returns:
            VendorMaster: Updated vendor data.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE ust_aims_plus.vendor_master
                SET vendor_name=%s, contact_person=%s, contact_phone=%s, gst_number=%s,
                    email=%s, address=%s, city=%s, active_status=%s
                WHERE vendor_id=%s
            """
            values = tuple(data.__dict__.values()) + (id,)
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

    def update_vendor_status(self, id, status):
        """
        Update only the status of a vendor.

        Args:
            id (int): Vendor ID.
            status (str): New status value.

        Returns:
            list[dict]: Updated vendor details.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "UPDATE ust_aims_plus.vendor_master SET status=%s WHERE vendor_id=%s"
            cursor.execute(query, (status, id))
            conn.commit()
            print("Status updated!")
            return self.get_vendor_by_id(id)
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def delete_vendor(self, id):
        """
        Delete a vendor by ID.

        Args:
            id (int): Vendor ID.

        Returns:
            list[dict] | bool: Deleted vendor details, or False if not found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            condition = self.get_vendor_by_id(id)

            if condition:
                query = "DELETE FROM ust_aims_plus.vendor_master WHERE vendor_id=%s"
                cursor.execute(query, (id,))
                conn.commit()
                print("Vendor deleted from id =", id)

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

    def get_vendor_by_keyword(self, keyword, value):
        """
        Search vendors dynamically by a given column (keyword) and value.

        Args:
            keyword (str): Column name to filter by.
            value (str): Value to match.

        Returns:
            list[dict] | bool: Matching vendors, or False if none found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            keys = get_keys()

            query = f"SELECT * FROM ust_aims_plus.vendor_master WHERE {keyword}=%s"
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

    def get_all_vendor_count(self):
        """
        Count total number of vendors in the table.

        Returns:
            int | None: Number of vendors, or None if no records exist.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM ust_aims_plus.vendor_master"
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
