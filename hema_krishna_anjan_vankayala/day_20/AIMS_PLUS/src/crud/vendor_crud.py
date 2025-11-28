from src.config import db_connection
from src.models import vendor_model
from typing import Optional

# Create a new vendor record
def create_vendor(new_vendor: vendor_model.VendorMaster):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO ust_asset_db.vendor_master
            (vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                new_vendor.vendor_name,
                new_vendor.contact_person,
                new_vendor.contact_phone,
                new_vendor.gst_number,
                new_vendor.email,
                new_vendor.address,
                new_vendor.city,
                new_vendor.active_status
            )
        )
        conn.commit()
    except Exception as e:
        raise ValueError("Error: ", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Get all vendors (optionally filter by active_status)
def get_all_vendors(status: Optional[str] = ""):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if status == "":
            cursor.execute("SELECT * FROM ust_asset_db.vendor_master")
            data = cursor.fetchall()
            return data
        else:
            cursor.execute(
                "SELECT * FROM ust_asset_db.vendor_master WHERE active_status = %s",
                (status,)
            )
            data = cursor.fetchall()
            return data
    except Exception as e:
        raise Exception(f"Error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Search vendors by field and keyword
def search_vendors(field_type: str, keyword: str):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM ust_asset_db.vendor_master WHERE {field_type} LIKE %s",
            (f'%{keyword}%',)
        )
        data = cursor.fetchall()
        return data
    except Exception as e:
        raise Exception(f"Error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Get vendor by ID
def get_vendor_by_id(log_id):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM ust_asset_db.vendor_master WHERE vendor_id=%s",
            (log_id,)
        )
        data = cursor.fetchone()
        return data
    except Exception as e:
        raise Exception(f"Error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Update vendor by ID
def update_vendor_by_id(vendor_id: int, new_asset: vendor_model.VendorMaster):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_vendor_by_id(vendor_id):
            cursor.execute(
                """
                UPDATE ust_asset_db.vendor_master
                SET vendor_name=%s, contact_person=%s, contact_phone=%s, gst_number=%s,
                    email=%s, address=%s, city=%s, active_status=%s
                WHERE vendor_id=%s
                """,
                (
                    new_asset.vendor_name,
                    new_asset.contact_person,
                    new_asset.contact_phone,
                    new_asset.gst_number,
                    new_asset.email,
                    new_asset.address,
                    new_asset.city,
                    new_asset.active_status,
                    vendor_id
                )
            )
            conn.commit()
            return True
        else:
            raise ValueError
    except Exception as e:
        raise ValueError("Error:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Delete vendor by ID
def delete_vendor_by_id(vendor_id: int):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_vendor_by_id(vendor_id):
            cursor.execute(
                "DELETE FROM ust_asset_db.vendor_master WHERE vendor_id=%s",
                (vendor_id,)
            )
            conn.commit()
            return True
        else:
            raise ValueError
    except Exception as e:
        raise ValueError("ERROR:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
