from src.model.model_maintenance_log import MaintenanceLog
from src.config.get_connection import get_connection


def create(data: MaintenanceLog):
    """
    Insert a new maintenance record into the maintenance_log table.
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO maintenance_log
    (asset_tag, maintenance_type, vendor_name, description, cost, maintenance_date, technician_name, status)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(query, (
        data.asset_tag, data.maintenance_type, data.vendor_name,
        data.description, data.cost, data.maintenance_date,
        data.technician_name, data.status
    ))

    conn.commit()
    conn.close()
    return "Maintenance record created successfully."


def get_all(status=None):
    """
    Retrieve all maintenance records.
    If status is provided, filter by status (e.g. Active, Pending, Completed).
    """
    conn = get_connection()
    cursor = conn.cursor()

    if status:
        cursor.execute("SELECT * FROM maintenance_log WHERE status=%s", (status,))
    else:
        cursor.execute("SELECT * FROM maintenance_log")

    result = cursor.fetchall()
    conn.close()
    return result


def get_by_id(log_id: int):
    """
    Retrieve a single maintenance record by log_id.
    Returns None if not found.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM maintenance_log WHERE log_id=%s", (log_id,))
    result = cursor.fetchone()

    conn.close()
    return result


def update(log_id: int, data: MaintenanceLog):
    """
    Update a full maintenance record.
    Replaces all editable fields using the provided MaintenanceLog model.
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE maintenance_log SET 
    asset_tag=%s, maintenance_type=%s, vendor_name=%s, description=%s,
    cost=%s, maintenance_date=%s, technician_name=%s, status=%s
    WHERE log_id=%s
    """

    cursor.execute(query, (
        data.asset_tag, data.maintenance_type, data.vendor_name,
        data.description, data.cost, data.maintenance_date,
        data.technician_name, data.status, log_id
    ))

    conn.commit()
    conn.close()
    return "Maintenance record updated successfully."


def set_status(log_id: int, status: str):
    """
    Update only the maintenance status field (PATCH style update).
    Useful for workflow updates.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE maintenance_log SET status=%s WHERE log_id=%s", (status, log_id))

    conn.commit()
    conn.close()
    return "Status updated successfully."


def delete(log_id: int):
    """
    Delete a maintenance record by log_id.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM maintenance_log WHERE log_id=%s", (log_id,))

    conn.commit()
    conn.close()
    return "Maintenance record deleted."


def find(column, value):
    """
    Search for records using partial match on allowed columns.
    Uses parameterized queries to avoid SQL injection.
    """
    allowed_columns = [
        "asset_tag", "maintenance_type", "vendor_name", "description",
        "cost", "maintenance_date", "technician_name", "status"
    ]

    if column not in allowed_columns:
        raise Exception(f"Invalid search column: {column}")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM maintenance_log WHERE {column} LIKE %s", (f"%{value}%",))
    result = cursor.fetchall()

    conn.close()
    return result


def get_count():
    """
    Count total number of maintenance records.
    Returns a single number.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) as total FROM maintenance_log")
    result = cursor.fetchone()[0]

    conn.close()
    return result
