from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
import pymysql
from io import StringIO
from datetime import date

# Initialize FastAPI maintenance_router
maintenance_router = APIRouter(prefix="/maintenance")

# Database connection function
def get_connection():
    # Establishes a connection to the MySQL database
    return pymysql.connect(
        host="localhost",  # MySQL host
        user="root",  # MySQL user
        password="pass@word1",  # MySQL password
        database="ust_asset_db"  # Your database name
    )

# Pydantic model for Maintenance
class Maintenance(BaseModel):
    # Defines the structure for Maintenance data with validation
    asset_tag: str
    maintenance_type: str
    vendor_name: str
    description: str
    cost: float
    maintenance_date: date
    technician_name: str
    status: str

# ------------------- POST Endpoint -------------------

# POST /maintenance/create
@maintenance_router.post("/create")
def create_maintenance(maintenance: Maintenance):
    # Creates a new maintenance log entry in the database
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """INSERT INTO maintenance_log (asset_tag, maintenance_type, vendor_name, description, cost, 
                    maintenance_date, technician_name, status) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (maintenance.asset_tag, maintenance.maintenance_type, maintenance.vendor_name, 
                               maintenance.description, maintenance.cost, maintenance.maintenance_date, 
                               maintenance.technician_name, maintenance.status))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Maintenance log created successfully"}  # Success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Error handling


# ------------------- GET Endpoints -------------------

# GET /maintenance/list (fetch all maintenance logs)
@maintenance_router.get("/maintenance/list")
def get_all_maintenance():
    # Fetches all maintenance logs from the database
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM maintenance_log")
        maintenance_logs = cursor.fetchall()
        cursor.close()
        connection.close()
        return maintenance_logs  # Return all logs
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))  # Error handling


# GET /maintenance/list (filter maintenance logs by status)
@maintenance_router.get("/list")
def get_maintenance_by_status(status: str):
    # Filters maintenance logs based on their status (Completed/Pending)
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM maintenance_log WHERE status = %s"
        cursor.execute(query, (status,))
        maintenance_logs = cursor.fetchall()
        cursor.close()
        connection.close()
        return maintenance_logs  # Return filtered logs
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))  # Error handling


# GET /maintenance/search?column=value (search logs by keyword)
@maintenance_router.get("/search")
def search_maintenance(column: str, value: str):
    # Searches maintenance logs based on a specific column and value
    valid_columns = ["log_id", "asset_tag", "maintenance_type", "vendor_name", "description", "cost", 
                     "maintenance_date", "technician_name", "status"]
    
    # Check if the provided column is valid to prevent SQL injection
    if column not in valid_columns:
        raise HTTPException(status_code=400, detail="Invalid column name")
    
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        # Construct the search query
        query = f"SELECT * FROM maintenance_log WHERE {column} LIKE %s"
        search_pattern = f"%{value}%"
        
        # Execute the query
        cursor.execute(query, (search_pattern,))
        maintenance_logs = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        if not maintenance_logs:
            raise HTTPException(status_code=404, detail="No maintenance logs found")
        
        return maintenance_logs  # Return matching logs
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))  # Error handling


# GET /maintenance/{id} (fetch a single maintenance log by log_id)
@maintenance_router.get("/{id}")
def get_maintenance_by_id(id: int):
    # Fetches a specific maintenance log based on its log_id
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM maintenance_log WHERE log_id = %s"
        cursor.execute(query, (id,))
        maintenance_log = cursor.fetchone()
        cursor.close()
        connection.close()
        if maintenance_log is None:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return maintenance_log  # Return the found log
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))  # Error handling


# ------------------- PUT Endpoint -------------------

# PUT /maintenance/{id} (update a maintenance log)
@maintenance_router.put("/{id}")
def update_maintenance(id: int, maintenance: Maintenance):
    # Updates an existing maintenance log by log_id
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM maintenance_log WHERE log_id = %s", (id,))
        count = cursor.fetchone()[0]
        
        if count == 0:
            cursor.close()
            connection.close()
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        
        query = """UPDATE maintenance_log SET asset_tag = %s, maintenance_type = %s, vendor_name = %s, 
                   description = %s, cost = %s, maintenance_date = %s, technician_name = %s, status = %s 
                   WHERE log_id = %s"""
        
        cursor.execute(query, (maintenance.asset_tag, maintenance.maintenance_type, maintenance.vendor_name, 
                               maintenance.description, maintenance.cost, maintenance.maintenance_date, 
                               maintenance.technician_name, maintenance.status, id))
        connection.commit()  # Commit the transaction
        cursor.close()
        connection.close()
        
        return {"message": "Maintenance log updated successfully"}  # Success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Error handling


# ------------------- PATCH Endpoint -------------------

# PATCH /maintenance/{id}/status (update status of a maintenance log)
@maintenance_router.patch("/{id}/status")
def update_maintenance_status(id: int, status: str):
    # Updates the status of a maintenance log by its log_id
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE maintenance_log SET status = %s WHERE log_id = %s"
        cursor.execute(query, (status, id))
        connection.commit()  # Commit the transaction
        cursor.close()
        connection.close()
        return {"message": "Maintenance log status updated successfully"}  # Success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Error handling


# ------------------- DELETE Endpoint -------------------

# DELETE /maintenance/{id} (delete a maintenance log by log_id)
@maintenance_router.delete("/{id}")
def delete_maintenance(id: int):
    # Deletes a maintenance log from the database by log_id
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM maintenance_log WHERE log_id = %s"
        cursor.execute(query, (id,))
        connection.commit()  # Commit the transaction
        cursor.close()
        connection.close()
        return {"message": "Maintenance log deleted successfully"}  # Success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Error handling


# ------------------- GET Endpoint for Count -------------------

# GET /maintenance/count (count the total number of maintenance logs)
@maintenance_router.get("/maintenance/count")
def count_maintenance():
    # Fetches the total number of maintenance logs in the database
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM maintenance_log"
        cursor.execute(query)
        count = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return {"total_maintenance_logs": count}  # Return count
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))  # Error handling
