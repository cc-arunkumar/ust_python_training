import pymysql
from config.db_connection import get_connection

# 1. Create a new maintenance record
def create_maintenance(maintenance):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            query = """
            INSERT INTO aims_db.maintenance_log (maintenance_code, equipment_id, description, maintenance_date, status)
            VALUES (%s, %s, %s, %s, %s)
            """
            data = (maintenance['maintenance_code'], maintenance['equipment_id'], maintenance['description'],
                    maintenance['maintenance_date'], maintenance['status'])
            cursor.execute(query, data)
            conn.commit()
    except Exception as e:
        return {"error": str(e)}

# 2. Get all maintenance records
def get_all_maintenance():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM aims_db.maintenance_log"
            cursor.execute(query)
            rows = cursor.fetchall()  # Fetch all rows from the database
            return rows  # Return as list of tuples
    except Exception as e:
        return {"error": str(e)}

# 3. Get maintenance records by status
def get_maintenance_by_status(status):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM aims_db.maintenance_log WHERE status = %s"
            cursor.execute(query, (status,))
            rows = cursor.fetchall()  # Fetch all rows matching the status
            return rows  # Return as list of tuples
    except Exception as e:
        return {"error": str(e)}

# 4. Get a maintenance record by ID
def get_maintenance_by_id(id):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM aims_db.maintenance_log WHERE maintenance_id = %s"
            cursor.execute(query, (id,))
            row = cursor.fetchone()  # Fetch a single row by ID
            return row  # Return as a tuple or None if not found
    except Exception as e:
        return {"error": str(e)}

# 5. Update a maintenance record by ID
def update_maintenance(id, maintenance):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            query = """
            UPDATE aims_db.maintenance_log SET maintenance_code = %s, equipment_id = %s, description = %s, 
            maintenance_date = %s, status = %s WHERE maintenance_id = %s
            """
            data = (maintenance["maintenance_code"], maintenance["equipment_id"], maintenance["description"],
                    maintenance["maintenance_date"], maintenance["status"], id)
            cursor.execute(query, data)
            conn.commit()
    except Exception as e:
        return {"error": str(e)}

# 6. Update maintenance status by ID
def update_maintenance_status(id, status):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            query = "UPDATE aims_db.maintenance_log SET status = %s WHERE maintenance_id = %s"
            cursor.execute(query, (status, id))
            conn.commit()
    except Exception as e:
        return {"error": str(e)}

# 7. Delete a maintenance record by ID
def delete_maintenance(id):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            query = "DELETE FROM aims_db.maintenance_log WHERE maintenance_id = %s"
            cursor.execute(query, (id,))
            conn.commit()
    except Exception as e:
        return {"error": str(e)}

# 8. Search maintenance records by keyword
def search_maintenance_by_keyword(keyword):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM aims_db.maintenance_log WHERE maintenance_code LIKE %s OR description LIKE %s"
            like_keyword = f"%{keyword}%"
            cursor.execute(query, (like_keyword, like_keyword))
            rows = cursor.fetchall()  # Fetch all rows that match the keyword
            return rows  # Return as list of tuples
    except Exception as e:
        return {"error": str(e)}

# 9. Get count of maintenance records
def get_maintenance_count():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT COUNT(*) FROM aims_db.maintenance_log"
            cursor.execute(query)
            count = cursor.fetchone()[0]  # Fetch the count value
            return count  # Return the count as an integer
    except Exception as e:
        return {"error": str(e)}
