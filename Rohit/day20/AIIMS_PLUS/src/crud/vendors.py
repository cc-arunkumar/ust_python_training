import pymysql  # Import pymysql to connect and interact with MySQL databases
from src.config.db_connection import get_connection  # Import custom function to establish DB connection
import datetime  # Import datetime (not used here, but useful for date handling if needed)
from fastapi import HTTPException  # Import HTTPException for API error handling in FastAPI


# -----------------------------
# GET ALL VENDORS
# -----------------------------
def get_all_data():
    """
    Fetch all vendor records from vendor_master table.
    """
    try:
        conn = get_connection()  # Establish DB connection
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # DictCursor returns rows as dictionaries
        sql = "SELECT * FROM ust_asset_inventory.vendor_master"  # SQL query to fetch all vendors
        cursor.execute(sql)  # Execute query
        ans = cursor.fetchall()   # Fetch all rows
        return ans
    except Exception as e:
        print("Error fetching tasks:", e)  # Print error for debugging
        return []  # Return empty list if error occurs
    finally:
        if cursor: cursor.close()  # Close cursor safely
        if conn: conn.close()      # Close connection safely


# -----------------------------
# GET VENDORS BY STATUS
# -----------------------------
def get_data_by_status(active_status: str):
    """
    Fetch vendor records filtered by active_status (Active/Inactive).
    """
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM ust_asset_inventory.vendor_master WHERE active_status=%s"
        cursor.execute(sql, (active_status,))
        ans = cursor.fetchall()
        return ans
    except Exception as e:
        print("Error fetching vendors:", e)
        return []
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# GET VENDOR BY ID
# -----------------------------
def get_data_by_id(id:int):
    """
    Fetch a single vendor record by vendor_id.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "select * from ust_asset_inventory.vendor_master where vendor_id=%s"
        cursor.execute(sql, (id,))
        ans = cursor.fetchone()  # Fetch single row
        return ans 
    except Exception as e:
        print("Error fetching vendors:", e)
        return []
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# CREATE NEW VENDOR
# -----------------------------
def create_vendor(vendor):
    """
    Insert a new vendor record into vendor_master table.
    Accepts a Pydantic model or object 'vendor' containing vendor details.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # SQL query for inserting new vendor record
        sql = """
        INSERT INTO vendor_master (
            vendor_id, vendor_name, contact_person, contact_phone,
            gst_number, email, address, city, active_status
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Values tuple extracted from vendor object
        values = (
            str(vendor.vendor_id),       # Vendor ID (string conversion for safety)
            vendor.vendor_name,          # Vendor name
            vendor.contact_person,       # Contact person name
            vendor.contact_phone,        # Contact phone number
            vendor.gst_number,           # GST number
            vendor.email,                # Email address
            vendor.address,              # Vendor address
            vendor.city.value,           # City (enum value converted to string)
            vendor.activity_status.value # Active status (enum value converted to string)
        )

        cursor.execute(sql, values)  # Execute insert query
        conn.commit()  # Commit transaction

        return {"message": "Vendor created successfully", "vendor_id": str(vendor.vendor_id)}

    except Exception as e:
        if conn: conn.rollback()  # Rollback if error occurs
        raise HTTPException(status_code=500, detail=f"Error creating vendor: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        

# -----------------------------
# UPDATE FULL VENDOR RECORD
# -----------------------------
def update_vendor(id: str, vendor):
    """
    Update all fields of a vendor record by vendor_id.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # SQL query to update vendor record
        sql = """
        UPDATE vendor_master
        SET vendor_name=%s, contact_person=%s, contact_phone=%s,
            gst_number=%s, email=%s, address=%s, city=%s, active_status=%s
        WHERE vendor_id=%s
        """

        # Values tuple for update query
        values = (
            vendor.vendor_name,
            vendor.contact_person,
            vendor.contact_phone,
            vendor.gst_number,
            vendor.email,
            vendor.address,
            vendor.city.value,
            vendor.activity_status.value,
            id,
        )

        cursor.execute(sql, values)  # Execute update query
        conn.commit()  # Commit changes

        if cursor.rowcount == 0:  # If no rows updated
            raise HTTPException(status_code=404, detail=f"Vendor with id {id} not found")

        return {"message": "Vendor updated successfully", "vendor_id": id}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating vendor: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# UPDATE VENDOR STATUS ONLY
# -----------------------------
def update_vendor_status(id: str, status: str):
    """
    Update only the active_status field of a vendor record.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Update query for status
        sql = "UPDATE vendor_master SET active_status=%s WHERE vendor_id=%s"
        cursor.execute(sql, (status, id))
        conn.commit()

        if cursor.rowcount == 0:  # If no rows updated
            raise HTTPException(status_code=404, detail=f"Vendor with id {id} not found")

        return {"message": "Vendor status updated successfully", "vendor_id": id, "active_status": status}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating vendor status: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# DELETE VENDOR
# -----------------------------
def delete_vendor(id: str):
    """
    Delete a vendor record by vendor_id.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Delete query
        sql = "DELETE FROM vendor_master WHERE vendor_id=%s"
        cursor.execute(sql, (id,))
        conn.commit()

        if cursor.rowcount == 0:  # If no rows deleted
            raise HTTPException(status_code=404, detail=f"Vendor with id {id} not found")

        return {"message": "Vendor deleted successfully", "vendor_id": id}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting vendor: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# SEARCH VENDORS BY COLUMN
# -----------------------------
def get_rows_by_column(column_name: str, keyword: str):
    """
    Search vendors by keyword in a specific column.
    Only allowed columns can be searched to prevent SQL injection.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        # Allowed columns for search
        allowed_columns = ["vendor_id", "vendor_name", "contact_person", "contact_phone",
                           "gst_number", "email", "address", "city", "active_status"]

        if column_name not in allowed_columns:  # Validate column name
            return {"error": f"Invalid column name: {column_name}"}

        # Build query dynamically with safe column name
        sql = f"SELECT * FROM vendor_master WHERE {column_name} = %s"
        cursor.execute(sql, (keyword,))
        rows = cursor.fetchall()

        # Return rows if found, else message
        return rows if rows else {"message": f"No rows found where {column_name} = {keyword}"}

    except Exception as e:
        print("Error fetching rows:", e)
        return {"error": str(e)}
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# COUNT VENDORS
# -----------------------------
def count_vendors():
    """
    Count total number of vendors in vendor_master table.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM vendor_master"  # Count query
        cursor.execute(sql)
        total = cursor.fetchone()[0]  # Fetch count value
        return total
    except Exception as e:
        print("Error counting vendors:", e)
        return 0
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
