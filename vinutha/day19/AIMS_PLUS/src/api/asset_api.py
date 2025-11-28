from fastapi import FastAPI, HTTPException, APIRouter
from typing import List
from pydantic import BaseModel
import pymysql
import csv
from io import StringIO

# Initialize FastAPI asset_router
asset_router = APIRouter(prefix="/assets")

# Database connection function
def get_connection():
    return pymysql.connect(
        host="localhost",  # MySQL host
        user="root",  # MySQL user
        password="pass@word1",  # MySQL password
        database="ust_asset_db"  # Your database name
    )

# Pydantic model for Asset
class Asset(BaseModel):
    asset_tag: str
    asset_type: str
    serial_number: str
    manufacturer: str
    model: str
    purchase_date: str
    warranty_years: int
    condition_status: str
    assigned_to: str
    location: str
    asset_status: str

# GET endpoint to fetch all assets
@asset_router.get("/assets/list")
def get_all_assets():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM asset_inventory")
        assets = cursor.fetchall()
        cursor.close()
        connection.close()
        return assets
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# GET endpoint to filter assets by status
@asset_router.get("/list")
def get_assets_by_status(status: str):
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM asset_inventory WHERE asset_status = %s"
    cursor.execute(query, (status,))
    assets = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return assets

# GET endpoint to search assets by keyword in a specific column
@asset_router.get("/search")
def search_assets(column: str, keyword: str):
    # List of valid columns to prevent SQL injection
    valid_columns = [
        "asset_tag", "asset_type", "serial_number", "manufacturer", "model",
        "purchase_date", "warranty_years", "condition_status", "assigned_to",
        "location", "asset_status"
    ]
    
    # Check if the provided column is valid
    if column not in valid_columns:
        raise HTTPException(status_code=400, detail="Invalid column name")

    connection = get_connection()
    cursor = connection.cursor()

    # For numeric columns (like warranty_years), use exact matching (=)
    if column == "warranty_years":
        try:
            # Ensure keyword is a valid integer for warranty_years
            warranty_years = int(keyword)
            query = f"SELECT * FROM asset_inventory WHERE {column} = %s"
            cursor.execute(query, (warranty_years,))
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid value for warranty_years. It must be a number.")
    else:
        # For string-based columns, use LIKE for partial matching
        query = f"SELECT * FROM asset_inventory WHERE {column} LIKE %s"
        cursor.execute(query, (f"%{keyword}%",))  # Add "%" around the keyword for partial matching

    assets = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return assets

# GET endpoint to get asset by asset_id
@asset_router.get("/{id}")
def get_asset_by_id(id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (id,))
    asset = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    
    return asset

# GET endpoint to count total assets
@asset_router.get("/assets/count")
def count_assets():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM asset_inventory")
    count = cursor.fetchone()
    cursor.close()
    connection.close()
    
    return {"total_assets": count[0]}

# POST endpoint to create a new asset
@asset_router.post("/create")
def create_asset(asset: Asset):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """INSERT INTO asset_inventory (asset_tag, asset_type, serial_number, manufacturer, model, 
                    purchase_date, warranty_years, condition_status, assigned_to, location, asset_status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
                               asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
                               asset.assigned_to, asset.location, asset.asset_status))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Asset created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# # PUT endpoint to update full asset record by asset_id
# @asset_router.put("/{id}")
# def update_asset(id: int, asset: Asset):
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         query = """UPDATE asset_inventory SET asset_tag = %s, asset_type = %s, serial_number = %s, 
#                    manufacturer = %s, model = %s, purchase_date = %s, warranty_years = %s, 
#                    condition_status = %s, assigned_to = %s, location = %s, asset_status = %s 
#                    WHERE asset_id = %s"""
#         cursor.execute(query, (asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
#                                asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
#                                asset.assigned_to, asset.location, asset.asset_status, id))
#         connection.commit()
#         cursor.close()
#         connection.close()
#         return {"message": "Asset updated successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
#PUT endpoint to update full asset record by asset_id
@asset_router.put("/{id}")
def update_asset(id: int, asset: Asset):
    try:
        # First, check if the asset exists
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM asset_inventory WHERE asset_id = %s", (id,))
        count = cursor.fetchone()[0]
        
        if count == 0:
            cursor.close()
            connection.close()
            raise HTTPException(status_code=404, detail="Asset not found")
        
        # If the asset exists, perform the update
        query = """UPDATE asset_inventory 
                   SET asset_tag = %s, asset_type = %s, serial_number = %s, 
                       manufacturer = %s, model = %s, purchase_date = %s, 
                       warranty_years = %s, condition_status = %s, 
                       assigned_to = %s, location = %s, asset_status = %s 
                   WHERE asset_id = %s"""
        
        cursor.execute(query, (asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
                               asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
                               asset.assigned_to, asset.location, asset.asset_status, id))
        connection.commit()  # Commit the transaction
        cursor.close()
        connection.close()
        
        return {"message": "Asset updated successfully"}
    
    except pymysql.MySQLError as e:
        # MySQL errors, like lock wait timeout
        raise HTTPException(status_code=500, detail=f"MySQL error: {e}")
    except Exception as e:
        # General errors
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
    
# PATCH endpoint to update only the asset status
@asset_router.patch("/{id}/status")
def update_asset_status(id: int, asset_status: str):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE asset_inventory SET asset_status = %s WHERE asset_id = %s"
        cursor.execute(query, (asset_status, id))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Asset status updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# DELETE endpoint to delete an asset by asset_id
@asset_router.delete("/{id}")
def delete_asset(id: int):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM asset_inventory WHERE asset_id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Asset deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
