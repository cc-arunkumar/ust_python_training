import pymysql
from typing import Optional
from ..models.maintenancelog import MaintenanceLog, StatusValidate
from ..config.db_connection import get_connection
from datetime import datetime
import csv


def get_keys():
    """
    Retrieve column names (keys) from the maintenance_log table in the database.

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
            AND TABLE_NAME = 'maintenance_log'
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


# CRUD operations for Maintenance Log
class MaintenanceCrud:
    def create_maintenance(self, data: MaintenanceLog):
        """
        Insert a new maintenance record into the maintenance_log table.

        Args:
            data (MaintenanceLog): Maintenance details provided as a Pydantic model.

        Returns:
            MaintenanceLog: The inserted maintenance data.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO ust_aims_plus.maintenance_log (
                    asset_tag, maintenance_type, vendor_name, description,
                    cost, maintenance_date, technician_name, status
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

    def get_all_maintenance(self, status):
        """
        Retrieve all maintenance logs or filter by status.

        Args:
            status (str): 'ALL' to fetch all logs, or a specific status value.

        Returns:
            list[dict] | None: List of maintenance logs as dictionaries, or None if no records found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            keys = get_keys()

            if status == "ALL":
                query = "SELECT * FROM ust_aims_plus.maintenance_log"
                cursor.execute(query)
            else:
                query = "SELECT * FROM ust_aims_plus.maintenance_log WHERE status = %s"
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

    def get_maintenance_by_id(self, log_id):
        """
        Retrieve a single maintenance log by its ID.

        Args:
            log_id (int): Unique identifier of the maintenance log.

        Returns:
            list[dict] | bool: Maintenance details as a dictionary inside a list, or False if not found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            keys = get_keys()

            query = "SELECT * FROM ust_aims_plus.maintenance_log WHERE log_id = %s"
            cursor.execute(query, (log_id,))
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

    def update_maintenance(self, id, data: MaintenanceLog):
        """
        Update an existing maintenance log by ID.

        Args:
            id (int): Maintenance log ID to update.
            data (MaintenanceLog): Updated maintenance details.

        Returns:
            MaintenanceLog: Updated maintenance data.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE ust_aims_plus.maintenance_log
                SET asset_tag=%s, maintenance_type=%s, vendor_name=%s, description=%s,
                    cost=%s, maintenance_date=%s, technician_name=%s, status=%s
                WHERE log_id=%s
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

    def update_maintenance_status(self, id, status):
        """
        Update only the status of a maintenance log.

        Args:
            id (int): Maintenance log ID.
            status (str): New status value.

        Returns:
            list[dict]: Updated maintenance log details.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "UPDATE ust_aims_plus.maintenance_log SET status=%s WHERE log_id=%s"
            cursor.execute(query, (status, id))
            conn.commit()
            print("Status updated!")
            return self.get_maintenance_by_id(id)
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def delete_maintenance(self, id):
        """
        Delete a maintenance log by ID.

        Args:
            id (int): Maintenance log ID.

        Returns:
            list[dict] | bool: Deleted maintenance log details, or False if not found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            condition = self.get_maintenance_by_id(id)

            if condition:
                query = "DELETE FROM ust_aims_plus.maintenance_log WHERE log_id=%s"
                cursor.execute(query, (id,))
                conn.commit()
                print("Maintenance deleted from id =", id)

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

    def get_maintenance_by_keyword(self, keyword, value):
        """
        Search maintenance logs dynamically by a given column (keyword) and value.

        Args:
            keyword (str): Column name to filter by.
            value (str): Value to match.

        Returns:
            list[dict] | bool: Matching maintenance logs, or False if none found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            keys = get_keys()

            query = f"SELECT * FROM ust_aims_plus.maintenance_log WHERE {keyword}=%s"
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

    def get_all_maintenance_count(self):
        """
        Count total number of maintenance logs in the table.

        Returns:
            int | None: Number of maintenance logs, or None if no records exist.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM ust_aims_plus.maintenance_log"
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
