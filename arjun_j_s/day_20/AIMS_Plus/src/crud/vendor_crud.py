import csv
from ..models.vendor_model import VendorMaster, StatusValidator
from src.config.db_connection import get_connection

path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/final/vendor_master.csv"

class Vendor:

    def get_headers(self):  # Get column names of vendor_master table
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = 'ust_aims_plus'
                  AND table_name = 'vendor_master'
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

    def create_vendor(self, vendor: VendorMaster):  # Insert new vendor record
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO ust_aims_plus.vendor_master 
                (vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = tuple(vendor.__dict__.values())
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

    def get_all_vendor(self, status="all"):  # Get all vendors (optionally filter by status)
        try:
            conn = get_connection()
            cursor = conn.cursor()
            header = self.get_headers()
            if status != "all":
                cursor.execute("SELECT * FROM ust_aims_plus.vendor_master WHERE active_status=%s", (status,))
            else:
                cursor.execute("SELECT * FROM ust_aims_plus.vendor_master")
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

    def get_vendor_by_id(self, vendor_id: int):  # Get vendor by ID
        try:
            conn = get_connection()
            cursor = conn.cursor()
            header = self.get_headers()
            cursor.execute("SELECT * FROM ust_aims_plus.vendor_master WHERE vendor_id=%s", (vendor_id,))
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

    def get_vendor_count(self):  # Get total vendor count
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ust_aims_plus.vendor_master")
            row = cursor.fetchall()
            return len(row) if row else None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_vendor_keyword(self, keyword, value):  # Search vendors by keyword/value
        try:
            conn = get_connection()
            cursor = conn.cursor()
            header = self.get_headers()
            cursor.execute(f"SELECT * FROM ust_aims_plus.vendor_master WHERE {keyword}=%s", (value,))
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

    def bulk_upload(self):  # Bulk upload vendors from CSV file
        with open(path, "r") as vendor_file:
            vendor_data = csv.DictReader(vendor_file)
            vendor_data = list(vendor_data)
        for data in vendor_data:
            try:
                self.create_vendor(data)
            except Exception as e:
                raise e
        return True

    def update_vendor_status(self, vendor_id, status):  # Update vendor status by ID
        try:
            conn = get_connection()
            cursor = conn.cursor()
            StatusValidator(active_status=status)
            cursor.execute("UPDATE ust_aims_plus.vendor_master SET active_status=%s WHERE vendor_id=%s", (status, vendor_id))
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

    def update_vendor(self, vendor_id: int, vendor: VendorMaster):  # Update full vendor record
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE ust_aims_plus.vendor_master 
                SET vendor_name=%s, contact_person=%s, contact_phone=%s, gst_number=%s, email=%s, address=%s, city=%s, active_status=%s
                WHERE vendor_id=%s
            """
            values = tuple(vendor.__dict__.values()) + (vendor_id,)
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

    def delete_vendor(self, vendor_id: int):  # Delete vendor by ID
        try:
            conn = get_connection()
            cursor = conn.cursor()
            if self.get_vendor_by_id(vendor_id):
                cursor.execute("DELETE FROM ust_aims_plus.vendor_master WHERE vendor_id=%s", (vendor_id,))
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