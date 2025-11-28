import csv
from ..models.maintenance_model import MaintenanceLog, StatusValidator
from src.config.db_connection import get_connection

path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/final/maintenance_log.csv"

class Maintain:

    def get_headers(self):  # Get column names of maintenance_log table
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = 'ust_aims_plus'
                  AND table_name = 'maintenance_log'
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

    def create_maintenance(self, maintenance: MaintenanceLog):  # Insert new maintenance log
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO ust_aims_plus.maintenance_log 
                (asset_tag, maintenance_type, vendor_name, description, cost, maintenance_date, technician_name, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = tuple(maintenance.__dict__.values())
            cursor.execute(query, values)
            conn.commit()
            print("Data added successfully")
            return True
        except Exception as e:
            print(str(e))
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_all_log(self, status="all"):  # Get all maintenance logs (optionally filter by status)
        try:
            conn = get_connection()
            cursor = conn.cursor()
            header = self.get_headers()
            if status != "all":
                cursor.execute("SELECT * FROM ust_aims_plus.maintenance_log WHERE status=%s", (status,))
            else:
                cursor.execute("SELECT * FROM ust_aims_plus.maintenance_log")
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

    def get_log_by_id(self, log_id: int):  # Get maintenance log by ID
        try:
            conn = get_connection()
            cursor = conn.cursor()
            header = self.get_headers()
            cursor.execute("SELECT * FROM ust_aims_plus.maintenance_log WHERE log_id=%s", (log_id,))
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

    def get_log_count(self):  # Get total maintenance log count
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ust_aims_plus.maintenance_log")
            row = cursor.fetchall()
            return len(row) if row else None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_log_keyword(self, keyword, value):  # Search maintenance logs by keyword/value
        try:
            conn = get_connection()
            cursor = conn.cursor()
            header = self.get_headers()
            cursor.execute(f"SELECT * FROM ust_aims_plus.maintenance_log WHERE {keyword}=%s", (value,))
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

    def bulk_upload(self):  # Bulk upload maintenance logs from CSV file
        with open(path, "r") as log_file:
            log_data = csv.DictReader(log_file)
            log_data = list(log_data)
        for data in log_data:
            try:
                self.create_maintenance(data)
            except Exception as e:
                raise e
        return True

    def update_log_status(self, log_id, status):  # Update maintenance log status by ID
        try:
            conn = get_connection()
            cursor = conn.cursor()
            StatusValidator(status=status)
            cursor.execute("UPDATE ust_aims_plus.maintenance_log SET status=%s WHERE log_id=%s", (status, log_id))
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

    def update_log(self, log_id: int, maintain: MaintenanceLog):  # Update full maintenance log record
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE ust_aims_plus.maintenance_log 
                SET asset_tag=%s, maintenance_type=%s, vendor_name=%s, description=%s, cost=%s, 
                    maintenance_date=%s, technician_name=%s, status=%s
                WHERE log_id=%s
            """
            values = tuple(maintain.__dict__.values()) + (log_id,)
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

    def delete_log(self, log_id: int):  # Delete maintenance log by ID
        try:
            conn = get_connection()
            cursor = conn.cursor()
            if self.get_log_by_id(log_id):
                cursor.execute("DELETE FROM ust_aims_plus.maintenance_log WHERE log_id=%s", (log_id,))
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