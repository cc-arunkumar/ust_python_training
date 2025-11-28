from src.config import db_connection
from src.models import vendor_model
from typing import Optional

# Function: Create a new vendor record in the database
def create_vendor(new_vendor: vendor_model.VendorMaster):
    # Insert a new vendor into the vendor_master table
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO ust_inventory_db.vendor_master (
                vendor_name, contact_person, contact_phone, gst_number,
                email, address, city, active_status
            ) VALUES (
                %s, %s, %s, %s,
                %s, %s, %s, %s
            )
        """
        # Prepare vendor data for insertion
        data = (
            new_vendor.vendor_name,
            new_vendor.contact_person,
            new_vendor.contact_phone,
            new_vendor.gst_number,
            new_vendor.email,
            new_vendor.address,
            new_vendor.city,
            new_vendor.active_status
        )
        cursor.execute(query, data)
        conn.commit()
        return True
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Retrieve all vendors, optionally filtered by active_status
def get_all_vendors(status: Optional[str] = ""):
    # If status is empty, fetch all vendors; otherwise filter by active_status
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if status == "":
            cursor.execute("SELECT * FROM ust_inventory_db.vendor_master")
            data = cursor.fetchall()
            return data
        else:
            cursor.execute("SELECT * FROM ust_inventory_db.vendor_master WHERE active_status=%s", (status,))
            data = cursor.fetchall()
            return data
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Retrieve a single vendor by ID
def get_vendor_by_id(vendor_id: int):
    # Query vendor_master table for a specific vendor_id
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_inventory_db.vendor_master WHERE vendor_id=%s", (vendor_id,))
        data = cursor.fetchone()
        if data:
            return data
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Update an existing vendor by ID
def update_vendor_by_id(vendor_id: int, new_vendor: vendor_model.VendorMaster):
    # Update vendor record if it exists
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_vendor_by_id(vendor_id):
            query = """
                UPDATE ust_inventory_db.vendor_master
                SET vendor_name = %s,
                    contact_person = %s,
                    contact_phone = %s,
                    gst_number = %s,
                    email = %s,
                    address = %s,
                    city = %s,
                    active_status = %s
                WHERE vendor_id = %s
            """
            # Prepare updated vendor data
            data = (
                new_vendor.vendor_name,
                new_vendor.contact_person,
                new_vendor.contact_phone,
                new_vendor.gst_number,
                new_vendor.email,
                new_vendor.address,
                new_vendor.city,
                new_vendor.active_status,
                vendor_id
            )
            cursor.execute(query, data)
            conn.commit()
            return True
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Delete a vendor by ID
def delete_vendor_by_id(vendor_id: int):
    # Remove vendor record if it exists
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_vendor_by_id(vendor_id):
            cursor.execute("DELETE FROM ust_inventory_db.vendor_master WHERE vendor_id=%s", (vendor_id,))
            conn.commit()
            return True
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Search vendors by a given field and value
def search_by_tag_vendor(field, value):
    # Perform a LIKE query on the specified field
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        query = f"SELECT * FROM ust_inventory_db.vendor_master WHERE {field} LIKE %s"
        cursor.execute(query, (f"%{value}%",))
        data = cursor.fetchall()
        return data
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()
