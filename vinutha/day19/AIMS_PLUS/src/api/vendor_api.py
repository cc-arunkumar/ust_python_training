from fastapi import FastAPI, HTTPException, APIRouter
from typing import List
from pydantic import BaseModel
import pymysql
from io import StringIO

# Initialize FastAPI vendor_router
vendor_router = APIRouter(prefix="/vendors")

# Database connection function
def get_connection():
    return pymysql.connect(
        host="localhost",  # MySQL host
        user="root",  # MySQL user
        password="pass@word1",  # MySQL password
        database="ust_asset_db"  # Your database name
    )

# Pydantic model for Vendor
class Vendor(BaseModel):
    vendor_name: str
    contact_person: str
    contact_phone: str
    gst_number: str
    email: str
    address: str
    city: str
    active_status: str

# POST endpoint to create a new vendor
@vendor_router.post("/create")
def create_vendor(vendor: Vendor):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """INSERT INTO vendor_master (vendor_name, contact_person, contact_phone, gst_number, email, 
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

# GET endpoint to fetch all vendors
@vendor_router.get("/vendors/list")
def get_all_vendors():
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

# GET endpoint to filter vendors by status
@vendor_router.get("/list")
def get_vendors_by_status(status: str):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM vendor_master WHERE active_status = %s"
        cursor.execute(query, (status,))
        vendors = cursor.fetchall()
        cursor.close()
        connection.close()
        return vendors
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# GET endpoint to search vendors by keyword (in vendor_name, contact_person, city, etc.)
# @vendor_router.get("/search")
# def search_vendors(keyword: str):
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         query = """SELECT * FROM vendor_master WHERE vendor_name LIKE %s OR contact_person LIKE %s OR city LIKE %s"""
#         search_pattern = f"%{keyword}%"
#         cursor.execute(query, (search_pattern, search_pattern, search_pattern))
#         vendors = cursor.fetchall()
#         cursor.close()
#         connection.close()
#         return vendors
#     except Exception as e:
#         raise HTTPException(status_code=404, detail=str(e))
@vendor_router.get("/search")
def search_vendors(column: str, value: str):
    # List of valid columns to prevent SQL injection
    valid_columns = ["vendor_id","vendor_name","contact_person","contact_phone",
                     "gst_number","email","address","city","active_status"]
    
    # Check if the provided column is valid
    if column not in valid_columns:
        raise HTTPException(status_code=400, detail="Invalid column name")
    
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        # Construct the search query
        query = f"SELECT * FROM vendor_master WHERE {column} LIKE %s"
        search_pattern = f"%{value}%"
        
        # Execute the query
        cursor.execute(query, (search_pattern,))
        vendors = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        if not vendors:
            raise HTTPException(status_code=404, detail="No vendors found")
        
        return vendors
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# GET endpoint to get vendor by vendor_id
@vendor_router.get("/{id}")
def get_vendor_by_id(id: int):
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

# GET endpoint to count total vendors
@vendor_router.get("/vendors/count")
def count_vendors():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM vendor_master"
        cursor.execute(query)
        count = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return {"total_vendors": count}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# PUT endpoint to update vendor by vendor_id
@vendor_router.put("/{id}")
def update_vendor(id: int, vendor: Vendor):
    try:
        # First, check if the vendor exists
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM vendor_master WHERE vendor_id = %s", (id,))
        count = cursor.fetchone()[0]
        
        if count == 0:
            cursor.close()
            connection.close()
            raise HTTPException(status_code=404, detail="Vendor not found")
        
        # If the vendor exists, perform the update
        query = """UPDATE vendor_master SET vendor_name = %s, contact_person = %s, contact_phone = %s, 
                   gst_number = %s, email = %s, address = %s, city = %s, active_status = %s 
                   WHERE vendor_id = %s"""
        
        cursor.execute(query, (vendor.vendor_name, vendor.contact_person, vendor.contact_phone, vendor.gst_number,
                               vendor.email, vendor.address, vendor.city, vendor.active_status, id))
        connection.commit()  # Commit the transaction
        cursor.close()
        connection.close()
        
        return {"message": "Vendor updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# PATCH endpoint to update vendor status by vendor_id
@vendor_router.patch("/{id}/status")
def update_vendor_status(id: int, active_status: str):
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

# DELETE endpoint to delete vendor by vendor_id
@vendor_router.delete("/{id}")
def delete_vendor(id: int):
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
