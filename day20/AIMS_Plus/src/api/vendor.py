from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
import pymysql

# -----------------------------
# Initialize FastAPI router
# -----------------------------
# Prefix "/vendors" means all endpoints will start with /vendors
# Tag "Vendors" groups these endpoints in API docs (Swagger UI)
vendor_router = APIRouter(prefix="/vendors", tags=["Vendors"])

# -----------------------------
# Database connection function
# -----------------------------
def get_connection():
    """
    Establish and return a connection to the MySQL database.
    Using DictCursor so results are returned as dictionaries (column names as keys).
    """
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db",
        cursorclass=pymysql.cursors.DictCursor
    )

# -----------------------------
# Pydantic model for Vendor
# -----------------------------
class Vendor(BaseModel):
    """
    Defines the structure of a Vendor object.
    Used for validation and serialization of request/response bodies.
    """
    vendor_name: str
    contact_person: str
    contact_phone: str
    gst_number: str
    email: str
    address: str
    city: str
    active_status: str


# ------------------- POST -------------------

@vendor_router.post("/create")
def create_vendor(vendor: Vendor):
    """
    Create a new vendor record in the database.
    Accepts vendor details in request body and inserts into vendor_master table.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """INSERT INTO vendor_master 
                   (vendor_name, contact_person, contact_phone, gst_number, email, 
                    address, city, active_status) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (vendor.vendor_name, vendor.contact_person, vendor.contact_phone, vendor.gst_number,
                               vendor.email, vendor.address, vendor.city, vendor.active_status))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Vendor created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ------------------- GET -------------------

@vendor_router.get("/list")
def get_all_vendors():
    """
    Fetch all vendors from the database.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM vendor_master")
        vendors = cursor.fetchall()
        cursor.close()
        connection.close()
        return vendors
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@vendor_router.get("/list/status")
def get_vendors_by_status(status: str):
    """
    Fetch vendors filtered by active_status (case-insensitive).
    Example: /vendors/list/status?status=active
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM vendor_master WHERE LOWER(active_status) = LOWER(%s)"
        cursor.execute(query, (status,))
        vendors = cursor.fetchall()
        cursor.close()
        connection.close()
        return vendors
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@vendor_router.get("/search")
def search_vendors(keyword: str):
    """
    Search vendors by keyword in vendor_name, contact_person, or city.
    Uses LIKE for partial matching.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """SELECT * FROM vendor_master 
                   WHERE vendor_name LIKE %s OR contact_person LIKE %s OR city LIKE %s"""
        like_pattern = f"%{keyword}%"
        cursor.execute(query, (like_pattern,) * 3)  # Apply keyword to all 3 fields
        vendors = cursor.fetchall()
        cursor.close()
        connection.close()
        if not vendors:
            raise HTTPException(status_code=404, detail="No vendors found")
        return vendors
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@vendor_router.get("/{id}")
def get_vendor_by_id(id: int):
    """
    Fetch a single vendor by its vendor_id.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM vendor_master WHERE vendor_id = %s"
        cursor.execute(query, (id,))
        vendor = cursor.fetchone()
        cursor.close()
        connection.close()
        if vendor is None:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return vendor
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@vendor_router.get("/count")
def count_vendors():
    """
    Count the total number of vendors in the database.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT COUNT(*) AS total FROM vendor_master"
        cursor.execute(query)
        count = cursor.fetchone()["total"]
        cursor.close()
        connection.close()
        return {"total_vendors": count}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# ------------------- PUT -------------------

@vendor_router.put("/{id}")
def update_vendor(id: int, vendor: Vendor):
    """
    Update all fields of a vendor by its vendor_id.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) AS count FROM vendor_master WHERE vendor_id = %s", (id,))
        count = cursor.fetchone()["count"]

        if count == 0:
            cursor.close()
            connection.close()
            raise HTTPException(status_code=404, detail="Vendor not found")

        query = """UPDATE vendor_master 
                   SET vendor_name = %s, contact_person = %s, contact_phone = %s, 
                       gst_number = %s, email = %s, address = %s, city = %s, active_status = %s 
                   WHERE vendor_id = %s"""
        cursor.execute(query, (vendor.vendor_name, vendor.contact_person, vendor.contact_phone, vendor.gst_number,
                               vendor.email, vendor.address, vendor.city, vendor.active_status, id))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Vendor updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ------------------- PATCH -------------------

@vendor_router.patch("/{id}/status")
def update_vendor_status(id: int, active_status: str):
    """
    Update only the active_status field of a vendor.
    Example: /vendors/{id}/status?active_status=inactive
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE vendor_master SET active_status = %s WHERE vendor_id = %s"
        cursor.execute(query, (active_status, id))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Vendor status updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ------------------- DELETE -------------------

@vendor_router.delete("/{id}")
def delete_vendor(id: int):
    """
    Delete a vendor from the database by its vendor_id.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM vendor_master WHERE vendor_id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Vendor deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
