from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
import pymysql

# -------------------------------
# Initialize FastAPI Router
# -------------------------------
# This router groups all endpoints related to maintenance logs.
# Prefix "/maintenance" means all routes will start with /maintenance.
# Tags are used for API documentation grouping.
maintenance_router = APIRouter(prefix="/maintenance", tags=['Maintenance'])

# -------------------------------
# Database Connection Function
# -------------------------------
# Creates and returns a connection to the MySQL database.
# DictCursor ensures query results are returned as dictionaries instead of tuples.
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db",
        cursorclass=pymysql.cursors.DictCursor
    )

# -------------------------------
# Pydantic Model for Maintenance Log
# -------------------------------
# Defines the structure of a maintenance log record.
# Excludes log_id since it is AUTO_INCREMENT in the database.
class MaintenanceLog(BaseModel):
    asset_tag: str
    maintenance_type: str
    vendor_name: str
    description: str
    cost: float
    maintenance_date: str
    technician_name: str
    status: str


# -------------------------------
# POST Endpoint
# -------------------------------

# POST /maintenance/create
# Create a new maintenance log entry in the database.
@maintenance_router.post("/create")
def create_maintenance_log(log: MaintenanceLog):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """INSERT INTO maintenance_log 
                   (asset_tag, maintenance_type, vendor_name, description, 
                    cost, maintenance_date, technician_name, status)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (log.asset_tag, log.maintenance_type, log.vendor_name, log.description,
                               log.cost, log.maintenance_date, log.technician_name, log.status))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Maintenance log created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# -------------------------------
# GET Endpoints
# -------------------------------

# GET /maintenance/list
# Fetch all maintenance logs from the database.
@maintenance_router.get("/list")
def get_all_maintenance_logs():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM maintenance_log")
        logs = cursor.fetchall()
        cursor.close()
        connection.close()
        return logs
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# GET /maintenance/list/status?status=
# Fetch maintenance logs filtered by their status (e.g., Completed, Pending).
@maintenance_router.get("/list/status")
def get_maintenance_logs_by_status(status: str):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM maintenance_log WHERE LOWER(status) = LOWER(%s)"
        cursor.execute(query, (status,))
        logs = cursor.fetchall()
        cursor.close()
        connection.close()
        return logs
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# GET /maintenance/search?keyword=
# Search maintenance logs by keyword across multiple fields.
@maintenance_router.get("/search")
def search_maintenance_logs(keyword: str):
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM maintenance_log 
               WHERE asset_tag LIKE %s OR maintenance_type LIKE %s OR vendor_name LIKE %s 
               OR description LIKE %s OR technician_name LIKE %s OR status LIKE %s"""
    like_pattern = f"%{keyword}%"
    cursor.execute(query, (like_pattern,) * 6)  # Apply keyword to all searchable fields
    logs = cursor.fetchall()
    cursor.close()
    connection.close()
    return logs


# GET /maintenance/{id}
# Retrieve a single maintenance log by its unique ID.
@maintenance_router.get("/{id}")
def get_maintenance_log_by_id(id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM maintenance_log WHERE log_id = %s", (id,))
    log = cursor.fetchone()
    cursor.close()
    connection.close()

    if log is None:
        raise HTTPException(status_code=404, detail="Maintenance log not found")

    return log


# GET /maintenance/count
# Return the total number of maintenance logs in the database.
@maintenance_router.get("/count")
def count_maintenance_logs():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) AS total FROM maintenance_log")
        count = cursor.fetchone()["total"]
        cursor.close()
        connection.close()
        return {"total_logs": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


# -------------------------------
# PUT Endpoint
# -------------------------------

# PUT /maintenance/{id}
# Update an existing maintenance log by ID (full update of all fields).
@maintenance_router.put("/{id}")
def update_maintenance_log(id: int, log: MaintenanceLog):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Check if log exists before updating
        cursor.execute("SELECT COUNT(*) AS count FROM maintenance_log WHERE log_id = %s", (id,))
        count = cursor.fetchone()["count"]

        if count == 0:
            cursor.close()
            connection.close()
            raise HTTPException(status_code=404, detail="Maintenance log not found")

        # Perform update
        query = """UPDATE maintenance_log 
                   SET asset_tag = %s, maintenance_type = %s, vendor_name = %s, 
                       description = %s, cost = %s, maintenance_date = %s, 
                       technician_name = %s, status = %s 
                   WHERE log_id = %s"""
        cursor.execute(query, (log.asset_tag, log.maintenance_type, log.vendor_name, log.description,
                               log.cost, log.maintenance_date, log.technician_name, log.status, id))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Maintenance log updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")


# -------------------------------
# PATCH Endpoint
# -------------------------------

# PATCH /maintenance/{id}/status
# Update only the status field of a maintenance log (partial update).
@maintenance_router.patch("/{id}/status")
def update_maintenance_log_status(id: int, status: str):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE maintenance_log SET status = %s WHERE log_id = %s"
        cursor.execute(query, (status, id))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Maintenance log status updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# -------------------------------
# DELETE Endpoint
# -------------------------------

# DELETE /maintenance/{id}
# Delete a maintenance log by ID.
# After deletion, reorder log_id values sequentially and reset AUTO_INCREMENT.
@maintenance_router.delete("/{id}")
def delete_maintenance_log(id: int):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Delete the log
        query = "DELETE FROM maintenance_log WHERE log_id = %s"
        cursor.execute(query, (id,))
        connection.commit()

        # Reorder IDs sequentially
        cursor.execute("SET @count = 0;")
        cursor.execute("UPDATE maintenance_log SET log_id = (@count:=@count+1) ORDER BY log_id;")

        # Reset AUTO_INCREMENT to max(log_id)+1
        cursor.execute("SELECT COALESCE(MAX(log_id), 0) + 1 AS next_id FROM maintenance_log")
        next_id = cursor.fetchone()["next_id"]
        cursor.execute(f"ALTER TABLE maintenance_log AUTO_INCREMENT = {next_id}")
        connection.commit()

        cursor.close()
        connection.close()
        return {"message": "Maintenance log deleted successfully, IDs reordered"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
